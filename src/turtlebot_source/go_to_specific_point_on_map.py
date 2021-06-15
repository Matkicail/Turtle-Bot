#!/usr/bin/env python

'''
Copyright (c) 2015, Mark Silliman
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

# TurtleBot must have minimal.launch & amcl_demo.launch
# running prior to starting this script
# For simulation: launch gazebo world & amcl_demo prior to run this script

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
import numpy as np

class GoToPose():
    def __init__(self):

        self.goal_sent = False

        # What to do if shut down (e.g. Ctrl-C or failure)
        rospy.on_shutdown(self.shutdown)
        
        # Tell the action client that we want to spin a thread by default
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Wait for the action server to come up")

        # Allow up to 5 seconds for the action server to come up
        self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000),
                                     Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

        # Start moving
        self.move_base.send_goal(goal)

        # Allow TurtleBot up to 60 seconds to complete task
        success = self.move_base.wait_for_result(rospy.Duration(60)) 

        state = self.move_base.get_state()
        result = False


        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        self.goal_sent = False
        self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(2)

#---------------------------------------------------------------------
rospy.init_node('nav_test', anonymous=False)
navigator = GoToPose()
quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}
objectFound = False
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size = 1)
#---------------------------------------------------------------------
def callbackObjectFound(coordinates):
    global objectFound
    objectFound = True
    navigator.shutdown()
    twist = Twist()
    twist.angular.z = 1

    while not rospy.is_shutdown():
        pub.publish(twist)
        rospy.sleep(0.2)


#---------------------------------------------------------------------

if __name__ == '__main__':
    rospy.Subscriber('objectCoordinate', Point, callbackObjectFound)

    try:
        pointsOfInterests=np.array([[0,0],
                                    [5.8,-0.055],
                                    [5.8,6.08],
                                    [2.1997,6.5573],
                                    [2.042,9.7708],
                                    [-5.4973,10.88],
                                    [-5.4973,1.3793],
                                    [-5.4973,10.88],
                                    [1.836,9.5812],
                                    [-0.67498,6.4268],
                                    [2.0049,3.5128],
                                    [-2.9432,3.1102],
                                    [0,0]]).astype(float)

        counter=1
        global objectFound
        while objectFound != True:
            position = {'x': (pointsOfInterests[counter][0]), 'y' : (pointsOfInterests[counter][1])}
            
            rospy.loginfo("Go to (%s, %s) pose counter: %s", position['x'], position['y'], counter)
            
            if objectFound != True:
                success = navigator.goto(position, quaternion)
            
            counter=counter+1
            if counter==len(pointsOfInterests):
                counter=0

            if success:
                rospy.loginfo("Hooray, reached the desired pose")
            else:
                rospy.loginfo("The base failed to reach the desired pose")
            rospy.sleep(1)

        # Sleep to give the last log messages time to be sent
        rospy.spin()
        
    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")

