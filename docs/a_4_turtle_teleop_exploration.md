# Turtle teleop exploration

<!---
Use turtle_teleop_key (Figura 1.5) y el programa pysubpose.py para conocer las dimensiones del
plano donde el Turtlesim puede moverse.
-->

To know the dimensions of the plane of movement, could be used the command `turtle_teleop_key` and the program `pypubvel.py`. First, its necessary to define a *Workspace* and create a *Package* (in this case, the name of the package is *pruebas*), this package will be saved into the subfolder *src*. The package will be created with the command `catkin_create_pkg pruebas`. Additionally, this command will create a folder in which there will be 2 files:
- `CMakeList.txt`: this file have the instructions, relationship between libraries and packages, etc.
- `package.xml`: is the manifest of the package.

This is an example, of how to create the package *pruebas*:
<p align="center">
  <img align="center" width="500" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/6e6d1fe2-9fca-4f3d-a81a-1b4422ae0a15">
<p/>

After the creation of the package, and setting the files `pypubvel.py` and `pysubpose.py` as an executable flies with `source devel/setup.bash`, could be posible to run these programs using the command `rosrun`.

<p align="center">
  <img align="center" width="500" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/f866e0ff-c74c-4a50-8ba0-aa87e0980259">
<p/>

<p align="center">
  <img align="center" width="500" src="https://github.com/mobile-robotics-unal/intro2ROS/assets/161974694/ce3d8f76-7cfb-4c73-ac25-6de4c663440a">
<p/>


