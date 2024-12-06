import xml.etree.ElementTree as ET

# clover.launch
tree = ET.parse('catkin_ws/src/clover/clover/launch/clover.launch')
root = tree.getroot()

position = 8
arg = root[position]
arg.set('default', 'true')

tree.write('catkin_ws/src/clover/clover/launch/clover.launch')

# 2 aruco.launch

tree1 = ET.parse('catkin_ws/src/clover/clover/launch/aruco.launch')
root1 = tree1.getroot()

position1 = 1
arg1 = root1[position1]
arg1.set('default', 'true')

tree1.write('catkin_ws/src/clover/clover/launch/aruco.launch')



tree2 = ET.parse('catkin_ws/src/clover/clover/launch/aruco.launch')
root2 = tree2.getroot()

position2= 2
arg2 = root2[position2]
arg2.set('default', 'true')

tree2.write('catkin_ws/src/clover/clover/launch/aruco.launch')


#map cmit.txt

tree3 = ET.parse('catkin_ws/src/clover/clover/launch/aruco.launch')
root3 = tree3.getroot()

position3= 5
arg3 = root3[position3]
arg3.set('default', 'cmit.txt')

tree3.write('catkin_ws/src/clover/clover/launch/aruco.launch')




