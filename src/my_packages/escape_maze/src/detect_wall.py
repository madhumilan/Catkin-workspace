#! /usr/bin/env python

import rospy
from move_robot import MoveRobot
from sensor_msgs.msg import LaserScan

class StopWall:
    def __init__(self):
        self.sub = rospy.Subscriber('/scan', LaserScan, self.callback)
        self.moverobot_object = MoveRobot()
#	self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def callback(self, msg):
	'''
        print "Distance at 175 to 185:", msg.ranges[175:186]
	print "Distance at 0 to 10:", msg.ranges[0:11]
	print "Distance at 311 to 320:", msg.ranges[-1:-11]
	'''
	print "Distance at index 179=", msg.ranges[179]        
        if msg.ranges[179] <= 0.3:
            linear_x = 0.0
            angular_z = 0.3
            self.moverobot_object.send_cmd(linear_x, angular_z)

        #If the distance to an obstacle in front of the robot is smaller than 1 meter, the robot will stop
        if msg.ranges[179] > 0.3:
            linear_x = 0.15
            angular_z = 0.0
            self.moverobot_object.send_cmd(linear_x, angular_z)
            


if __name__ == '__main__':
    rospy.init_node('escape_maze')
    stopwall_object = StopWall()
    rospy.spin()
