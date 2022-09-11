#---
# file: Motor compensation.py
# description: Motor compensation
#---
# Motor compensation
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import struct
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

# Motor compensation is used to adjust small differences in speed between motors
# direction:1=left motor direction:2=right motor
# speed:0~255
def mostotCompensation(direction, speed):
    if direction == 1:
        buf = bytearray(2)
        buf[0] = 0x08
        buf[1] = speed
        i2c.write(I2caddr, buf)
    elif  direction == 2:
        buf = bytearray(2)
        buf[0] = 0x09
        buf[1] = speed
        i2c.write(I2caddr, buf)

while True:
    motor(1, 30, 1, 0)
    sleep(1000)
    mostotCompensation(1, 10)
    sleep(1000)