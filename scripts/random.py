#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = random.randint(1,4)
    rospy.loginfo(message.data*n)

if __name__ == '__main__':
    rospy.init_node('random')
    sub = rospy.Subscriber('twice', Int32, cb)
    rospy.spin()
