#!/usr/bin/env python 1

import rospy
from geometry_msgs.msg import Twist 
from random import random 

if __name__ == '__main__': 
    # Create a publisher on topic turtle1/cmd_vel, type geometry_msgs/Twist 
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1000) 
    rospy.init_node('pypubvel', anonymous=False) 

    rate = rospy.Rate(2) 

    # Similar to while(ros::ok())
    while not rospy.is_shutdown(): 
        # Create and populate new Twist message
        msg = Twist() 
        msg.linear.x = random() 
        msg.angular.z = 2*random() - 1 

        # Similar to ROS_INFO_STREAM macro, log information.

        log_message =f"Sending random velocity command: linear={msg.linear.x} angular= {msg.angular.z})"
        rospy.loginfo(log_message)

        # Publish the message and wait on rate.
        pub.publish(msg) 
        rate.sleep()