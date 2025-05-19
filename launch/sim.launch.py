import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ros_gz_bridge.actions import RosGzBridge

def generate_launch_description():
    pkg_name = 'aBot_pkg'
    my_pkg_path = get_package_share_directory(pkg_name)
    bridge_yaml_path = os.path.join(my_pkg_path, 'config', 'ros_gz_bridge')

    robot_state_pub = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(my_pkg_path, 'launch', 'robot_state_publisher.launch.py')]),
            launch_arguments={'use_sim_time': 'true'}.items())
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
        launch_arguments={'gz_args': 'empty.sdf'}.items())
    
    gz_ros_bridge = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('ros_gz_bridge'), 'launch', 'ros_gz_bridge.launch.py')]),
        launch_arguments={'bridge_name': 'ros_gz_bridge', 'config_file': bridge_yaml_path}.items())
    
    spawn_model = Node(package='ros_gz_sim', 
                       executable='create', 
                       arguments=['-topic', 'robot_description', '-name', 'aBot', '-x', '0', '-y', '0', '-z', '0.1'],
                       output='screen')
    
    return LaunchDescription([
        robot_state_pub,
        gazebo,
        spawn_model,
        gz_ros_bridge
    ])