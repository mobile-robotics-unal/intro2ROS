# Python code explained
<!--- 
Describa paso a paso que hacen los programas realizados en Python, indique las funciones de ROS
usadas.
-->
In this case, there are two programs in *Python*. Each one have a few characteristics that let subscribe to an specific theme or publish the different states of the robot.

## `pypub.vel` Program
This program let know the current state of the robot, and take read of the data in a frequecy that is set by the user. The main commands that are used in this code are:
- `rospy.Publisher()`: Creates a publisher for a theme with an specific message.
- `rospy.Rate()`: Creates an object which set the rate (in Hz) for a loop. This process could be refered to sleep the loop.
  
First, a publisher on topic `turtle1/cmd_vel`, with a message type *Twist*. After that, the Python program initializes node `pypubvel`. While `rospy` are working, the program creates a message with a random linear velocity `msg.linear.x = random()` and a random angular velocity `msg.random.x = 2*random() - 1`.

Finally, using the following functions the message is saved and published:
- `rospy.loginfo()`: Save the message in the ROS register.
- `pup.publish()`: Publish the message

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
# Publish the message and wait on rate.
pub.publish(msg)
rate.sleep() 
```

## `pysubpose.py` program.
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
