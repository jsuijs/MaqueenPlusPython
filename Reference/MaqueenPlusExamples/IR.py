#---
# file: IR.py
# description: Infrared-controlled Maqueen Plus
#---
# Infrared-controlled Maqueen Plus
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import necir
I2caddr = 0x10

# Maqueen Plus motor control
# direction:1 forward  2 back
# speed:0~255
def motor(directionL, speedL, directionR, speedR):
    buf = bytearray(5)
    buf[0] = 0x00
    buf[1] = directionL
    buf[2] = speedL
    buf[3] = directionR
    buf[4] = speedR
    i2c.write(I2caddr, buf)

def cb(addr, cmd):
    # Infrared data address
    print('addr=', hex(addr))
    # Infrared key value
    print('cmd=', hex(cmd))
    # IR address judgment
    if addr == 0xbf00:
        if cmd == 0xee11:    #Button 2, forward
            motor(1, 255, 1, 255)
        if cmd == 0xe619:    #Button 8, back
            motor(2, 255, 2, 255)
        if cmd == 0xeb14:    #Button 4, left
            motor(1, 0, 1, 255)
        if cmd == 0xe916:    #Button 6, right
            motor(1, 255, 1, 0)
        if cmd == 0xea15:    #Button 5, stop
            motor(1, 0, 1, 0)
# Initialize IR receiving pin and request data
necir.init(16, cb)

while True:
  pass