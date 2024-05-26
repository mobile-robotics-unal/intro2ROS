# ROS services explained

<!--- 
Describa como usar algún servicio en Python [6]. Luego pruebe el siguiente código ejemplo que se
encarga de dibujar un cuadrado con el turtlesim: (se recomienda usar las instrucciones rosservice list
y rosservice info)
--->

To use a service in Python is necesary to follow the next steps:

1. Select ROS Service:

ROS services are defined as srv files that rospy converts to py filest, that contains the request and response schemas. In this case we will use the service `turtle1/teleport_absolute`.

2. Service proxies:
Is necesary to create a rospy.ServiceProxy to call a service. Is recomended to use `rospy.wait_for_service()` to block the code until the service is available. For example:

```python
from turtlesim.srv import TeleportAbsolute
rospy.wait_for_service("turtle1/teleport_absolute")
turtle1_teleport = rospy.ServiceProxy("turtle1/teleport_absolute", TeleportAbsolute)
```

3. Calling Services

Servies proxies are callable to use the service. Each service could have multiple argumments. In this case, we use `turtle1_teleport()` to set $x=4$, $y=10$ and $\theta=0$:

```python
resp1 = turtle1_teleport(4, 10, 0) 
```

## Draw a square with turtlesim

With the teletransport service we can move the turtle to a define set of coordinates to draw a square. We save the coordinates in a yaml and then we can pass them as a parameter. The code can be found in the file [turtlesim_service](../src/intro_2_ros_a/scripts/turtlesim_service.py). We then us a roslaunch to call the service. 
```xml
<launch>
    <!-- Start the master node 
    <node pkg="turtlesim" type="turtlesim_node " name="turtlesim_node"/>

    <node pkg="turtesim" type="turtle_teleop_key" name="turtle_teleop_key"/>
  
   -->
    <rosparam command="load" file="$(find intro_2_ros_a)/config/square.yaml" />

    <node pkg="turtlesim" name="turtle_node" type="turtlesim_node"/>
    <node pkg="intro_2_ros_a" name="draw_service_caller" type="turtlesim_service.py" />
    <rosparam command="load" file="$(find intro_2_ros_a)/config/square.yaml" />
    

    
    <group ns="pepita">
   
        <rosparam command="load" file="$(find intro_2_ros_a)/config/triangle.yaml" />
        <node pkg="turtlesim" name="turtle_node" type="turtlesim_node"/>
        <node pkg="rosservice" name="spawner" type="rosservice" args="call /spawn 5.0 3.0 0.0 'pepita/turtle1'" />
        <node pkg="intro_2_ros_a" name="draw_service_caller" type="turtlesim_service.py" />
    </group>

</launch>
```

With [this roslaunch](../src/intro_2_ros_a/launch/draw.launch) we call a turtle sim node and then we call the service  call the service to spawn a second turtle we call "pepita" and call the parameters to set different trajectories for each turtle to draw a square and a triangle. Resulting in the following image:


![imagen](https://github.com/mobile-robotics-unal/intro2ROS/assets/25491198/5838a0e8-1cbb-411b-aec2-d69b762df28b)