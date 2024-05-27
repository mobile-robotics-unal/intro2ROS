# TurtleBot 2 

<!---
Realice una investigación acerca del robot TurtleBot2 y su relación con la base Kobuki.
-->

TurtleBot 2 is the world’s most popular low cost, open source robot for education and research. This second generation personal robot is equipped with a powerful Kobuki robot base, a dual-core netbook, Orbbec Astra Pro Sensor and a gyroscope. All components have been seamlessly integrated to deliver an out-of-the-box development platform. Tap into the thriving open source ROS developer community and get started learning robotics on day one.

> [!NOTE]
> Taken from [Open Source Robotics Fundation, 2024](https://www.turtlebot.com/turtlebot2/)

# Kobuki Base

Kobuki is an mobile base for open-source research and development purposes. It can be used to quickly and cheaply build research platforms and also provides access to other open source software, including ROS. The result is a product that can very easily utilise existing 3D sensing technologies and navigation algorithms to develop applications for research.

![kobuki](https://github.com/mobile-robotics-unal/intro2ROS/assets/49196698/12c16e19-a4ec-4d62-bd88-4de127ee0b92)

# Tech Specs kobuki

## Size and Weight
- Dimensions: 354x354x420 mm
- Weight: 6,3 kg
- Max Payload: 5 kg


  ![top](https://github.com/mobile-robotics-unal/intro2ROS/assets/49196698/fc0eb83a-ecdc-4053-b197-0f6d089dfd77)

## Speed and performance
- Max Speed: 0,65 m/s
- Obstacle clearance: 15 mm
- Drivers and apis: ROS


  ![front](https://github.com/mobile-robotics-unal/intro2ROS/assets/49196698/0ba3a79d-b0c5-4262-a417-c7c6e60dcf46)

## Funcional Specification

Maximum translational velocity: 70 cm/s
Maximum rotational velocity: 180 deg/s (>110 deg/s gyro performance will degrade)
Payload: 5 kg (hard floor), 4 kg (carpet)
Cliff: will not drive off a cliff with a depth greater than 5cm
Threshold Climbing: climbs thresholds of 12 mm or lower
Rug Climbing: climbs rugs of 12 mm or lower
Expected Operating Time: 3/7 hours (small/large battery)
Expected Charging Time: 1.5/2.6 hours (small/large battery)
Docking: within a 2mx5m area in front of the docking station

## Hardware Specification

PC Connection: USB or via RX/TX pins on the parallel port
Motor Overload Detection: disables power on detecting high current (>3A)
Odometry: 52 ticks/enc rev, 2578.33 ticks/wheel rev, 11.7 ticks/mm
Gyro: factory calibrated, 1 axis (110 deg/s)
Bumpers: left, center, right
Cliff sensors: left, center, right
Wheel drop sensor: left, right
Power connectors: 5V/1A, 12V/1.5A, 12V/5A
Expansion pins: 3.3V/1A, 5V/1A, 4 x analog in, 4 x digital in, 4 x digital out
Audio : several programmable beep sequences
Programmable LED: 2 x two-coloured LED
State LED: 1 x two coloured LED [Green - high, Orange - low, Green & Blinking - charging]
Buttons: 3 x touch buttons
Battery: Lithium-Ion, 14.8V, 2200 mAh (4S1P - small), 4400 mAh (4S2P - large)
Firmware upgradeable: via usb
Sensor Data Rate: 50Hz
Recharging Adapter: Input: 100-240V AC, 50/60Hz, 1.5A max; Output: 19V DC, 3.16A
Netbook recharging connector (only enabled when robot is recharging): 19V/2.1A DC
Docking IR Receiver: left, centre, right
Diameter : 351.5mm / Height : 124.8mm / Weight : 2.35kg (4S1P - small)

# References

1. <https://www.turtlebot.com/turtlebot2/>
2. <https://robosavvy.co.uk/kobuki-ymr-k01-w1-turtlebot-2-base.html>
