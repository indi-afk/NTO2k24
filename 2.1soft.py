import random
import xml.etree.ElementTree as ET

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



root = ET.Element("Root")           #created file.xml with coordinates
x1_xml = ET.SubElement(root,"x1")
y1_xml = ET.SubElement(root,"y1")
x2_xml = ET.SubElement(root,"x2")
y2_xml = ET.SubElement(root,"y2")
x3_xml = ET.SubElement(root,"x3")
y3_xml = ET.SubElement(root,"y3")
x4_xml = ET.SubElement(root,"x4")
y4_xml = ET.SubElement(root,"y4")
x5_xml = ET.SubElement(root,"x5")
y5_xml = ET.SubElement(root,"y5")

tree = ET.ElementTree(root)
tree.write("coordinates.xml", encoding = "utf-8", xml_declaration=True)


tree1 = ET.parse('coordinates.xml')
root1 = tree1.getroot()

tree2 = ET.parse('gg.xml')
root2 = tree2.getroot()

new_root = ET.Element("root")

new_root = ET.append(root1)
new_root = ET.append(root2)

new_tree = ET.ElementTree(new_root)
new_tree.write('gg_with_coordinates', encoding = 'utf-8', xml_declaration = True)  #file.xml with coordinates and include models


tree3 = ET.parse('gg_with_coordinates.xml')
root3 = tree3.getroot()

tree4 = ET.parse('clover_aruco.world')
root4 = tree4.getroot()

root4.find('world')
root4.append(root3)

tree4.write('clover_aruco11.world', encoding='utf-8', xml_declaration=True)

tree5 = ET.parse('catkin_ws/src/clover/clover_simulation/launch/simulator.launch')
root5 = tree5.getroot()

position = 13
arg5 = root5[position]
arg5.set('value', 'clover_aruco11.world')

tree1.write('catkin_ws/src/clover/clover_simulation/launch/simulator.launch')
