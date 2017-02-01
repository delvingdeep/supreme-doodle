#!/usr/bin/env python
import rospy
import random
import sys
from geometry_msgs.msg import PoseStamped 
import time


if __name__ == "__main__":
    try:
    	rospy.init_node("random_move")
    	rate = rospy.Rate(0.08)
	init_time = rospy.Time.now()
	seq=0
    	while not rospy.is_shutdown() or (rospy.Time.now().secs-init_time.secs< 600):
    		pub = rospy.Publisher("/move_base/current_goal", PoseStamped, queue_size=10)
		cord=PoseStamped()
		seq=seq+1
		cord.header.seq=seq
		cord.header.stamp=rospy.Time.now()
		cord.header.frame_id="odom"
		cord.pose.position.x=-10.0
		cord.pose.position.y=-10.0
		cord.pose.orientation.w = 1.0

		pub.publish(cord)
	   	rate.sleep()
	    
    except rospy.ROSInterruptException:
	pass
