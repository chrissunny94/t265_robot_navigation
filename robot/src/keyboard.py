#!/usr/bin/env python
import sys, select, tty, termios
import rospy
from std_msgs.msg import String
if __name__ == '__main__':
    key_pub = rospy.Publisher('keys', String, queue_size=1)
    rospy.init_node("keyboard_driver")
    rate = rospy.Rate(100)
    old_attr = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())


    msg = """
Control Your RC_Robot!
---------------------------
   Moving Around | Shoulder | Elbow | Gripper | Wrist
        w        |  	y   |  u    |   i     |    o
   a    s    d   |      h   |  j    |   k     |    l
        x        | Waist_Rotate |
                 |    n    m    |
        
CTRL-C to quit
"""

    print msg
    while not rospy.is_shutdown():
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            key_pub.publish(sys.stdin.read(1))
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
