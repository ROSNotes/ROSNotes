import rospy
from geometry_msgs.msg import Twist


pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
rospy.init_node('xuehenxiaowugui')
xuegai_rate = rospy.Rate(6)                                                                                                

while not rospy.is_shutdown():
	moveturtle = Twist()
	moveturtle.linear.x = 2
	moveturtle.angular.z = 2

	pub.publish(moveturtle)

	xuegai_rate.sleep()
