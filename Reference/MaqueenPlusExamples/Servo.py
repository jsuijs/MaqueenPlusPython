#---
# file: Servo.py
# description: Maqueen Plus servo control
#---
# Maqueen Plus servo control
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
I2caddr = 0x10

# index:corresponds to the servo interface
# angle:Servo angle
def servo(index,angle):
    if(index == 1):
        buf =bytearray(2)
        buf[0]=0x14
        buf[1]=angle
        i2c.write(I2caddr, buf)
    if(index == 2):
        buf =bytearray(2)
        buf[0]=0x15
        buf[1]=angle
        i2c.write(I2caddr, buf)
    if(index == 3):
        buf =bytearray(2)
        buf[0]=0x16
        buf[1]=angle
        i2c.write(I2caddr, buf)

while True:
    # Servo 1 rotates 0 degrees
    servo(1, 0)
    sleep(1000)
    # Servo 1 rotates 90 degrees
    servo(1, 90)
    sleep(1000)
    # Servo 1 rotates 180 degrees
    servo(1, 180)
    sleep(1000)