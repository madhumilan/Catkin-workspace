#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class MoveRobot:
	def __init__(self):
		self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
		self.move_msg = Twist()

	def send_cmd(self, linear=0, angular=0):
		self.move_msg.linear.x = linear
		self.move_msg.linear.y = angular
		self.pub.publish(self.move_msg)
		#rospy.loginfo("MessagePublished")

#if __name__ == '__main__':
#	rospy.init_node('escape_maze')
#	moveRobot_obj = MoveRobot()
#	moveRobot_obj.send_cmd(0.3,0)

