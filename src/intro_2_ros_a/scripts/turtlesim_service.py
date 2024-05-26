import rospy 
from turtlesim.srv import TeleportAbsolute 
from std_srvs.srv import Empty 

if __name__ == '__main__': 
    rospy.init_node('turtlesimservice', anonymous=False) 

    rospy.wait_for_service('turtle1/teleport_absolute') 
    turtle1_teleport = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)

    rospy.wait_for_service('clear') 
    clear1 = rospy.ServiceProxy('clear', Empty) 


    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
        
        target_points = rospy.get_param("points", [])
        for point in target_points:
            turtle1_teleport(point[0], point[1], point[2])
            rate.sleep()

    