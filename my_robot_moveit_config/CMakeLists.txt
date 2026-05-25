cmake_minimum_required(VERSION 3.8)
project(my_robot_moveit_config)

find_package(ament_cmake REQUIRED)
find_package(ur_description REQUIRED)

# This installs everything in the config/ and launch/ folders to the package share directory
install(DIRECTORY config/
  DESTINATION share/${PROJECT_NAME}/config
)
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)
ament_package()