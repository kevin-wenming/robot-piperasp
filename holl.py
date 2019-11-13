import time
import datetime
import RPi.GPIO as GPIO
import smbus
numholl=0
def sensorCallback(channel):
  # 如果传感器输出发生变化，则调用
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  if GPIO.input(channel):
    # 没有磁铁
    print("Sensor HIGH " + stamp)
  else:
    # 磁铁
    global numholl
    numholl=numholl+1
    t=open(r'/home/pi/trye2/11-12/Kalman-Filter-Python-for-mpu6050-master/project/project/project/holl.txt','a')   #打开文件并存储数据
    t.write(str(numholl)+'\n')
    t.write(str(stamp)+'\n')
    t.write('------------'+'\n')
    print("Sensor LOW " + stamp)
def main():
  sensorCallback(17)
  try:
    # 进入循环，直到手动按CTRL-C退出
    while True :
      time.sleep(0.001)
      
  except KeyboardInterrupt:
    # 重置GPIO
    GPIO.cleanup()
# 告诉GPIO库使用GPIO引用
def holl123():
  GPIO.setmode(GPIO.BCM)
  print("Setup GPIO pin as input on GPIO17")
# 设置开关GPIO为输入
# 默认拉高
  GPIO.setup(17 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.add_event_detect(17, GPIO.BOTH, callback=sensorCallback, bouncetime=200)
  main()

 