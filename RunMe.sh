rm -f ./build/CMakeCache.txt
rm -f ./src/CMakeCache.txt
rm -f ./src/CMakeLists.txt



catkin_make --force-cmake
catkin_make
chmod +x *