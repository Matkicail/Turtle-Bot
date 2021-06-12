Folder "include": contains libraries and blob detection tests
Folder "src": contains ROS nodes

You must run general RunMe, then roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/<YOURNAME>/ros_home/Turtle-Bot/ros_home.yaml

The runs the object tracking.
roslaunch opencv blob_tracking.launch

This uses the tracked objects distance along with the robots coordinates to calculate the estimate of the objects coordinates.
rosrun opencv my_turtle_blob_tracking.py
