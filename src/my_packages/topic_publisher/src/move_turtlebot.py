#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


def moveRobot():
	msg.linear.x = 0.2
	msg.angular.y = 0
	pub.publish(msg)

def stopRobot():
	msg.linear.x = 0
	msg.angular.y = 0
	pub.publish(msg)

if __name__ == '__main__':
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	msg = Twist()
	rospy.init_node("topic_publisher")
	count = 0
	rate = rospy.Rate(5)
	rate.sleep()
	stopRobot()
	

