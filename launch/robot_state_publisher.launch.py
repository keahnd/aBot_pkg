import xacro
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command

def generate_launch_description():
    enable_sim_time = LaunchConfiguration('use_sim_time')
    enable_ros2_control = LaunchConfiguration('use_ros2_control')

    pkg_path = os.path.join(get_package_share_directory('aBot_pkg'))
    urdf_path = os.path.join(pkg_path, 'desc', 'robot.urdf.xacro')

    # robot_description_raw = xacro.process_file(urdf_path).toxml()
    robot_description = Command(['xacro ', urdf_path, ' use_ros2_control:=', enable_ros2_control, ' sim_mode:=', enable_sim_time])

    node_robot_state_publisher = Node(package='robot_state_publisher',
                                      executable='robot_state_publisher',
                                      output='screen',
                                      parameters=[{'robot_description': robot_description,
                                                   'use_sim_time': enable_sim_time}])
    
    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false'),
        DeclareLaunchArgument('use_ros2_control', default_value='false'),
        node_robot_state_publisher])