#---
# file: Grayscale value.py
# description: Value from grayscale sensor
#---
# Value from grayscale sensor
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import struct
I2caddr = 0x10

# Corresponding sensor parameter: L3:1, L2:2, L1:3, R1:4, R2:5, R3:6
# Index: the corresponding sensor
def grayscaleValue(index):
    buf = bytearray(1)
    buf[0] = 0x1E
    i2c.write(I2caddr, buf)
    grayscaleValue_d = struct.unpack('>HHHHHH', i2c.read(I2caddr, 12))
    if index == 1:
        return grayscaleValue_d[0]
    elif index == 2:
        return grayscaleValue_d[1]
    elif index == 3:
        return grayscaleValue_d[2]
    elif index == 4:
        return grayscaleValue_d[3]
    elif index == 5:
        return grayscaleValue_d[4]
    elif index == 6:
        return grayscaleValue_d[5]

while True:
    print(grayscaleValue(1))
    sleep(500)