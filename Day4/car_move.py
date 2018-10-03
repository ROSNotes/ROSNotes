import rospy
from geometry_msgs.msg import Twist


pub = rospy.Publisher('/cmd_vel/mx_chassis',Twist,queue_size=10)
rospy.init_node('xiaocheyidong')
xuegai_rate = rospy.Rate(10)

while not rospy.is_shutdown():
	movecar = Twist()
	movecar.linear.x = 1
	movecar.angular.z = 1

	pub.publish(movecar)

	xuegai_rate.sleep()
