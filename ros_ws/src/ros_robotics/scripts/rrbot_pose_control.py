#!/usr/bin/env python3

import rospy
from moveit_msgs.msg import MoveGroupActionGoal
from std_msgs.msg import Float64
from time import sleep

def move_group_callback(moveit_msg):
    base_mid = moveit_msg.goal.request.goal_constraints[0].joint_constraints[0].position
    mid_top = moveit_msg.goal.request.goal_constraints[0].joint_constraints[1].position
    rospy.loginfo(rospy.get_caller_id() + " X joint_base_mid angle is = %s rad", '{:.2f}'.format(base_mid))
    rospy.loginfo(rospy.get_caller_id() + " X joint_mid_top angle is = %s rad", '{:.2f}'.format(mid_top))
    main(base_mid, mid_top)

def main(arg1, arg2):
    base_mid_pub = rospy.Publisher('/rrbot/joint_base_mid_position_controller/command', Float64, queue_size=10)        
    base_mid_pub.publish(arg1)
    mid_top_pub = rospy.Publisher('/rrbot/joint_mid_top_position_controller/command', Float64, queue_size=10)    
    mid_top_pub.publish(arg2)    
            
if __name__ == '__main__':
    
    rospy.init_node('pose_control')
    while not rospy.is_shutdown():
            rospy.Subscriber('/move_group/goal', MoveGroupActionGoal, move_group_callback)             
            sleep(0.1)            
    

        
        
        
    