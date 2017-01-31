#!/usr/bin/env python
import rospy
import random
import sys
from move_base_msgs.msg import MoveBaseActionGoal 
import time


if __name__ == "__main__":
    try:
    	rospy.init_node("random_move")
    	rate = rospy.Rate(0.08)
	init_time = rospy.Time.now()
	seq=0
    	while not rospy.is_shutdown() and rospy.Time.now().secs-init_time.secs<600:
    		pub = rospy.Publisher("/move_base/goal", MoveBaseActionGoal, queue_size=10)
		cord=MoveBaseActionGoal()
		seq=seq+1
		cord.header.seq=seq
		cord.header.stamp=rospy.Time.now()
		cord.goal.target_pose.header.seq=seq
		cord.goal.target_pose.header.stamp=rospy.Time.now()
		cord.goal.target_pose.header.frame_id="map"
		cord.goal.target_pose.pose.position.x=-10
		cord.goal.target_pose.pose.position.y=-10

		pub.publish(cord)
	   	rate.sleep()
	    
    except rospy.ROSInterruptException:
	pass
