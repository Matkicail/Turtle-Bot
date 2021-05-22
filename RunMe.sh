rm -f ./build/CMakeCache.txt

catkin_make --pkg turtlebot_interactions --force-cmake
catkin_make
chmod +x *