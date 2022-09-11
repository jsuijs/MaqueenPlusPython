#---
# file: Motor.py
# description: Motor control
#---
# Motor control
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
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

while True:
    # Maqueen Plus left motor forward speed 255
    motor(1, 255, 1, 0)
    sleep(1000)
    # Maqueen Plus right motor forward speed 255
    motor(1, 0, 1, 255)
    sleep(1000)
    # Maqueen Plus left motor back speed 255
    motor(2, 255, 2, 0)
    sleep(1000)
    # Maqueen Plus right motor back speed 255
    motor(2, 0, 2, 255)
    sleep(1000)