import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import cv2
import numpy as np
from sensor_msgs.msg import Image, Range
from cv_bridge import CvBridge
from clover import long_callback
from std_msgs.msg import String

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

def navigate_wait(x=0, y=0, z=2, yaw=float('nan'), speed=0.75, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

def range_callback(msg):
    global range1
    range1 = msg.range
    #print('Rangefinder distance:', msg.range)

rospy.Subscriber('rangefinder/range', Range, range_callback)

bridge = CvBridge()

def find_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    #red = cv2.inRange(hsv, (0, 250, 250), (20,255,255))
    #blue = cv2.inRange(hsv, (87, 250, 250), (95,255,255))
    #green = cv2.inRange(hsv, (65, 250, 250), (80,255,255))
    #yellow = cv2.inRange(hsv, (27,250,250), (35,255,255))


    red_lower = np.array([0, 250, 250])
    red_upper = np.array([20,255,255])
    blue_lower = np.array([87, 250, 250])
    blue_upper = np.array([95,255,255])
    green_lower = np.array([50, 250, 250])
    green_upper = np.array([85,255,255])
    yellow_lower = np.array([27,250,250])
    yellow_upper = np.array([35,255,255])

    color = []
    #red
    mask = cv2.inRange(hsv, red_lower, red_upper)
    if cv2.countNonZero(mask) > 0:
         color.append('red')
    
    #green
    mask1 = cv2.inRange(hsv, green_lower, green_upper)
    if cv2.countNonZero(mask1) > 0:
         color.append('green')

    #yellow
    mask2 = cv2.inRange(hsv, yellow_lower, yellow_upper)
    if cv2.countNonZero(mask2) > 0:
         color.append('yellow')

    #blue
    mask3 = cv2.inRange(hsv, blue_lower, blue_upper)
    if cv2.countNonZero(mask3) > 0:
         color.append('blue')

    return color


@long_callback
def image_callback(data):
    img = bridge.imgmsg_to_cv2(data,'bgr8')
    global col
    col=find_color(img)
    
buildings_pub = rospy.Publisher('/buildings', String, queue_size=1)
image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback)

navigate_wait(frame_id = 'body', auto_arm=True)
xd=0
for f in range(0,16):
    while (xd < 10 and f % 2 == 0) or (xd > -1 and f % 2 == 1):
        if 0.7 < range1 < 1.3:
            rospy.sleep(3)
            telemetry = get_telemetry()
            x1 = telemetry.x
            y1 = telemetry.y
            print(x1, y1, col[0])
            x2 = str(x1)
            y2 = str(y1)
            fraza = 'x = ' + x2 +', y = ' + y2 + ', color = ' + col[0]
            buildings_pub.publish(data = fraza)

                     
        if f % 2 == 0:
             xd += 0.7
        else:
             xd -= 0.7
        yd = f*0.7
        navigate_wait(x=xd, y=yd)

navigate_wait(x=0,y=0)
land()


