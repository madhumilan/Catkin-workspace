#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

def rotate(pub):
	move = Twist()
	move.angular.z = 0.5
	pub.publish(move)
	time.sleep(5)
	move.angular.z = 0.0
	pub.publish(move)

if __name__ == '__main__':
	rospy.init_node('escape_maze',anonymous=True)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	rotate(pub)

