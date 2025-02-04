#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################
#                                           #
# Library for robot control with different  #
# approaches and other usefull functions.   #
#                                           #
# Changes:                                  #
#    * Threshold option for cartesian       #
#      ans polar control functions          #
#    * IBVS funtion for image based visual  #
#      servoin control.                     #
#    * Function for recover the coordinate  #
#      of a point in the image with respect #
#      to the camera frame.                 #
#                                           #
# Author: Adalberto Oliveira                #
# Autonomous Vehicle - Infnet	            #
# Version: 1.4                              #
# Date: 21-10-2021                          #
#                                           #
#############################################


import rospy, time, sys, math, angles
import numpy as np
from geometry_msgs.msg import Pose2D, Twist, PointStamped
from turtlesim.msg import Pose
import image_geometry
#import tf
import tf2_ros as tf2
import tf2_geometry_msgs


def cartesian_control(robot_pose,goal,K_v,K_omega,max_lin=0.5, max_ang=0.5, threshold=0):
    """
    This function computes the control signal to guides the 
    robot to the desired goal. It's based on the Cartesian
    Control Algorithm
    """

    # Computing the position error
    error_x = goal.x - robot_pose.x
    error_y = goal.y - robot_pose.y
    error_lin = round(math.sqrt(error_x**2 + error_y**2)-threshold,2)
    v = K_v*error_lin

    # Computing the heading
    heading = math.atan2(error_y,error_x)
    error_th = round(angles.shortest_angular_distance(robot_pose.theta,heading),2)
    
    omega = K_omega*error_th

    # velocity limitation
    v = max_lin*np.sign(v) if abs(v) > max_lin else v
    omega = max_ang*np.sign(omega) if abs(omega) > max_ang else omega

    print('Error lin:',error_lin, 'Erro heading:',error_th)

    u = Twist()

    u.linear.x = v
    u.angular.z = omega

    return u

# Author: Alexander Silva
# Autonomous Vehicle - Infnet	            
# Version: 1.0                              
# Date: 29-03-2021                          
def cartesian_control_v1(robot_pose,goal_stamped,K_v,K_omega,max_lin, max_ang, threshold):
        
    rospy.loginfo(rospy.get_caller_id() + " Posição robot_pose X: %s m", '{:.2f}'.format(robot_pose.x))
    rospy.loginfo(rospy.get_caller_id() + " Posição robot_pose Y: %s m", '{:.2f}'.format(robot_pose.y))
    rospy.loginfo(rospy.get_caller_id() + " Posição goal_stamped X: %s m", '{:.2f}'.format(goal_stamped.point.x))
    rospy.loginfo(rospy.get_caller_id() + " Posição goal_stamped Y: %s m", '{:.2f}'.format(goal_stamped.point.y))
    rospy.loginfo(rospy.get_caller_id() + " Ganho linear: %s", '{:.2f}'.format(K_v))
    rospy.loginfo(rospy.get_caller_id() + " Ganho angular: %s", '{:.2f}'.format(K_omega))
    rospy.loginfo(rospy.get_caller_id() + " Regulação parcial: %s m", '{:.2f}'.format(threshold))
        
    # Computing the position error
    error_x = goal_stamped.point.x - robot_pose.x
    error_y = goal_stamped.point.y - robot_pose.y
    error_lin = round(math.sqrt(error_x**2 + error_y**2)-threshold,2)
    v = K_v*error_lin

    # Computing the heading
    heading = math.atan2(error_y,error_x)
    error_th = round(angles.shortest_angular_distance(robot_pose.theta,heading),2)
    
    omega = K_omega*error_th

    # velocity limitation
    v = max_lin*np.sign(v) if abs(v) > max_lin else v
    omega = max_ang*np.sign(omega) if abs(omega) > max_ang else omega

    rospy.loginfo(rospy.get_caller_id() + " error_lin: %s", '{:.2f}'.format(error_lin))
    rospy.loginfo(rospy.get_caller_id() + " error_th: %s", '{:.2f}'.format(error_th))

    u = Twist()

    u.linear.x = v
    u.angular.z = omega

    return u    


