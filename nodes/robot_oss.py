#!/usr/bin/env python

 

수입  시스템
수입  장미꽃
import actionlib
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler


rospy.init_node('my_python_node')
pub_cmd = rospy.Publisher('cmd_vel',Twist, queue_size = 10)
pub_init = rospy.Publisher('initialpose', PoseWithCovarianceStamped())
client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
print(client.wait_for_server())


def update_init_pose(x, y, theta):
    init_pose = PoseWithCovarianceStamped()
    init_pose.header.frame_id = "map"
    init_pose.header.stamp = rospy.Time.now()
    init_pose.pose.pose.position.x = x
    init_pose.pose.pose.position.y = y
    init_pose.pose.pose.orientation.w = 1.0
    q = quaternion_from_euler(0.0, 0.0, theta)
    init_pose.pose.pose.orientation.x = q[0]
    init_pose.pose.pose.orientation.y = q[1]
    init_pose.pose.pose.orientation.z = q[2]
    init_pose.pose.pose.orientation.w = q[3]
pub_init.publish(init_pose)

 

def send_goal(x, y, theta):
    goal = MoveBaseGoal()
    init_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    quat = quaternion_from_euler(0.0, 0.0, theta)
    goal.target_pose.pose.orientation.x = quat[0]
    goal.target_pose.pose.orientation.y = quat[1]
    goal.target_pose.pose.orientation.z = quat[2]
    goal.target_pose.pose.orientation.w = quat[3]
    client.send_goal(goal)
    wait = client.wait_for_result()

   if not wait:
    print('Error')
  else:
    print(client.get_result())

update_init_pose(0.2, 0.3, 0.4)
update_init_pose(0.2, 0.3, 0.4)
send_goal(0.5,0.5,0.0)
send_goal(0.5,1.0,0.0)
send_goal(-2.0, -0.3, 0.0)

 

rospy.spin()
