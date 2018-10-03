import rospy
from std_msgs.msg import String 
from geometry_msgs.msg import Twist 

def callback(xue):
	if (xue.linear.x>0):
	  rospy.loginfo("xiaocheqianjin")
	if (xue.linear.x<0):
	  rospy.loginfo("xiaochehoutui")
 	if (xue.angular.z>0):
	  rospy.loginfo("xiaochezuozhuan")
	if (xue.angular.z<0):
	  rospy.loginfo("xiaocheyouzhuan")
def listener():

	rospy.init_node('listener', anonymous = True)
	rospy.Subscriber("cmd_vel", Twist, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()

