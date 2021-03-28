# Install script for directory: /home/ros_ws/src/moveit/moveit_ros/planning_interface/py_bindings_tools

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ros_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
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

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so.1.1.1" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so.1.1.1")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so.1.1.1"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ros_ws/devel/.private/moveit_ros_planning_interface/lib/libmoveit_py_bindings_tools.so.1.1.1")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so.1.1.1" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so.1.1.1")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so.1.1.1"
         OLD_RPATH "/home/ros_ws/devel/.private/moveit_ros_warehouse/lib:/opt/ros/noetic/lib:/home/ros_ws/devel/.private/moveit_ros_manipulation/lib:/home/ros_ws/devel/.private/moveit_ros_move_group/lib:/home/ros_ws/devel/.private/moveit_ros_planning/lib:/home/ros_ws/devel/.private/moveit_ros_occupancy_map_monitor/lib:/home/ros_ws/devel/.private/moveit_core/lib:/opt/ros/noetic/lib/x86_64-linux-gnu:/home/ros_ws/devel/.private/geometric_shapes/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so.1.1.1")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/ros_ws/devel/.private/moveit_ros_planning_interface/lib/libmoveit_py_bindings_tools.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so"
         OLD_RPATH "/home/ros_ws/devel/.private/moveit_ros_warehouse/lib:/opt/ros/noetic/lib:/home/ros_ws/devel/.private/moveit_ros_manipulation/lib:/home/ros_ws/devel/.private/moveit_ros_move_group/lib:/home/ros_ws/devel/.private/moveit_ros_planning/lib:/home/ros_ws/devel/.private/moveit_ros_occupancy_map_monitor/lib:/home/ros_ws/devel/.private/moveit_core/lib:/opt/ros/noetic/lib/x86_64-linux-gnu:/home/ros_ws/devel/.private/geometric_shapes/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libmoveit_py_bindings_tools.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so.1.1.1" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so.1.1.1")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so.1.1.1"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface" TYPE SHARED_LIBRARY FILES "/home/ros_ws/devel/.private/moveit_ros_planning_interface/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so.1.1.1")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so.1.1.1" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so.1.1.1")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so.1.1.1"
         OLD_RPATH "/home/ros_ws/devel/.private/moveit_ros_planning_interface/lib:/home/ros_ws/devel/.private/moveit_ros_warehouse/lib:/opt/ros/noetic/lib:/home/ros_ws/devel/.private/moveit_ros_manipulation/lib:/home/ros_ws/devel/.private/moveit_ros_move_group/lib:/home/ros_ws/devel/.private/moveit_ros_planning/lib:/home/ros_ws/devel/.private/moveit_ros_occupancy_map_monitor/lib:/home/ros_ws/devel/.private/moveit_core/lib:/opt/ros/noetic/lib/x86_64-linux-gnu:/home/ros_ws/devel/.private/geometric_shapes/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so.1.1.1")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface" TYPE SHARED_LIBRARY FILES "/home/ros_ws/devel/.private/moveit_ros_planning_interface/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so"
         OLD_RPATH "/home/ros_ws/devel/.private/moveit_ros_planning_interface/lib:/home/ros_ws/devel/.private/moveit_ros_warehouse/lib:/opt/ros/noetic/lib:/home/ros_ws/devel/.private/moveit_ros_manipulation/lib:/home/ros_ws/devel/.private/moveit_ros_move_group/lib:/home/ros_ws/devel/.private/moveit_ros_planning/lib:/home/ros_ws/devel/.private/moveit_ros_occupancy_map_monitor/lib:/home/ros_ws/devel/.private/moveit_core/lib:/opt/ros/noetic/lib/x86_64-linux-gnu:/home/ros_ws/devel/.private/geometric_shapes/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/moveit_ros_planning_interface/_moveit_roscpp_initializer.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/ros_ws/src/moveit/moveit_ros/planning_interface/py_bindings_tools/include/")
endif()

