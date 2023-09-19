
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main"> /etc/apt/sources.list.d/ros-latest.list'


This worked:
https://answers.ros.org/question/410123/ubuntu-2204-ros2-humble-installing-error-gpg-libc-bin/

https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

Turtlesim:
https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html



hand of a humanoid robot
wrist
elbow
leg shoulder
Ros can be run regardless of the type of the operating systems

source /opt/ros/humble/setup.bash
rqt
rqt_graph
ros2 node
ros2 node list
ros2 node info /turtlesim
ros2 topic
ros2 topic list



ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0" -

ros2 topic pub -r 10 /turtle1/cmd_vel geometry_msgs/msg/Twist "linear:

ros2 service call /spawn turtlesim/srv/Spawn "{x: 2,y: 2,theta: 0.0, name: ''}"

ros2 bag

ros2 bag record -a -o cmd_record


