import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import cv2
import numpy as np
from sensor_msgs.msg import Image, Range
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

def navigate_wait(x=0, y=0, z=1.8, yaw=float('nan'), speed=0.5, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
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
    return msg.range

rospy.Subscriber('rangefinder/range', Range, range_callback)

navigate_wait(frame_id = 'body', auto_arm=True)
xd=0
for f in range(0,20):
    while (xd != 9.5 and f % 2 == 0) or (xd != -0.5 and f % 2 == 1):
        if 0.3 < range1 < 0.7:
                rospy.sleep(3)
        if f % 2 == 0:
             xd += 0.5
        else:
             xd -= 0.5
        yd = f*0.5
        navigate_wait(x=xd, y=yd)

navigate_wait(x=0,y=0)
land()
