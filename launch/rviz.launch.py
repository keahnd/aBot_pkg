import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
	pkg_name = 'aBot_pkg'
	my_pkg_path = get_package_share_directory(pkg_name)
	rviz_config_path = os.path.join(my_pkg_path, 'config', 'aBot_rviz.rviz')


	rviz2_node = Node(package='rviz2', 
					executable='rviz2', 
					arguments=['-d', rviz_config_path],
					parameters=[{'use_sim_time': True}],
					output='screen')

	return LaunchDescription([
		rviz2_node,
	])