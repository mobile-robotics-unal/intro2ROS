# Turtle teleop exploration

<!---
Use turtle_teleop_key (Figura 1.5) y el programa pysubpose.py para conocer las dimensiones del
plano donde el Turtlesim puede moverse.
-->
First, to program with ROS, its necessary to define a "Workspace" and create a "Package".  The "Workspace" is a folder where the new packages will be stored, in this folder we create a new folder with the name *src*. In the *src* folder, the *source codes* of all the packages will be stored.

```python
#!/usr/bin/env python 
import rospy 
from geometry_msgs.msg import Twist 
from random import random 

if __name__ == ’__main__’: 
  # Create a publisher on topic turtle1/cmd_vel, type geometry_msgs/Twist 
  pub = rospy.Publisher(’turtle1/cmd_vel’, Twist, queue_size=1000) 
  rospy.init_node(’pypubvel’, anonymous=False) 

  rate = rospy.Rate(2) 

  # Similar to while(ros::ok()) 
  while not rospy.is_shutdown(): 
    # Create and populate new Twist message 
    msg = Twist() 
    msg.linear.x = random() 
    msg.angular.z = 2*random() - 1 

# Similar to ROS_INFO_STREAM macro, log information. 
rospy.loginfo(’Sending random velocity command:’ + ’ linear=’ + str(msg.linear.x) + ’ angular=’ + str(msg.angular.z)) 
# Publish the message and wait on rate. 25
pub.publish(msg) 26
rate.sleep() 
```
```python
#!/usr/bin/env python

import rospy

from turtlesim.msg import Pose
def poseMessageReceived(message):rospy.loginfo(’position=(’ + str(message.x) + ’,’ + str(message.y) +’)’ + ’ direction=’ + str(message.theta))

if __name__ == ’__main__’:
	rospy.init_node(’pysubpose’, anonymous=False)
	sub = rospy.Subscriber(’turtle1/pose’, Pose, poseMessageReceived)
	
rospy.spin
```