def polar_control(robot_pose,goal,K_rho,K_alpha, K_beta, max_lin=0.5, max_ang=0.5, threshold=0):
    """
    This function computes the control signal to guides the 
    robot to the desired goal. It's based on the Cartesian
    Control Algorithm
    """

    # recovering the variables
    x = robot_pose.x
    y = robot_pose.y
    theta = robot_pose.theta

    x_d = goal.x
    y_d = goal.y
    theta_d = goal.theta

    # Computing the position error
    delta_x = x_d - x
    delta_y = y_d - y
    heading = math.atan2(delta_y,delta_x)

    # Creating the new variables
    rho  = round(math.sqrt(delta_x**2 + delta_y**2)-threshold,2)
    alpha = round(angles.shortest_angular_distance(theta,heading),2)
    beta = round(- theta - alpha + theta_d,2)
    #beta = round(angles.shortest_angular_distance(heading,theta_d),2)
   
    # Computing control signals
    #v = round(K_rho*rho,3)
    
    # Non-Linear control for rho
    v = round(K_rho*rho*math.cos(alpha),2)

    omega = round(K_alpha*alpha + K_beta*beta,2)

    print('Rho:',rho,
    		'\nAlpha:',alpha,
            '\nBeta:',beta)

    # velocity limitation
    v = max_lin*np.sign(v) if abs(v) > max_lin else v
    omega = max_ang*np.sign(omega) if abs(omega) > max_ang else omega


    u = Twist()

    u.linear.x = v
    u.angular.z = omega

    return u


def tracking_control(donkey_pose, master_pose, delta_tracking, gains, error_int, max_vel):
    """
    This function computes the control signal to guides the 
    robot to the desired goal. It's based on the Cartesian
    Control Algorithm
    """
    
    # Recovering control gains
    K_v = gains[0]    
    K_omega = gains[1]
    K_int = gains[5]

    # Recovering velocitie limits
    max_lin_vel = max_vel[0]
    max_ang_vel = max_vel[1]

    # Computing the position error
    error_x = master_pose.x - donkey_pose.x
    error_y = master_pose.y - donkey_pose.y
    error_lin = round(math.sqrt(error_x**2 + error_y**2)-delta_tracking,3)
    error_int += error_lin*0.066

    # Computing the heading
    heading = math.atan2(error_y,error_x)
    error_th = round(angles.shortest_angular_distance(donkey_pose.theta, heading),3)
    
    errors = [error_int, error_lin, error_th]

    # Computing control signals
    v = K_v*error_lin + K_int*error_int
    v = np.sign(v)*max_lin_vel if v > max_lin_vel else v

    omega = K_omega*error_th
    omega = np.sign(omega)*max_ang_vel if omega > max_ang_vel else omega

    u = Twist()

    u.linear.x = v
    u.angular.z = omega

    return u, errors


def ibvs(img_goal, image_point, camera_matrix, gains_cart,vel_lim):
    """
    This function receives the destination pixel (img_goal), the current 
    pixel coordinate and camera matrix, and returns the control signal based on 
    IBVS approach, with control gains and velocity limits 
    """

    # recovering goal point
    ud = img_goal.x
    vd = img_goal.y

    # Recovering image point
    u = image_point.x
    v = image_point.y

    # Recovering velocity limits
    lim_lin = vel_lim[0]
    lim_ang = vel_lim[1]

    # getting camera parameters
    Z = image_point.theta
    f = camera_matrix[0]
    u0 = camera_matrix[1]
    v0 = camera_matrix[2]

    # Creating the Jacobian matrix
    u_ = u - u0
    v_ = v - v0

    j11 = u_/Z
    j12 = ((f**2 + u_**2)/ f)+((19*f)/(250*Z))
    j21 = v_/Z
    j22 = (u_*v_)/f

    J = np.zeros((2,2))
    J[0][0] = j11
    J[0][1] = j12
    J[1][0] = j21
    J[1][1] = j22

    J_inv = np.linalg.inv(J)

    # defining image error
    e_u = ud - u
    e_v = vd - v

    e = np.zeros((2,1))
    e[0] = e_u
    e[1] = e_v

    # creating control law
    K = np.zeros((2,2))
    K[0][0] = gains_cart[0]
    K[1][1] = gains_cart[1]

    m1 = np.matmul(K,e)

    U = np.matmul(J_inv, m1)
    
    # creating control message
    cmd_vel = Twist()
    
    # velocity limiter
    v = round(U[0][0],3) if abs(U[0][0]) <= lim_lin else lim_lin*np.sign(U[0][0]) 
    w = round(U[1][0],3) if abs(U[1][0]) <= lim_ang else lim_ang*np.sign(U[1][0]) 

    cmd_vel.linear.x = v
    cmd_vel.angular.z = w

    return cmd_vel

