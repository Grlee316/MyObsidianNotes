
Need to install colcon clean
sudo apt install python3-colcon-clean

ROS 2 build package
ros2 pkg create --build-type ament_cmake cpp_pubsub

![[Pasted image 20231003200856.png]]

How to make C package
ros2 pkg create --build-type ament_cmake <package_name>

how to make python package
ros2 pkg create --build-type ament_python <package_name>

use the package
ros2 run my_package my_node

customize package.xml
![[Pasted image 20231003201449.png]]


## **Installing XACRO**
sudo apt install ros-humble-xacro

