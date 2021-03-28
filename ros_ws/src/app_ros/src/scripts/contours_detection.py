#!/usr/bin/env python3

import rospy, sys, time, cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
#import rospkg
#import glob

def read_ros_image(video, show):

    #rospack = rospkg.RosPack()
    #img_path = rospack.get_path('app_ros')+'/images'
    #rgb_image = np.array([cv2.imread(file) for file in glob.glob(img_path + image_name)])
    
    #rgb_image = np.array(cv2.imread(image_name, 0))
    # average = rgb_image.mean(axis=0).mean(axis =0)
    # print(average)

     # Lendo a camera
    _,cv_image = video.read() 

    if show: 
        cv2.namedWindow('RGB Image', cv2.WINDOW_AUTOSIZE)
        cv2.imshow("RGB Image",cv_image)
        cv2.waitKey(5)
        
    bridge = CvBridge()
    img_msg = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")  

    return img_msg

def convert_rgb_to_gray(rgb_image,show):
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    if show: 
        cv2.imshow("Gray Image",gray_image)
    return gray_image

def convert_gray_to_binary(gray_image, adaptive, show):
    if adaptive: 
        binary_image = cv2.adaptiveThreshold(gray_image, 
                            255, 
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                            cv2.THRESH_BINARY_INV, 115, 2)
    else:
        _,binary_image = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY_INV)
    if show:
        cv2.imshow("Binary Image", binary_image)
    return binary_image    

def getContours(binary_image):      
    contours, hierarchy = cv2.findContours(binary_image, 
                                              cv2.RETR_TREE, 
                                               cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours, image_name):
    index = -1 #means all contours
    thickness = 2 #thinkess of the contour line
    color = (255, 0, 255) #color of the contour line
    cv2.drawContours(image, contours, index, color, thickness)
    cv2.imshow(image_name,image)



def main():
   
     # Initializing ros node
    rospy.init_node('camera_node', anonymous=True)    # node name    
    
   # Publishers
    pub_image = rospy.Publisher('/image_raw', Image, queue_size=10)  # send control signals

    # control rate
    rate = rospy.Rate(30)   # run the node at 15H
    pub_img = Image()    

    # main loop
    while not rospy.is_shutdown():

        #image_name = "test_image.jpg"
        pub_img = read_ros_image(cap, True)
        #gray_image= convert_rgb_to_gray(rgb_image,True)
        #binary_image = convert_gray_to_binary(gray_image, True, True)
        #contours = getContours(binary_image)
        #draw_contours(rgb_image, contours,"RGB Contours")

        print('Camera node running ok!')        
        pub_image.publish(pub_img)        
        rate.sleep()

    #cv2.waitKey(5)
    cv2.destroyAllWindows()

#video = int(sys.argv[1])   # webacam
video = eval(input("Digite a porta da sua camera: "))

# Criando a porta de captura de video 
cap = cv2.VideoCapture(video)

if __name__ == '__main__':
    main()
