import smbus
import math
import time
import numpy as np
import cv2
import datetime


power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

newfile=r'/home/pi/trye/imu1.txt'
newfile=r'/home/pi/trye/temp1.txt'

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


def reat_byte(adr):
    return bus.read_byte_data(i2cAddress1,adr)

def read_word(adr):
    high = bus.read_byte_data(i2cAddress1,adr)
    low = bus.read_byte_data(i2cAddress1,adr)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if(val >= 0x8000):
        return-((65535 - val)+1)
    else:
        return val
    
def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x,dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y,dist(x,z))
    return math.degrees(radians)

def get_z_rotation(x,y,z):
    radians = math.atan2(z,dist(x,y))
    return math.degrees(radians)

bus = smbus.SMBus(1)
i2cAddress1 = 0x68
i2cAddress2 = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43

while True:
    i = datetime.datetime.now()
    
    bus.write_byte(0X48,0X40)
    value2 = bus.read_byte(0X48)
    print("当前温度:%1.0f "%(value2))
    
    t=open(r'/home/pi/trye/temp1.txt','a')
    t.write(str(value2)+'\n')
    t.write(str(i)+'\n')
    
    print("陀螺仪数据")
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    print("x轴陀螺仪计数值:",gyro_xout,"每秒转度:",(gyro_xout / 131))
    print("y轴陀螺仪计数值:",gyro_yout,"每秒转度:",(gyro_yout / 131))
    print("z轴陀螺仪计数值:",gyro_zout,"每秒转度:",(gyro_zout / 131),"n")

    print("加速度数据")

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    print("X轴加速度值：",accel_xout,"每秒旋转角度：",accel_xout_scaled)
    print("Y轴加速度值：",accel_yout,"每秒旋转角度：",accel_yout_scaled)
    print("Z轴加速度值：",accel_zout,"每秒旋转角度：",accel_zout_scaled)

    print("-----------------------")
    print("x轴旋转角度：",get_x_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled))
    print("y轴旋转角度：",get_y_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled))
    print("z轴旋转角度：",get_z_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled))
    data=[get_x_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled),get_y_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled),get_z_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled),i,'-------']
    t=open(r'/home/pi/trye/imu1.txt','a')
    for i in range(10):
        t.write(str(data[i])+'\n')
    t.close()
    
    ret, frame = cap.read()
    if ret == 1:
        frame = cv2.flip(frame,0)
        out.write(frame)
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               