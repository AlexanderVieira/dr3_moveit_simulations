#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################
#                                           #
# Node to control the Turtlebot3 simulator. #
# This node receives image poit and sends   #
# control signal to the cmd_vel topic.      #
#                                           #
# Author: Alexander Silva                   #
# Autonomous Vehicle - Infnet	            #
# Version: 1.0                              #
# Date: 29-03-2021                          #
#                                           #
#############################################

# importing libraries
import rospy, time, sys, math, control_lib, tf
import numpy as np
import control_lib_v2 as ctrl
from geometry_msgs.msg import Pose2D, Twist, PointStamped
from turtlesim.msg import Pose
from std_msgs.msg import Bool, Int32, Int32MultiArray
from nav_msgs.msg import Odometry
from sensor_msgs.msg import CameraInfo
import image_geometry
from smach import State,StateMachine
import smach_ros

############ WORK FUNCTIONS ##################

def callback_camera_info(msg):

    global model
    global camera_matrix
    
    model.fromCameraInfo(msg)
    
    K = np.array(msg.K).reshape([3, 3])
    f = K[0][0]
    u0 = K[0][2]
    v0 = K[1][2]

    camera_matrix[0] = f
    camera_matrix[1] = u0
    camera_matrix[2] = v0
   
def callback_img_point(msg):
    """
    This function receives the goal and saves it 
    in a globa variable goal
    """

    global camera_height
    global image_point
    global mask_is_true        

    # recovering point
    u = msg.x
    v = msg.y
    base_point = [u, v]
    mask_is_true = msg.theta
    distance = 0     

    try:
        # finding distance to the point 
        pixel_rectified = model.rectifyPoint(base_point)
        line = model.projectPixelTo3dRay(pixel_rectified)
        th = math.atan2(line[2],line[1])
        distance = math.tan(th) * camera_height        
        # image_point = Pose2D()
        image_point.x = u #u
        image_point.y = v #v
        image_point.theta = distance

        rospy.loginfo(rospy.get_caller_id() + " Distance do objeto = %s m", '{:.2f}'.format(image_point.theta))
        rospy.loginfo(rospy.get_caller_id() + " Ponto base u = %s pixel", '{:.2f}'.format(image_point.x))
        rospy.loginfo(rospy.get_caller_id() + " Ponto base v = %s pixel", '{:.2f}'.format(image_point.y))

    except:
        pass  
    
    
def callback_odom(msg):
   
    global robot_pose
    
    robot_pose.x = round(msg.pose.pose.position.x, 3)
    robot_pose.y = round(msg.pose.pose.position.y, 3)

    # rospy.loginfo(robot_pose.x) 
    # rospy.loginfo(robot_pose.y)
    
    q = [msg.pose.pose.orientation.x, 
        msg.pose.pose.orientation.y, 
        msg.pose.pose.orientation.z, 
        msg.pose.pose.orientation.w]

    euler = tf.transformations.euler_from_quaternion(q)
    
    theta = round(euler[2],3)
    
    robot_pose.theta = theta


def callback_control_type(msg):
    """
    This function receives the type of controller:
    0: Cartesian control
    1: Polar control
    """
    global ctrl_type 
    ctrl_type = msg.data


def control_robot():
    """
    This function is called from the main conde and calls 
    all work methods of fucntions into the codde.
    """

    # Global variables     
    global image_point
    global robot_pose
    global gains_cart
    global ctrl_type       
    global camera_matrix
    global mask_is_true
    global vel_lim
    global threshold
    global error_int    
    global errors
    
    # Initializing ros node
    rospy.init_node('turtlebot3_control', anonymous=True)    # node name
    
    # Subscribers
    rospy.Subscriber('img_point', Pose2D, callback_img_point)   # receives the goal coordinates
    rospy.Subscriber('odom', Odometry, callback_odom)    # receives thr robot odometry
    rospy.Subscriber('control_type',Int32,callback_control_type) #receives c.t.
    rospy.Subscriber('camera_info',CameraInfo, callback_camera_info)   # receives the goal coordinates
    # rospy.Subscriber('mask_is_true',Bool, callback_mask_is_true)

    # Publishers
    cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)  # send control signals

    # control rate
    rate = rospy.Rate(10)   # run the node at 15H

    # main loop
    while not rospy.is_shutdown():

        # Computing the control signal
        control_signal = Twist()       

        # calling PBVS
        try:
            if ctrl_type == 0:                
                
                # controle cartesiano
                control_signal = ctrl.pbvs(image_point, camera_matrix, robot_pose, gains_cart, vel_lim, threshold)         
                #rospy.loginfo(rospy.get_caller_id() + " (error_lin) = %s m", '{:.2f}'.format(errors[0]))

            if ctrl_type == 1:
                
                # controle polar
                control_signal = ctrl.pbvs_v1(image_point, camera_matrix, robot_pose, gains_cart, vel_lim, threshold)
                #rospy.loginfo(rospy.get_caller_id() + " (rho) = %s m", '{:.2f}'.format(errors[0]))

            if ctrl_type == 2:

                # controle rastreamento
                control_signal = ctrl.pbvs_v2(image_point, camera_matrix, robot_pose, gains_cart, vel_lim, threshold, error_int)
                #rospy.loginfo(erros)
                #rospy.loginfo(rospy.get_caller_id() + " Rastreador (error_lin) = %s m", '{:.2f}'.format(errors[0]))             

            else:
                control_signal = Twist()
                control_signal.linear.x = 0.0
                control_signal.angular.z = 0.5
        except:
            pass

        #print control_signal
        cmd_vel.publish(control_signal)       
                
        rate.sleep()

############ MAIN CODE #######################
# initializing Global variables
# Readin from launch
K_eu = float(sys.argv[1])   # Control gain for linear velocity
K_ev = float(sys.argv[2])   # Control gain for angular velocity
K_rho = float(sys.argv[3])   
K_alpha = float(sys.argv[4])   
K_beta = float(sys.argv[5]) 
K_int = float(sys.argv[6]) 
threshold = float(sys.argv[7])
max_lin = float(sys.argv[8])
max_ang = float(sys.argv[9])
ctrl_type = int(sys.argv[10])
camera_height = float(sys.argv[11])


# Inner values
robot_pose = Pose2D()
image_point = Pose2D()
gains_cart = [K_eu, K_ev, K_rho, K_alpha, K_beta, K_int]
camera_matrix = np.zeros((3,1))
vel_lim = [max_lin, max_ang]
mask_is_true = False
errors = []
error_int = 0.0


# creating a camera model
model = image_geometry.PinholeCameraModel()

if __name__ == '__main__':
    control_robot()
   
    # try:
    #     control_robot()
    # except:
    #     print('Node ended.')
      
