import smbus
import math
import serial
import time
import miu2
import temp2
import datetime

while(1):  
  m = datetime.datetime.now()                        #获取当前时间
  t=open(r'/home/pi/trye/project/workdata.txt','a')  #记录当前时间
  t.write(str(m)+'\n')                               #记录当前时间
  try:
    miu2.getimu()                                      #获取IMU数据
    temp2.gettemp()                                    #获取模拟量接口数据
  except IOError:                                                      #避免I/O错误导致程序中断
    print("Error:NO data")