# Author: Alexander Silva
# Autonomous Vehicle - Infnet	            
# Version: 1.0                              
# Date: 29-03-2021    
def pbvs(image_point, camera_matrix, robot_pose, gains_cart, vel_lim, threshold):
    
    # Recovering gains
    k_v = gains_cart[0]
    k_w = gains_cart[1]

    # Recovering velocity limits
    max_lin = vel_lim[0]
    max_ang = vel_lim[1]

    goal_stamped = PointStamped()
    cam_point = PointStamped()
    cmd_vel = Twist()

    cam_point = get_img_point(image_point, camera_matrix, frame_id='camera_link')
    #rospy.loginfo(cam_point)
    goal_stamped = get_goal_stamped(cam_point)
    #rospy.loginfo(goal_stamped)
    cmd_vel = cartesian_control_v1(robot_pose, goal_stamped, k_v, k_w, max_lin, max_ang, threshold)
    #rospy.loginfo(cmd_vel)

    return cmd_vel

def get_img_point(image_point, camera_matrix, frame_id):
    """
    This function receives the image point in pixel and returns the point 
    coordinate in the camera frame as a PointStamped object with frame_id.
    """
    
    #rospy.loginfo(camera_matrix)
    #rospy.loginfo(image_point)

    # Recovering image point
    u = image_point.x
    v = image_point.y

    # getting camera parameters
    Z = image_point.theta
    f = camera_matrix[0]
    u0 = camera_matrix[1]
    v0 = camera_matrix[2]

    # Transforming from pixel to image coordinates
    if f != 0.0:
        x_i = (1/f)*(u - u0)
        y_i = (1/f)*(v - v0)

    # Converting from image frame to camera frame
    x_c = Z 
    y_c = -x_i * Z 
    z_c = -y_i * Z

    # Creating camera point
    camera_point = PointStamped()

    camera_point.header.stamp = rospy.Time()
    camera_point.header.frame_id = frame_id
    camera_point.point.x = x_c
    camera_point.point.y = y_c
    camera_point.point.z = z_c

    #rospy.loginfo(camera_point)

    return camera_point

# Author: Alexander Silva
# Autonomous Vehicle - Infnet	            
# Version: 1.0                              
# Date: 29-03-2021    
def get_goal_stamped(cam_point):
   
    #rospy.loginfo(cam_point)

    img_goal = PointStamped()
    tran = PointStamped()

    # creating transformation engine
    #listener = tf.TransformListener()
    tfBuffer = tf2.Buffer()
    listener = tf2.TransformListener(tfBuffer)
   
    # filling the object 
    img_goal.header.stamp = rospy.Time()   # getting time stamp
    img_goal.header.frame_id = cam_point.header.frame_id
    img_goal.point.x = cam_point.point.x 
    img_goal.point.y = cam_point.point.y
    img_goal.point.z = cam_point.point.z
    
    #rate = rospy.Rate(10)
    tran = tfBuffer.transform(img_goal, "odom", timeout=rospy.Duration(10))
    #rate.sleep()
    #rospy.loginfo(tran)

    return tran
