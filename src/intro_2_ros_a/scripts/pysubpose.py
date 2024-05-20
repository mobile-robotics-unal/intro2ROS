#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

class listener ():

    def __init__(self):
        self.x_min = None
        self.x_max = None
        self.y_min = None
        self.y_max = None
        
        rospy.init_node('pysubpose', anonymous=True)
        rate = rospy.Rate(0.001)

        self.sub = rospy.Subscriber('turtle1/pose', Pose, self.poseMessageReceived)
        rospy.spin()
    
        
    def poseMessageReceived(self,message):
        log_message = f"position ({message.x:.2f} , {message.y:.2f}) direction= + {message.theta:.2f})"
        rospy.loginfo(message)

        rate = rospy.Rate(1)  # 1 Hz

        rate.sleep()

    def corners(self,message):
        if self.x_min is None:
            self.x_min = message.x
            self.x_max = message.x
            self.y_min = message.y
            self.y_max = message.y

        self.x_min = min(message.x,self.x_min)
        self.x_max = max(message.x, self.x_max)
        self.y_min = min(message.y, self.y_min)
        self.y_max = max(message.y, self.y_max)

        corner_min = [round(self.x_min,2),round(self.y_min,2)]
        corner_max = [round(self.x_min,2),round(self.y_min,2)]
        log_message = f" min: ({corner_min,2} , max: {corner_max})"
        rospy.loginfo(log_message)

        rate = rospy.Rate(1)  # 1 Hz
        rate.sleep()


if __name__ == '__main__':
    listener()
