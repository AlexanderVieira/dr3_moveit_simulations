#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy, time, math
from geometry_msgs.msg import Quaternion

def main_goal():
    global x
    global y
    global z
    global w    

    rospy.init_node('send_goal', anonymous=True)    # node name
    goal_pub = rospy.Publisher('/panda_goal', Quaternion, queue_size=10, latch=True)

    rate = rospy.Rate(15)

    goal = Quaternion()
    goal.x = x
    goal.y = y
    goal.z = z
    goal.w = w
    
    while not rospy.is_shutdown():
        print(goal)
        goal_pub.publish(goal)
        rate.sleep()


################# Main ########################

x = eval(input("Digite a posicao desejada no eixo X com formato 0.0: "))
y = eval(input("Digite a posicao desejada no eixo y com formato 0.0: "))
z = eval(input("Digite a posicao desejada no eixo z com formato 0.0: "))
w = eval(input("Digite a posicao desejada no eixo w com formato 0.0: "))

if __name__ == '__main__':
    main_goal()
