# -*- encoding: UTF-8 -*-
'''PoseInit: Small example to make Nao go to an initial position.'''

import argparse
import time
from naoqi import ALProxy
def main(robotIP,PORT=9559):
    motionProxy = ALProxy("ALMotion",robotIP,PORT)
    postureProxy = ALProxy("ALRobotPosture",robotIP,PORT)
    #Wake up robot
    motionProxy.wakeUp()
    #Send robot to Stand Init
    postureProxy.goToPosture("StandInit",0.5)
    time.sleep(2);
    #Go to rest position
    motionProxy.rest()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",type=str,default="192.168.1.106",
                        help="Robot ip address")
    parser.add_argument("--port",type=int,default=9559,help="Robot port number")
    args = parser.parse_args()
    main(args.ip,args.port)


