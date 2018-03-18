import pycom
from machine import I2C
import time
from MAG3110 import MAG_3110
from startiot import Startiot

#Initial
pycom.heartbeat(False) # disable the blue blinking
pycom.rgbled(0x0000FF)
#Toggle LORA mode.
CONNECT_DEVICE = 0

if CONNECT_DEVICE:
    pycom.rgbled(0xFF0000)
    iot = Startiot()
    print("Awaiting connection")
    iot.connect()
    print("Connected")
    pycom.rgbled(0x00FF00)
#Create instance of the MAG3110 sensor
Mag = MAG_3110()


while True:
    pack = Mag.collect_data()
    temp = Mag.temperature()
    Mag.print(pack, temp)
    if CONNECT_DEVICE:
        print("Attempting to send data")
        iot.send(pack)
        print("Data sent")
    time.sleep(2)