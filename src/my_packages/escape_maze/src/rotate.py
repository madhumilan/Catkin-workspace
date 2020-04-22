#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

def rotate(publisher):
	print "In rotate function"
	move = Twist()
	move.angular.z = 0.5
	publisher.publish(move)
	print "Message published."
	time.sleep(5)
	move.angular.z = 0.0
	publisher.publish(move)
	print "Returning."

if __name__ == '__main__':
	rospy.init_node('escape_maze')
	print "Node initialized."
	publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	rotate(publisher)
#	rospy.spin()

