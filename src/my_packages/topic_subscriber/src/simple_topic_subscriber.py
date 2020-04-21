#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	print data

print "Subscriber is executing"
rospy.init_node("topic_subscriber")
sub = rospy.Subscriber('/Texter', String, callback)
rospy.spin()
