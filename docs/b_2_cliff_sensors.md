# Cliff sensor
<!--

2. ¿Para que sirve los sensores cliff en el Kobuki?¿Como leer un evento de dicho sensor?
-->

Cliff sensors, in the context of the Kobuki base, are important safety sensors that detect edges or drops to prevent the robot from falling off elevated surfaces.

## How cliff sensor works
- Technology: Typically use infrared (IR) light to detect the distance to the ground. They emit an IR beam and measure the time it takes to reflect back. If the distance is larger than expected (indicating an edge or drop), the sensor detects a "cliff".
- Placement: These sensors are located on the underside of the robot, around the perimeter, to provide full coverage. The Kobuki base usually has several cliff sensors at the front and rear.

## Publish Cliff Sensor Data in ROS

The Kobuki base publishes various sensor data, including cliff sensor information, to ROS topics. To access and visualize this data, you can use the rostopic tool.

1. Launch the TurtleBot 2/Kobuki Base: Ensure that your TurtleBot 2 is properly set up and that the ROS master node is running. You typically launch the robot's software stack using a launch file.
   
````
roslaunch kobuki minimal.launch
````
