#---
# file: Patrol.py
# description: Line-tracking Maqueen Plus
#---
# Line-tracking Maqueen Plus
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

#Corresponding sensor parameter: L3:1, L2:2, L1:3, R1:4, R2:5, R3:6
#Index: the corresponding sensor
def line(index):
    buf = bytearray(1)
    buf[0] = 0x1D
    i2c.write(I2caddr, buf)
    line_d = struct.unpack('b', i2c.read(I2caddr, 1))
    make = 0
    if index == 1:
        if (line_d[0] & 0x01) == 1:
            make = 1
        else:
            make = 0
    elif index == 2:
        if (line_d[0] & 0x02) == 2:
            make = 1
        else:
            make = 0
    elif index == 3:
        if (line_d[0] & 0x04) == 4:
            make = 1
        else:
            make= 0
    elif index == 4:
        if (line_d[0] & 0x08) == 8:
            make = 1
        else:
            make = 0
    elif index == 5:
        if (line_d[0] & 0x10) == 16:
            make = 1
        else:
            make = 0
    elif index == 6:
        if (line_d[0] & 0x20) == 32:
            make = 1
        else:
            make = 0
    return make

while True:
    # Maqueen Plus line-tracking sensor L1 and R1 are on the black line, sensor L2 and R2 are not
    if line(2) == 0 and line(3) == 1 and line(4) == 1 and line(5) == 0:
        motor(1, 60, 1, 60)
    # Maqueen Plus line-tracking sensor L1, R1 and L2 are on the black line, sensor R2 is not
    if line(2) == 1 and line(3) == 1 and line(4) == 1 and line(5) == 0:
        motor(1, 60, 1, 150)
    # Maqueen Plus line-tracking sensor L1 and L2 are on the black line, sensor R1 and R2 are not
    if line(2) == 1 and line(3) == 1 and line(4) == 0 and line(5) == 0:
        motor(1, 30, 1, 150)
    # Maqueen Plus line-tracking sensor R1, R2 and L1 are on the black line, sensor L2 is not
    if line(2) == 0 and line(3) == 1 and line(4) == 1 and line(5) == 1:
        motor(1, 150, 1, 60)
    # Maqueen Plus line-tracking sensor R1 and R2 are on the black line, sensor L1 and L2 are not
    if line(2) == 0 and line(3) == 0 and line(4) == 1 and line(5) == 1:
        motor(1, 150, 1, 30)