# Basic ROS commands
<!---
2. Investigue sobre qué comandos se pueden usar con rosnode, rostopic, rosservice,rosmsg, rospack [4].
-->

## Rosnode

- `rosnode ping`: Probe the connectivity of a node.
- `rosnode list`: Shows a list of active nodes.
- `rosnode info`: Print the information of an specific node.
- `rosnode machine`: Gives the list of the active nodes int the machine.
- `rosnode kill`: Ends a process of an active node.

## Rostopic

- `rostopic bw`: Shows the bandwith used per topic.
- `rostopic echo`: Prints a message in the screen.
- `rostopic find`: Search a topic for a theme.
- `rostopic hz`: Let know information about the publish rate of a theme.
- `rostopic info`: Shows information of an active theme.
- `rostopic list`: Shows a list of published themes.
- `rostopic pub`: Publish information about a theme.
- `rostopic type`: Prints the type of theme.

## rosservice

- `rosservice list`: Prints information of an active service.
- `rosservice node`: Imprime el nombre del nodo proveniente de un servicio Prints the node's name comming from a service.
- `rosservice call`: Llama el servicio con los argumentos dados Calls the service.
- `rosservice args`: List of arguments of a service.
- `rosservice type`: Prints the type of service.
- `rosservice uri`: Prints the ROSRPC uri service.
- `rosservice find`: Find a service by its type.

## rosmsg

- `rosmsg show`: Shows the fields on msg/srv.
- `rosmsg list`: Shows the names of all msg/srv.
- `rosmsg md5`: Let know msg/srv md5 sum.
- `rosmsg package`: Gives the list of all msg/srv in a package.
- `rosmsg packages`: List of all the packages with an specific msg/srv

## rospack

- `rospack`: Search and do a backup of a package.
- `catkin_create_pkg`: Creates a new package.
- `catkin_make`: Creates a new workspace for a package.
- `rosdep`: Installs all system dependencies of a package.
- `rqt`: Shows all depedencies of a package as a graph.
