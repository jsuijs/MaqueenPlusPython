#---
# file: Motor state.py
# description: Get motor speed and direction
#---
# Get motor speed and direction
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

# direction parameters:1=left motor;2=right motor
# Get the motor speed
def motorSpeed(direction):
    buf = bytearray(1)
    buf[0] = 0
    i2c.write(I2caddr, buf)
    motorSpeed_d = struct.unpack('>BBBB', i2c.read(I2caddr, 8))
    if direction == 1:
        return motorSpeed_d[1]
    elif  direction == 2:
        return motorSpeed_d[3]

# Get the motor direction
# State:0=stop;1=forward;2=reverse
def motorState(direction):
    buf = bytearray(1)
    buf[0] = 0
    i2c.write(I2caddr, buf)
    motorSpeed_d = struct.unpack('>BBBB', i2c.read(I2caddr, 8))
    if direction == 1:
        return motorSpeed_d[0]
    elif  direction == 2:
        return motorSpeed_d[2]

while True:
    motor(1, 100, 1, 0)
    print(motorSpeed(1))
    sleep(500)
    print(motorState(1))
    sleep(500)