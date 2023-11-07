# this is for the ros1 version
import roslib
roslib.load_manifest('learning_tf')
import rospy

import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
 br = tf.TransforBroadcaster()
 br.sendTransform((msg.x,msg.y,0),
  		   tf.transformations.quarternion_from_euler(0,0,msg.theta),
  		   rospy.Time.now(),
  	           turtlename,
  		   "world")

if __name__ == '__main__':
 rospy.init_node('turtle_tf_broadcaster')
 turtlename = rospy.get_param('_turtle')
 rospy.Subscriber('/%s/pose' % turtlename,
  		  turtlesim.msg.Pose,
  		  handle_turtle_pose,
  		  turtlename)
 rospy.spin()
