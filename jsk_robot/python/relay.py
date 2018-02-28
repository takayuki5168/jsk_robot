#!/usr/bin/env python
import rospy
from remap_marker_msgs.msg import MarkerArray
from visualization_msgs import msg

def callback(data):
    outdata = msg.MarkerArray()
    for i in range(len(data.markers)):
        outdata.markers.append(data.markers[i])
    pub.publish(outdata)
    
def listener():
    rospy.init_node('relay', anonymous=True)
    rospy.Subscriber("spots_marker_array", MarkerArray, callback)
    rospy.spin()
        
if __name__ == '__main__':
    pub = rospy.Publisher('spots_marker_array_kinetic', msg.MarkerArray, queue_size=10)
    listener()
