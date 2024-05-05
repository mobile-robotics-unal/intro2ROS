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


