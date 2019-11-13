import caijixy
from Anglez import *
import smbus
import math
import serial
import time
import temp2
import datetime
import holl

gyro = 250      # 250, 500, 1000, 2000 [deg/s]
acc = 2         # 2, 4, 7, 16 [g]
tau = 0.98
mpu = MPU(gyro, acc, tau)

    # Set up sensor and calibrate gyro with N points
    #mpu.setUp()
mpu.calibrateGyro(500)

    # Run for 20 secounds
startTime = time.time()

def getimu():
   while(1):
    caijixy.anxy()
    mpu.compFilter()
