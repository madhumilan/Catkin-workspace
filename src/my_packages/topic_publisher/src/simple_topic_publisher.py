#! /usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node("topic_publisher")
pub = rospy.Publisher('/Texter', String, queue_size=1)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
	pub.publish("Hello...")
	rate.sleep()
