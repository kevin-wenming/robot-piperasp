import smbus
import time

address = 0x48                                          #ADC模块地址
A0 = 0x40                                               #四个模拟量接口地址
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)                                    #开启I2C总线
def gettemp():
    bus.write_byte(address,A0)                          #读取字节
    value = bus.read_byte(address)                      #赋值
    print("当前温度:%1.0f "%(value))
    
    t=open(r'/home/pi/trye/project/workdata.txt','a')   #打开文件并存储数据
    t.write(str(value)+'\n')
    t.write('------------'+'\n')
    time.sleep(1)

    