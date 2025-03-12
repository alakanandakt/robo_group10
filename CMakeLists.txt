cmake_minimum_required(VERSION 3.0.2)
project(my_bot)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Compiler flags for GCC or Clang
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS
  # Add your package dependencies here, e.g.
  # roscpp
  # rospy
  # std_msgs
)

# Uncomment to add any other dependencies manually
# find_package(<dependency> REQUIRED)

# Declare a catkin package
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES my_bot
  CATKIN_DEPENDS roscpp std_msgs # List dependencies here
  DEPENDS system_lib
)

# Include directories
include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Add executable and link libraries
add_executable(my_bot_node src/my_bot_node.cpp)

# Link the executable with the necessary libraries
target_link_libraries(my_bot_node
  ${catkin_LIBRARIES}
)

# Install targets
install(TARGETS my_bot_node
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY config launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# If you have other resources like worlds, add them here
# install(DIRECTORY worlds DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/worlds)
