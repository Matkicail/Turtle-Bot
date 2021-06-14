#!/usr/bin/env python
import rospy
import math
import tf
# from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point

# Global
turn = 0.0 # Turning Rate
blob_position = 0 # x position for the blob
blob_area = 0.0
known_area = 0.0
blob_distance = 0.0
known_distance = 0.0
robot_angle = 0.0

def callbackRun(data):
    global turn
    global blob_position
    global blob_area
    global known_area
    global blob_distance
    global known_distance

    
        
    # if obj.name == "targetObject":
    rospy.loginfo("Blob <" + "> Detected!")
    blob_position = data.x
    # blob_area = point.area
    rospy.loginfo("blob is at %s"%blob_position)
    # if blob_position > 220:
    #     rospy.loginfo("TURN RIGHT")
    #     blob_distance = 0.0
    #     turn = -1.0
    # if blob_position < 180:
    #     rospy.loginfo("TURN LEFT")
    #     blob_distance = 0.0
    #     turn = 1.0
    # if blob_position > 180 and blob_position < 220:
    rospy.loginfo("CENTERED")
    blob_distance = data.z
    turn = 0.0

def run():
    # rospy.init_node("track_blob_color_node", log_level = rospy.WARN)
    print("SUP")
    rospy.init_node('turtle_tf_listener')
    global blob_position
    global blob_area
    global known_area
    global blob_distance
    global known_distance
    global robot_angle

    listener = tf.TransformListener()
    # rospy.wait_for_service('spawn')
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size = 1)
    rate = rospy.Rate(2)
    sub = rospy.Subscriber('/blob/point_blob', Point, callbackRun)

    global turn
    twist = Twist()

    print("YUP")
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            print(e)
            rospy.sleep(0.1)
            continue

        angular = tf.transformations.euler_from_quaternion([rot[0], rot[1], rot[2], rot[3]])
        # print(angular)
        linear = trans
        print(linear)

        print("LOL")
        # if turn != 0.0:
        #     str = "Turning %s"%turn
        #     rospy.loginfo(str)
        #     twist.linear.x = linear[0]
        #     twist.linear.y = linear[1]
        #     twist.linear.z = linear[2]
        #     twist.angular.x = angular[0]
        #     twist.angular.y = angular[1]
        #     twist.angular.z = angular[2] + turn
        #     print("Hi")
        #     turn = 0.0
        # else:
        str = "Straight %s"%turn
        rospy.loginfo(str)
        # angle = angular[2]
        # if angle < 0:
            # angle -= math.pi
        twist.linear.x = linear[0] + blob_distance * math.cos(angular[2])
        twist.linear.y = linear[1] + blob_distance * math.sin(angular[2])
        twist.linear.z = linear[2]
        twist.angular.x = angular[0]
        twist.angular.y = angular[1]
        twist.angular.z = angular[2]

        # twist.angular.z = 0.5
        print(blob_distance)
        print(angular[2])
        print(twist.linear)
        # pub.publish(twist)
        blob_position = 0
        rate.sleep()

if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException: pass
                                    
