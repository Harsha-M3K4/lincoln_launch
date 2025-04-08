from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    dbw2_bridge = Node(
        package="transform_dbw2_bridge",
        executable="lincoln_dbw"
    )

    ld.add_action(dbw2_bridge)

    return ld