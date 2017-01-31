#!/usr/bin/env python
import rospy
import random
import sys
from move_base_msgs.msg import MoveBaseActionGoal 
import time


if __name__ == "__main__":
    try:
    	rospy.init_node("test_random")
    	rate = rospy.Rate(0.033)
	init_time = rospy.get_time()
	seq=0
    	while not rospy.is_shutdown() :
    		pub = rospy.Publisher("/move_base/goal", MoveBaseActionGoal, queue_size=10)
		cord=MoveBaseActionGoal()
		cord.header.seq=seq
		cord.header.stamp=rospy.Time.now()
		cord.goal.target_pose.header.seq=seq
		cord.goal.target_pose.header.stamp=rospy.Time.now()
		cord.goal.target_pose.header.frame_id="map"
		cord.goal.target_pose.pose.position.x=random.uniform(-10,10)
		cord.goal.target_pose.pose.position.y=random.uniform(-10,10)
		cord.goal.target_pose.pose.orientation.w=1.0
		#print cord
		pub.publish(cord)
		seq=seq+1
	   	rate.sleep()
	    
    except rospy.ROSInterruptException:
	pass
