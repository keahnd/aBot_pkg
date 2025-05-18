import xacro
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
    pkg_path = os.path.join(get_package_share_directory('aBot_pkg'))
    urdf_path = os.path.join(pkg_path, 'desc', 'robot.urdf.xacro')

    robot_description_raw = xacro.process_file(urdf_path).toxml()

    node_robot_state_publisher = Node(package='robot_state_publisher',
                                      executable='robot_state_publisher',
                                      output='screen',
                                      parameters=[{'robot_description': robot_description_raw}])
    
    return LaunchDescription([node_robot_state_publisher])