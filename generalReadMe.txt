========================
FOR OUR PURPOSES 
========================
run this file from a singularity terminal
note to run this just type "roslaunch turtlebot_teleop keyboard_teleop.launch"

------------------------


In a terminals: STRUCTURE IS CODE :: WHAT DOES
./startWorld :: STARTS THE WORLD
roslaunch turtlebot_gazebo gmapping_demo.launch :: get the gmapping to run
rosrun rviz rviz :: See the robots point of view
roslaunch turtlebot_teleop keyboard_teleop.launch :: Makes a controler (manual)

FURTHER NOTES:
in rviz, add a map, put the topic of the map to /map
in rviz, add the robot model to see it move.

Jono:
roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/jaredl/ros_home/Turtle-Bot/ros_home.yaml
roslaunch turtlebot_rviz_launchers view_navigation.launch
