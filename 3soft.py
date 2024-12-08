import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from clover import long_callback

rospy.init_node('flight')


get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

def navigate_wait(x=0, y=0, z=0, yaw=float('nan'), speed=0.7, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

def find_dronepoints(image, lower_color, upper_color):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    squares = []
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
    
        if len(approx) == 4:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                squares.append(((cX, cY), approx))
    return squares

all_squares = []

color_ranges = {
    "red": (np.array([0, 100, 100]), np.array([10,255,255])),
    "green": (np.array([40, 100, 100]), np.array([80,255,255])),
    "blue": (np.array([100, 100, 100]), np.array([140,255,255])),
    "yellow": (np.array([20, 100, 100]), np.array([30,255,255])),
}

bridge = CvBridge()

@long_callback
def image_callback(data):
    #global img
    img = bridge.imgmsg_to_cv2(data,'bgr8')
    for color_name, (lower_color, upper_color) in color_ranges.items():
       squares =  find_dronepoints(img,lower_color, upper_color)
       for center, contour in squares:
           all_squares.append((center, color_name))
           cv2.drawContours(img, [contour], -1, (199, 21, 133), 3)
           cv2.circle(img, center, 5 ,(127,255,212), -1)
    
    
#image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback)
    
navigate_wait(x=0, y=0, z=2, frame_id = 'body', auto_arm = True)
xd=0
yd=0
while xd<10 or :      #pridumatb
    xd+=1
    navigate_wait(x=xd, z=2)
