<launch>
  <!-- Launch argument to use sim time -->
  <arg name="use_sim_time" default="false" doc="Use sim time if true"/>

  <!-- Process the URDF file from the xacro file -->
  <param name="robot_description" command="xacro $(find my_bot)/description/robot.urdf.xacro" />

  <!-- Robot State Publisher node -->
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" output="screen">
    <param name="use_sim_time" value="$(arg use_sim_time)" />
  </node>

</launch>
