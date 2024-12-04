import rospy
import random
from gazebo_msgs.srv import SpawnModel, SetLinkState
from geometry_msgs.msg import Pose, Point, Quaternion
from gazebo_msgs.msg import LinkState

#set_link_state = rospy.ServiceProxy('gazebo/set_link', SetLinkState)

def add_model_to_Gazebo(model_name, model_path, pose):
    rospy.wait_for_service('gazebo/spawn_sdf_model')
    try:
        spawn_model = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        with open(model_path, 'r') as model_file:
            model_xml = model_file.read()
        spawn_model(model_name, model_xml,"", pose, "")
        rospy.loginfo(f"Model  '{model_name}' spawned succesfully!")
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

x1 = random.uniform(0,9)
y1 = random.uniform(0,9)

x2 = random.uniform(0,9)
y2 = random.uniform(0,9)
while ((x1-x2)**2 + (y1-y2)**2)**0.5 < 1:
    x2 = random.uniform(0,9)
    y2 = random.uniform(0,9)

x3 = random.uniform(0,9)
y3 = random.uniform(0,9)
while (((x1-x3)**2 + (y1-y3)**2)**0.5 < 1) or (((x3-x2)**2 + (y3-y2)**2)**0.5 < 1):
    x3 = random.uniform(0,9)
    y3 = random.uniform(0,9)

x4 = random.uniform(0,9)
y4 = random.uniform(0,9)
while (((x1-x4)**2 + (y1-y4)**2)**0.5 < 1) or (((x4-x2)**2 + (y4-y2)**2)**0.5 < 1) or (((x4-x3)**2 + (y4-y3)**2)**0.5 < 1):
    x4 = random.uniform(0,9)
    y4 = random.uniform(0,9)

x5 = random.uniform(0,9)
y5 = random.uniform(0,9)
while (((x1-x5)**2 + (y1-y5)**2)**0.5 < 1) or (((x5-x2)**2 + (y5-y2)**2)**0.5 < 1) or (((x5-x3)**2 + (y5-y3)**2)**0.5 < 1) or (((x5-x4)**2 + (y5-y4)**2)**0.5 < 1):
    x5 = random.uniform(0,9)
    y5 = random.uniform(0,9)


rospy.init_node('model_loader', anonymous=True)

model_name1 = 'blue_model'
model_path1 = '/home/clover/dronepoint/dronepoint_blue/dronepoint_blue.sdf'
pose1 = Pose()
pose1.position.x = x1
pose1.position.y = y1
pose1.position.z = 0
pose1.orientation.w = 1

add_model_to_Gazebo(model_name1, model_path1, pose1)

model_name2 = 'green_model'
model_path2 = '/home/clover/dronepoint/dronepoint_green/dronepoint_green.sdf'
pose2 = Pose()
pose2.position.x = x2
pose2.position.y = y2
pose2.position.z = 0
pose2.orientation.w = 1

add_model_to_Gazebo(model_name2, model_path2, pose2)

model_name3 = 'red_model'
model_path3 = '/home/clover/dronepoint/dronepoint_red/dronepoint_red.sdf'
pose3 = Pose()
pose3.position.x = x3
pose3.position.y = y3
pose3.position.z = 0
pose3.orientation.w = 1

add_model_to_Gazebo(model_name3, model_path3, pose3)

model_name4 = 'yellow_model'
model_path4 = '/home/clover/dronepoint/dronepoint_yellow/dronepoint_yellow.sdf'
pose4 = Pose()
pose4.position.x = x4
pose4.position.y = y4
pose4.position.z = 0
pose4.orientation.w = 1

add_model_to_Gazebo(model_name4, model_path4, pose4)

z = random.randint(0,3+1)
if z == 0:
    model_name5 = 'blue_model'
    model_path5 = '/home/clover/dronepoint/dronepoint_blue/dronepoint_blue.sdf'
if z == 1:
    model_name5 = 'green_model'
    model_path5 = '/home/clover/dronepoint/dronepoint_green/dronepoint_green.sdf'
if z == 2:
    model_name5 = 'red_model'
    model_path5 = '/home/clover/dronepoint/dronepoint_red/dronepoint_red.sdf'
if z == 3:
    model_name5 = 'yellow_model'
    model_path5 = '/home/clover/dronepoint/dronepoint_yellow/dronepoint_yellow.sdf'

pose5 = Pose()
pose5.position.x = x5
pose5.position.y = y5
pose5.position.z = 0
pose5.orientation.w = 1

add_model_to_Gazebo(model_name5, model_path5, pose5)




