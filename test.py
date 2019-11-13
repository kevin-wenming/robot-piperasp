import caijixy
from Anglez import *
import smbus
import math
import serial
import time
import temp2
import datetime
import holl
import threading
import allimu
import video2


threads = []

t1 = threading.Thread(target=holl.holl123)
threads.append(t1)
t2 = threading.Thread(target=temp2.gettemp)
threads.append(t2)
t3 = threading.Thread(target=allimu.getimu)
threads.append(t3)
t4 = threading.Thread(target=video2.getvideo)
threads.append(t4)
if __name__=='__main__':
    for t in threads:
        t.start()
    #for t in threads:
     #   t.join()



