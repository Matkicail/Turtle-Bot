#!/usr/bin/env python
import rospy
import math
import tf
# from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from std_msgs.msg import String

# Global
turn = 0.0 # Turning Rate
blob_position = 0 # x position for the blob
blob_area = 0.0
known_area = 0.0
blob_distance = 0.0
known_distance = 0.0
robot_angle = 0.0
found = False
flagFound = False

def callbackRun(data):
    global turn
    global blob_position
    global blob_area
    global known_area
    global blob_distance
    global known_distance
    global found 
    global flagFound

    if flagFound:
        return
    found = True
    flagFound = True

    blob_position = data
    blob_distance = data.z

def run():
    #Initiate node and setup parameters
    rospy.init_node('turtle_tf_listener')
    global blob_position
    global blob_area
    global known_area
    global blob_distance
    global known_distance
    global robot_angle
    global found 
    global flagFound

    # rospy.wait_for_service('spawn')
    publishObjectPosition = rospy.Publisher('objectCoordinate', Point, queue_size=1)
    rate = rospy.Rate(2)
    sub = rospy.Subscriber('/blob/point_blob', Point, callbackRun)

    #Set up a twist for storing coordinates
    twist = Twist()

    listener = tf.TransformListener()
    rospy.sleep(1)
    while not rospy.is_shutdown():
        if(not found):
            # try:

            #     (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
            #     angular = tf.transformations.euler_from_quaternion([rot[0], rot[1], rot[2], rot[3]])
            #     print(angular[2])
                
            #     if(abs(angular[2]) > math.pi/2):
            #         print("hi")
            # except:
            #     pass
            rate.sleep()
            continue
        elif found and flagFound:
            try:
                (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
                print(e)
                rospy.sleep(0.1)
                continue

            angular = tf.transformations.euler_from_quaternion([rot[0], rot[1], rot[2], rot[3]])

            robotRotation = angular[2]

            if(robotRotation < 0):
                robotRotation += 2 * math.pi

            angle = (blob_position.x) * math.pi/2
            print(angle)

            #Correct it if it's in the wrong range
            if(angle > 0 and 0 < robotRotation < math.pi/2):
                angle = angle
                print("hi")
            elif (angle < 0 and 0 < robotRotation < math.pi/2):
                angle = angle + math.pi/2
                print("hi2")
            elif(angle < 0 and  math.pi/2 < robotRotation < math.pi):
                print("hi3")
                angle = math.pi - abs(angle)
            elif(angle > 0 and  math.pi/2 < robotRotation < math.pi):
                print("hi4")
                angle = angle + math.pi /2
            elif angle < 0 and math.pi < robotRotation < 1.5 * math.pi:
                print("hi5")
                angle = abs(angle) + math.pi/2
            elif angle > 0 and math.pi < robotRotation < 1.5 * math.pi:
                print("hi6")
                angle = abs(angle) + math.pi/2
            elif angle < 0 and 1.5 * math.pi < robotRotation < 2 * math.pi:
                print("hi7")
                angle = angle
            elif angle > 0 and 1.5 * math.pi < robotRotation < 2 * math.pi:
                print("hi8")
                angle = angle + 1.5 * math.pi


            linear = trans

            twist.linear.x = linear[0] + blob_distance * math.cos(angle)
            twist.linear.y = linear[1] + blob_distance * math.sin(angle)

            coordinate = Point()
            coordinate.x = twist.linear.x
            coordinate.y = twist.linear.y

            if(math.isnan(twist.linear.x) or math.isnan(twist.linear.y)):
                flagFound = False
                found = False
                continue

            print(coordinate)
            print(found)

            #Publish coordinates
            publishObjectPosition.publish(coordinate)
            blob_position = 0
            rate.sleep()
            found = False

if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException: pass
                                    
