import smbus
import time
import datetime

address = 0x48                                          #ADC模块地址
A0 = 0x40                                               #四个模拟量接口地址
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)                                    #开启I2C总线
def gettemp():
 while(1):
    bus.write_byte(address,A0)                          #读取字节
    value = bus.read_byte(address) /5                     #赋值
    print("当前温度:%1.0f "%(value))
    timestamp = time.time()
    stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    t=open(r'/home/pi/trye2/11-12/Kalman-Filter-Python-for-mpu6050-master/project/project/project/temp.txt','a')   #打开文件并存储数据
    t.write(str(stamp)+'\n')
    t.write(str(value)+'\n')
    t.write('------------'+'\n')
    

    