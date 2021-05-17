#!/usr/bin/env python
import rospy
import sys, select, tty, termios
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

key_mapping = { 'w': [ 0, 0.5], 'x': [0, -0.5], 'a': [1, 0], 'd': [-1, 0], 's': [ 0, 0] }
shoulder_key = {'y':[0.02], 'h':[-0.02] }
gripper_key = {'i':[0.02], 'k':[-0.02] }
gripper1_key = {'i':[0.02], 'k':[-0.02] }
waist_key = {'n':[0.02], 'm':[-0.02] }
elbow_key = {'u':[0.02], 'j':[-0.02] }
wrist_key = {'o':[0.02], 'l':[-0.02] }


res = 0
res1 = 0
res2 = 0
res3 = 0
res4 = 0


def elbow_pos(y,lim_low, lim_high):
    global res
    res = res + y
    if res < lim_low:
      res = lim_low
    elif res > lim_high:
      res = lim_high
    else:
      res = res
    return res

def waist_pos(y,lim_low, lim_high):
    global res1
    res1 = res1 + y
    if res1 < lim_low:
      res1 = lim_low
    elif res1 > lim_high:
      res1 = lim_high
    else:
      res1 = res1
    return res1

def shoulder_pos(y,lim_low, lim_high):
    global res2
    res2 = res2 + y
    if res2 < lim_low:
      res2 = lim_low
    elif res2 > lim_high:
      res2 = lim_high
    else:
      res2 = res2
    return res2

def gripper_pos(y,lim_low, lim_high):
    global res3
    res3 = res3 + y
    if res3 < lim_low:
      res3 = lim_low
    elif res3 > lim_high:
      res3 = lim_high
    else:
      res3 = res3
    return res3

def wrist_pos(y,lim_low, lim_high):
    global res4
    res4 = res4 + y
    if res4 < lim_low:
      res4 = lim_low
    elif res4 > lim_high:
      res4 = lim_high
    else:
      res4 = res4
    return res4

def keys_cb(msg, twist_pub):
    t = Twist()
    shoulder_twist = JointTrajectory()
    point = JointTrajectoryPoint()
    gripper_twist = JointTrajectory()
    g_point = JointTrajectoryPoint()
    gripper1_twist = JointTrajectory()
    g1_point = JointTrajectoryPoint()
    waist_twist = JointTrajectory()
    w_point = JointTrajectoryPoint()
    elbow_twist = JointTrajectory()
    elbow_point = JointTrajectoryPoint()
    wrist_twist = JointTrajectory()
    wrist_point = JointTrajectoryPoint()

    if key_mapping.has_key(msg.data[0]):
        vels = key_mapping[msg.data[0]]
        t.angular.z = vels[0]
        print("angular : %s"%t.angular.z)
        t.linear.x = vels[1]
        print("linear : %s"%t.linear.x)
        twist_pub.publish(t)

    if shoulder_key.has_key(msg.data[0]):
        vels = shoulder_key[msg.data[0]]
        shoulder_twist.header.stamp = rospy.Time.now()
        shoulder_twist.joint_names = ['arm_joint']
        point.positions = [shoulder_pos(vels[0],-1,4)]
        point.time_from_start = rospy.Duration(1)
        shoulder_twist.points.append(point)
        print("Shoulder : %s"%point.positions)
        arm.publish(shoulder_twist)

    if gripper_key.has_key(msg.data[0]):
        velse = gripper_key[msg.data[0]]
        gripper_twist.header.stamp = rospy.Time.now()
        gripper_twist.joint_names = ['finger2_joint']
        g_point.positions = [gripper_pos(velse[0],0,1)]
        g_point.time_from_start = rospy.Duration(1)
        gripper_twist.points.append(g_point)
        print("Gripper : %s"%g_point.positions)
        finger_2.publish(gripper_twist)

    if gripper1_key.has_key(msg.data[0]):
        velse = gripper1_key[msg.data[0]]
        gripper1_twist.header.stamp = rospy.Time.now()
        gripper1_twist.joint_names = ['finger1_joint']
        g1_point.positions = [gripper_pos(velse[0],0,1)]
        g1_point.time_from_start = rospy.Duration(1)
        gripper1_twist.points.append(g1_point)
        print("Gripper1 : %s"%g1_point.positions)
        finger_1.publish(gripper1_twist)

    if waist_key.has_key(msg.data[0]):
        velse = waist_key[msg.data[0]]
        waist_twist.header.stamp = rospy.Time.now()
        waist_twist.joint_names = ['mount_arm_joint']
        w_point.positions = [waist_pos(velse[0],-3.14,3.14)]
        w_point.time_from_start = rospy.Duration(1)
        waist_twist.points.append(w_point)
        print("Waist : %s"%w_point.positions)
        mount_arm.publish(waist_twist)

    if elbow_key.has_key(msg.data[0]):
        velse = elbow_key[msg.data[0]]
        elbow_twist.header.stamp = rospy.Time.now()
        elbow_twist.joint_names = ['wrist_arm_joint']
        elbow_point.positions = [elbow_pos(velse[0],-2.5,2.5)]
        elbow_point.time_from_start = rospy.Duration(1)
        elbow_twist.points.append(elbow_point)
        print("Elbow : %s"%elbow_point.positions)
        wrist_arm.publish(elbow_twist)


    if wrist_key.has_key(msg.data[0]):
        velse = wrist_key[msg.data[0]]
        wrist_twist.header.stamp = rospy.Time.now()
        wrist_twist.joint_names = ['servo_joint']
        wrist_point.positions = [wrist_pos(velse[0],-3.14,3.14)]
        wrist_point.time_from_start = rospy.Duration(1)
        wrist_twist.points.append(wrist_point)
        print("Wrist : %s"%wrist_point.positions)
        servo.publish(wrist_twist)

def start():
    global twist_pub, arm, t, finger_2, mount_arm, wrist_arm, finger_1, servo
    twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    arm = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
    finger_1 = rospy.Publisher('/finger1_controller/command', JointTrajectory, queue_size=10)
    finger_2 = rospy.Publisher('/finger2_controller/command', JointTrajectory, queue_size=10)
    mount_arm = rospy.Publisher('/mount_arm_controller/command', JointTrajectory, queue_size=10)
    wrist_arm = rospy.Publisher('/wrist_arm_controller/command', JointTrajectory, queue_size=10)
    servo = rospy.Publisher('/servo_joint_controller/command', JointTrajectory, queue_size=10)
    rospy.Subscriber('keys', String, keys_cb, twist_pub)
    rospy.init_node('Robot_control')
    rospy.spin()

while not rospy.is_shutdown():
    print "  "
    print("The excavator teleop has been launched")
    start()