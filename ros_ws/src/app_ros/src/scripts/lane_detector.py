#!/usr/bin/env python3

import rospy 
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def callback(data):
    bridge = CvBridge()
    #rospy.loginfo(rospy.get_caller_id() + " Encoding = %s ", data.encoding)
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')  

    cv2.namedWindow('RGB Image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow("RGB Image", cv_image)
    cv2.waitKey(5)

    edges = cv2.Canny(cv_image, 50, 200)
    cv2.namedWindow('Image Canny', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Image Canny', edges)
    cv2.waitKey(5)     
    
def get_image():
    rospy.init_node('lane_detector', anonymous=True)
    rospy.Subscriber("/image_raw", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    get_image()
  
    
