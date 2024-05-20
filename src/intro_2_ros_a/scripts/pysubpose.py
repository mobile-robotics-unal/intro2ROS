#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def poseMessageReceived(message):rospy.loginfo(f"position=({message.x} , {message.y}) direction= + {message.theta})")

if __name__ == '__main__':
    rospy.init_node('pysubpose', anonymous=False)
    sub = rospy.Subscriber('turtle1/pose', Pose, poseMessageReceived)

rospy.spin