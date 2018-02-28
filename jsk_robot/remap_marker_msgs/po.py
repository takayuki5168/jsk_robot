#!/usr/bin/env python

from geometry_msgs.msg import Pose

data1 = Pose()
data1.position.x = 1
data1.position.y = 2
data1.position.y = 3
data1.orientation.x = 10
data1.orientation.y = 20
data1.orientation.y = 30

data2 = Pose()


for slot in data1.__slots__:
    setattr(type(data2), slot, getattr(data1, slot))

print('data1')
print(data1)
print('data2')
print(data2)
