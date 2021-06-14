Folder "include": contains libraries and blob detection tests
Folder "src": contains ROS nodes

You must run general RunMe, then roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/<YOURNAME>/ros_home/Turtle-Bot/ros_home.yaml

The runs the object tracking.
roslaunch opencv blob_tracking.launch

This uses the tracked objects distance along with the robots coordinates to calculate the estimate of the objects coordinates.
rosrun opencv my_turtle_blob_tracking.py

To see from the robots camera, you use rosrun rqt_image_view rqt_image_view



To choose a different object to look for, you must first be in
/Turtle-Bot/src/opencv/include
Then open the robots camera, look above. Find an object and save the image into /Turtle-Bot/src/opencv/include
Then you open this
python range_detector.py --image yourimage.png --filter HSV
Play around with the sliders until only the object is in the image.
Go to find_ball.py and under main change blue_min and blue_max to the min HSV and max HSV slider values you were just playing around with.
You should be done then.