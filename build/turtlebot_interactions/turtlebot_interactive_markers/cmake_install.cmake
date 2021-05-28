# Install script for directory: /home/matthew/ros_home/Turtle-Bot/Turtle-Bot/src/turtlebot_interactions/turtlebot_interactive_markers

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/matthew/ros_home/Turtle-Bot/Turtle-Bot/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/matthew/ros_home/Turtle-Bot/Turtle-Bot/build/turtlebot_interactions/turtlebot_interactive_markers/catkin_generated/installspace/turtlebot_interactive_markers.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot_interactive_markers/cmake" TYPE FILE FILES
    "/home/matthew/ros_home/Turtle-Bot/Turtle-Bot/build/turtlebot_interactions/turtlebot_interactive_markers/catkin_generated/installspace/turtlebot_interactive_markersConfig.cmake"
    "/home/matthew/ros_home/Turtle-Bot/Turtle-Bot/build/turtlebot_interactions/turtlebot_interactive_markers/catkin_generated/installspace/turtlebot_interactive_markersConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot_interactive_markers" TYPE FILE FILES "/home/matthew/ros_home/Turtle-Bot/Turtle-Bot/src/turtlebot_interactions/turtlebot_interactive_markers/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot_interactive_markers" TYPE EXECUTABLE FILES "/home/matthew/ros_home/Turtle-Bot/Turtle-Bot/build/turtlebot_interactions/turtlebot_interactive_markers/CMakeFiles/CMakeRelink.dir/turtlebot_marker_server")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot_interactive_markers" TYPE DIRECTORY FILES "/home/matthew/ros_home/Turtle-Bot/Turtle-Bot/src/turtlebot_interactions/turtlebot_interactive_markers/launch")
endif()

