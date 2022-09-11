#---
# file: Ultrasound.py
# description: Ultrasonic obstacle avoiding Maqueen Plus
#---
# Ultrasonic obstacle avoiding Maqueen Plus
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import urm10
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

#Ultrasonic pin parameters first parameter:Echo,second parameter:Trig
#urm10.read(Echo,Trig)
    a = urm10.read(2, 1)
     # Exclude invalid ultrasound data
    if a != 0:
         # When the distance is greater than 10cm
        if a > 10:
            motor(1, 100, 1, 100)
        # When the distance is less than 10cm
        else:
            motor(2, 100, 2, 100)
            sleep(500)
            motor(1, 100, 1, 0)
            sleep(500)