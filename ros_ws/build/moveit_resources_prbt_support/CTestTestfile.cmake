# CMake generated Testfile for 
# Source directory: /home/ros_ws/src/moveit_resources/prbt_support
# Build directory: /home/ros_ws/build/moveit_resources_prbt_support
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_moveit_resources_prbt_support_roslint_package "/home/ros_ws/build/moveit_resources_prbt_support/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/ros_ws/build/moveit_resources_prbt_support/test_results/moveit_resources_prbt_support/roslint-moveit_resources_prbt_support.xml" "--working-dir" "/home/ros_ws/build/moveit_resources_prbt_support" "--return-code" "/opt/ros/noetic/share/roslint/cmake/../../../lib/roslint/test_wrapper /home/ros_ws/build/moveit_resources_prbt_support/test_results/moveit_resources_prbt_support/roslint-moveit_resources_prbt_support.xml make roslint_moveit_resources_prbt_support")
set_tests_properties(_ctest_moveit_resources_prbt_support_roslint_package PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/roslint/cmake/roslint-extras.cmake;67;catkin_run_tests_target;/home/ros_ws/src/moveit_resources/prbt_support/CMakeLists.txt;92;roslint_add_test;/home/ros_ws/src/moveit_resources/prbt_support/CMakeLists.txt;0;")
subdirs("gtest")
