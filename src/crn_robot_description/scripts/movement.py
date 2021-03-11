#! /usr/bin/env python2
import rospy
# import command sending libraries
from std_msgs.msg import Float64
import future
from geometry_msgs.msg import Twist
import math


def main():
    i=0
    j=0
    x=0
    ##### Define publishers for the joint controllers #####
    rospy.init_node("movement")
    wheel_fl=rospy.Publisher('/crn_robot_description/wheel_front_left_controller/command', Float64, queue_size=1)
    wheel_fr=rospy.Publisher('/crn_robot_description/wheel_front_right_controller/command', Float64, queue_size=1)
    wheel_bl=rospy.Publisher('/crn_robot_description/wheel_rear_left_controller/command', Float64, queue_size=1)
    wheel_br=rospy.Publisher('/crn_robot_description/wheel_rear_right_controller/command', Float64, queue_size=1)
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        wheel_bl.publish( 1)
        wheel_br.publish( 1)
        wheel_fl.publish( 1)
        wheel_fr.publish( 1)
        #print("Hello")

        rate.sleep()

if __name__ == '__main__':
    main()
