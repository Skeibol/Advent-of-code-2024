import re
import cv2
import numpy as np
import time
import os

class Robot():
    def __init__(self,robotParameters):
        self.X = robotParameters[0]
        self.Y = robotParameters[1]
        self.velocityX = robotParameters[2]
        self.velocityY = robotParameters[3]
        
    def moveRobot(self,seconds):
        self.X += (self.velocityX * seconds )
        self.Y += (self.velocityY * seconds )
        self.X =  self.X  % BATHROOM_WIDTH
        self.Y =  self.Y  % BATHROOM_HEIGHT
        
    def getRobotQuadrant(self):
        axisX = BATHROOM_WIDTH // 2 
        axisY = BATHROOM_HEIGHT // 2 
        
        if self.X < axisX:
            if self.Y > axisY:
                return 3
            elif self.Y < axisY:
                return 1
        elif self.X > axisX:
            if self.Y < axisY:
                return 2
            elif self.Y > axisY:
                return 4
        
        return 0


BATHROOM_WIDTH = 101
BATHROOM_HEIGHT = 103
quadrants = [0,0,0,0,0]
robots = []
with open("./advent-of-code/day14/input.txt", "r") as file:
    for line in file:
        if line == "\n":
            continue

        x = re.findall("-?\\d+", line)
        robot = Robot([int(x) for x in x])
        robots.append(robot)



imageDirectory = r'./advent-of-code/day14/trees'
os.chdir(imageDirectory)

cnt = 1
while cnt<10000:
    filename = f"frame_{cnt}.png"
    img = np.zeros([BATHROOM_HEIGHT,BATHROOM_WIDTH,1])

    img[:,:,0] = np.ones([BATHROOM_HEIGHT,BATHROOM_WIDTH])*0
    for robot in robots:
        robot.moveRobot(51)
        img[robot.Y,robot.X,0] = 255
    print(cnt)
    img = cv2.resize(img, (BATHROOM_HEIGHT * 4, BATHROOM_WIDTH * 4))
    cv2.imwrite(filename, img)
    cnt+=1