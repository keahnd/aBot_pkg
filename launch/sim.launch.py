import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_name = 'aBot_pkg'

    robot_state_pub = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(pkg_name), 'launch', 'robot_state_publisher.launch.py')]),
            launch_arguments={'use_sim_time': 'true'}.items())
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]))
    
    spawn_model = Node(package='ros_gz_sim', 
                       executable='create', 
                       arguments=['-topic', 'robot_description', '-name', 'aBot'],
                       output='screen')
    
    return LaunchDescription([
        robot_state_pub,
        gazebo,
        spawn_model
    ])