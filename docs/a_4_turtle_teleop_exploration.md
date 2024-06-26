# Turtle teleop exploration

<!---
Use turtle_teleop_key (Figura 1.5) y el programa pysubpose.py para conocer las dimensiones del
plano donde el Turtlesim puede moverse.
-->

To know the dimensions of the plane of movement,  the command `turtle_teleop_key` and the program `pypubvel.py` can be used. First, its necessary to define a *Workspace* and create a *Package* (in this case, the name of the package is *pruebas*), this package will be saved into the subfolder *src*. The package will be created with the command `catkin_create_pkg intro_2_ros_a`. This command will create a folder in which there will be 2 files:

- `CMakeList.txt`: this file have the instructions, relationship between libraries and packages, etc.
- `package.xml`: is the manifest of the package.

This is an example, of how to create the package *pruebas*:
<p align="center">
  <img align="center" width="500" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/6e6d1fe2-9fca-4f3d-a81a-1b4422ae0a15">
<p/>

After the creation of the package, and setting the files `pypubvel.py` and `pysubpose.py` as an executable files with `source devel/setup.bash`, could be posible to run these programs using the command `rosrun`.

<p align="center">
  <img align="center" width="500" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/f866e0ff-c74c-4a50-8ba0-aa87e0980259">
<p/>

Now, we follow the next set of instructions (in different terminals):

1. Run the *Master*: `roscore`
2. In another terminal, we create a new node: `rosrun turtlesim turtlesim_node`
3. In the last terminal we write rosrun turtlesim `turtle_teleop_key` to control the turtle with the keyboard.
4. Run the `pysubpose.py` program.

<p align="center">
  <img align="center" width="500" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/ce3d8f76-7cfb-4c73-ac25-6de4c663440a">
<p/>
Now using the keyboard, we move the turtle around the workplane to know its dimensions, specifically to the corners of the space.
  
- Corner 1; $x=11.1028$, $y=-0.028803$ 
<p align="center">
  <img align="center" width="600" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/922b83ac-4a71-4303-a364-6f2c2f931892">
<p/>
  
- Corner 2; $x=-0.0214$, $y=-0.023777$ 
<p align="center">
  <img align="center" width="600" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/ccc17b15-b98e-4769-9d1f-0bdab3ceef4a">
<p/>
  
- Corner 3; $x=-0.0083$, $y=11.119777$ 
<p align="center">
  <img align="center" width="600" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/e954bf63-010c-4e51-9c42-6b4d7297cff8">
<p/>
  
- Corner 4; $x=11.1077$, $y=11.114716$ 
<p align="center">
  <img align="center" width="600" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/a77d23a8-8dc4-4d12-ae20-e42c436ce098">
<p/>

The figure is a quadrilateral with approximately dimensions $11.1291 \times 11.14858$ [square units].
