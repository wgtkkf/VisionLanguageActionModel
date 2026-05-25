from launch import LaunchDescription
from launch_ros.substitutions import FindPackageShare

from launch.substitutions import Command, PathJoinSubstitution

from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_dir = get_package_share_directory('my_robot_moveit_config')
    ur_description_dir = FindPackageShare('ur_description')
    
    # Path to the generic UR xacro
    #urdf_xacro_path = PathJoinSubstitution([ur_description_dir, 'urdf', 'ur.urdf.xacro'])
    urdf_xacro_path = os.path.join(package_dir, 'config', 'my_robot.urdf.xacro')

    # Robot Description
    robot_description_content = Command([
        'xacro ', urdf_xacro_path,
        ' ur_type:=ur5e',
        ' name:=ur5e',
        ' prefix:=""',
        ' safety_limits:=false',
        ' safety_pos_margin:=0.15',
        ' safety_k_position:=20',
        ' kinematics_params:=', PathJoinSubstitution([ur_description_dir, 'config', 'ur5e', 'default_kinematics.yaml']),
        ' joint_limit_params:=', PathJoinSubstitution([ur_description_dir, 'config', 'ur5e', 'joint_limits.yaml']),
        ' physical_params:=', PathJoinSubstitution([ur_description_dir, 'config', 'ur5e', 'physical_parameters.yaml']),
        ' visual_params:=', PathJoinSubstitution([ur_description_dir, 'config', 'ur5e', 'visual_parameters.yaml'])
    ])
    
    srdf_path = os.path.join(package_dir, 'config', 'ur5e_with_gripper.srdf')
    controllers_yaml = os.path.join(package_dir, 'config', 'moveit_controllers.yaml')

    return LaunchDescription([
        # 1. Broadcaster
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description_content}]
        ),
        # 2. Joint State Provider
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        # 3. The Brain (MoveGroup)
        Node(
            package='moveit_ros_move_group',
            executable='move_group',
            parameters=[
                {'robot_description': robot_description_content},
                {'robot_description_semantic': Command(['cat ', srdf_path])},
                controllers_yaml  # <--- CRITICAL: Loads the controller definitions
            ]
        ),
        # 4. The Eyes
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', os.path.join(package_dir, 'launch', 'moveit.rviz')]
        )
    ])