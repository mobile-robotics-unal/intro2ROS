# ROS services explained

<!--- 
Describa como usar algún servicio en Python [6]. Luego pruebe el siguiente código ejemplo que se
encarga de dibujar un cuadrado con el turtlesim: (se recomienda usar las instrucciones rosservice list
y rosservice info)
--->

To use a service in Python is necesary to follow the next steps:

1. Service definition:

Service definitions have the porpouse to be a container for the requests and responses. it is necesary to use whenever a service is created or used. For example:

```python
from turtlesim.srv import TeleportAbsolute
turtle1_teleport = rospy.ServiceProxy("turtle1/teleport_absolute", TeleportAbsolute)
```

In this case, we made a Service definition of the service TeleportAbsolute from turtlesim.

2. Service proxies:
Is necesary to create a rospy.ServiceProxy to call a service. Is recomended to use rospy.wait_for_service() to block the code until the service is available. For example:

```python
from turtlesim.srv import TeleportAbsolute
rospy.wait_for_service("turtle1/teleport_absolute")
turtle1_teleport = rospy.ServiceProxy("turtle1/teleport_absolute", TeleportAbsolute)
```
Also, Servies proxies are callable to use the service:


```python
resp1 = turtle1_teleport(4, 10, 0) 
```

In this case, we use turtle1_teleport() to set x=4, y=10 and theta=0.
