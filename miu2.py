import smbus
import math
import serial
import time
import datetime

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c



def reat_byte(adr):
    return bus.read_byte_data(address,adr)

def read_word(adr):
    high = bus.read_byte_data(address,adr)
    low = bus.read_byte_data(address,adr+1)
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

def get_y_rotation(x,y,z):                  #计算X、Y、Z轴转动角度
    radians = math.atan2(x,dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y,dist(x,z))
    return math.degrees(radians)

def get_z_rotation(x,y,z):
    radians = math.atan2(z,dist(x,y))
    return math.degrees(radians)

bus = smbus.SMBus(1)
address = 0x68

def getimu():                               #定义主函数

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
    xd = get_x_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled)  #x轴转动角度
    yd = get_y_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled)  #y轴转动角度
    zd = get_z_rotation(accel_xout_scaled,accel_yout_scaled,accel_zout_scaled)  #z轴转动角度
    data=[xd,yd,zd,'-------']
   
    
    t=open(r'/home/pi/trye/project/workdata.txt','a')                  #讲数据存储在文件中
    for i in range(4):
        t.write(str(data[i])+'\n')
    t.close()
    time.sleep(1)

  
        