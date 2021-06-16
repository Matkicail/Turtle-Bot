Matthew Kruger 1669326
Jared Harris-Dewey 1846346
Bo-Yan Wu 1888261
Michael-John Brewer 1851234

========================
For Submission
========================
Make sure to catkin_make. We have a RunMe.sh that removes cache files if needed.

You'll need to open 7 consoles and source/devel.setup.bash each one

Steps:
1) ./startWorld to launch

2) You will need to change the ros_home.yaml pointing location to your directory.
   You can enter the command below after replacing <NAME>
   roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/<NAME>/ros_home/Turtle-Bot/ros_home.yaml

3) You can enter the following to view the map and navigation:
   roslaunch turtlebot_rviz_launchers view_navigation.launch


4) To patrol you can enter:
   rosrun turtlebot_source go_to_specific_point_on_map.py

5) To get object tracking working, enter the two lines:
   roslaunch opencv blob_tracking.launch
   rosrun opencv my_turtle_blob_tracking.py

6) To get a video feed of object tracking enter:
   rqt_image_view rqt_image_view

   You will need to set the image to /blob/image_blob


========================
FOR OUR PURPOSES 
========================
Teleop:
note to run this just type "roslaunch turtlebot_teleop keyboard_teleop.launch"


In a terminals: STRUCTURE IS CODE :: WHAT DOES
./startWorld :: STARTS THE WORLD
roslaunch turtlebot_gazebo gmapping_demo.launch :: get the gmapping to run
rosrun rviz rviz :: See the robots point of view
roslaunch turtlebot_teleop keyboard_teleop.launch :: Makes a controler (manual)

FURTHER NOTES:
in rviz, add a map, put the topic of the map to /map
in rviz, add the robot model to see it move.