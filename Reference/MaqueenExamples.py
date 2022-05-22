
MAQUEEN_EXAMPLES = {
 "IR.py" :{"description" :"Infrared-controlled Maqueen " ,"code" :'''# Infrared-controlled Maqueen 
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import necir
I2caddr = 0x10

# Maqueen motor control
# direction:0=forward  1=back
# speed：0~255
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
    # Infrared address judgment 
    if addr == 0xbf00:
        if cmd == 0xee11:#Button 2, forward 
            motor(0, 255, 0, 255)
        if cmd == 0xe619:#Button 8, back 
            motor(1, 255, 1, 255)
        if cmd == 0xeb14:#Button 4, left 
            motor(0, 0, 0, 255)
        if cmd == 0xe916:#Button 6, right 
            motor(0, 255, 0, 0)
        if cmd == 0xea15:#Button 5, stop 
            motor(0, 0, 0, 0)   
# Initialize IR receiveing pin  and request data
necir.init(16,cb)
while True:
  pass'''},

 "Music.py": {"description": "Music", "code": '''# Music
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

# Music parameters
# music.DADADADUM
# music.ENTERTAINER
# music.PRELUDE
# music.ODE
# music.NYAN
# music.RINGTONE
# music.FUNK
# music.BLUES
# music.BIRTHDAY
# music.WEDDING
# music.FUNERAL
# music.PUNCHLINE
# music.PYTHON
# music.BADDY
# music.CHASE
# music.BA_DING
# music.WAWAWAWAA
# music.JUMP_UP
# music.JUMP_DOWN
# music.POWER_UP
# music.POWER_DOWN

import music

for i in range(3):
    music.play(music.ODE)

for i in range(3):
    music.play(music.BLUES)

while True:
    pass'''},

 "Ultrasound.py": {"description": "Ultrasonic obstacle avoiding Maqueen", "code": '''# Ultrasonic obstacle avoiding Maqueen
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import urm10
I2caddr = 0x10

# Maqueen motor control
# direction:0=forward  1=back
# speed：0~255
def motor(directionL, speedL, directionR, speedR):
    buf = bytearray(5)
    buf[0] = 0x00
    buf[1] = directionL
    buf[2] = speedL
    buf[3] = directionR
    buf[4] = speedR
    i2c.write(I2caddr, buf)

while True:

# Ultrasonic pin parameters first parameter:Echo,second parameter:Trig
# urm10.read(Echo,Trig)
    a = urm10.read(2, 1) 
    # Exclude invalid ultrasound data
    if a != 0:
        # When the distance is greater than 10cm
        if a > 10: 
            motor(0, 255, 0, 255)
        # When the distance is less than 10cm
        else: 
            motor(1, 255, 1, 255) 
            sleep(500) 
            motor(0, 255, 0, 0 
            sleep(500)'''},

 "Patrol.py": {"description": "Line-tracking Maqueen", "code": '''# Line-tracking Maqueen
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
I2caddr = 0x10

# Maqueen motor control
# direction:0=forward  1=back
# speed：0~255
def motor(directionL, speedL, directionR, speedR):
    buf = bytearray(5)
    buf[0] = 0x00
    buf[1] = directionL
    buf[2] = speedL
    buf[3] = directionR
    buf[4] = speedR
    i2c.write(I2caddr, buf)

# index：the corresponding line-tracking sensor
def Patrol(index):
    if(index == 1):
        a = pin13.read_digital()
        return a
    if(index == 2):
        a = pin14.read_digital()
        return a

while True:
    # When the left and right line-tracking sensors are not on the black line
    if Patrol(1) == 0 and Patrol(2) == 0: 
        motor(0, 200, 0, 200)
    # When the left line-tracking sensors is on the black line
    elif Patrol(1) == 1 and Patrol(2) == 0: 
        motor(0, 255, 0, 50)
    # When the right line-tracking sensors is on the black line
    elif Patrol(1) == 0 and Patrol(2) == 1: 
        motor(0, 50, 0, 255)'''},

 "Servo.py": {"description": "Maqueen servo control", "code": '''# Maqueen servo control
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
I2caddr = 0x10

# index：the corresponding servo
# angle：Servo angle
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

while True:
    # Servo 1 rotates 0 degrees
    servo(1, 0) 
    sleep(1000)
    # Servo 1 rotates 90 degrees
    servo(1, 90) 
    sleep(1000)
    # Servo 1 rotates 180 degrees
    servo(1, 180) 
    sleep(1000)'''},

 "Motor.py": {"description": "Motor control", "code": '''# Motor control
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
I2caddr = 0x10

# Maqueen motor control
# direction:0=forward  1=back
# speed：0~255
def motor(directionL, speedL, directionR, speedR):  
    buf = bytearray(5)                             
    buf[0] = 0x00
    buf[1] = directionL
    buf[2] = speedL
    buf[3] = directionR
    buf[4] = speedR
    i2c.write(I2caddr, buf)

while True:
    # Maqueen left motor forward speed 255
    motor(0, 255, 0, 0) 
    sleep(1000)
    # Maqueen right motor forward speed 255
    motor(0, 0, 0, 255) 
    sleep(1000)
    # Maqueen left motor back speed 255
    motor(1, 255, 1, 0) 
    sleep(1000)
    # Maqueen right motor back speed 255
    motor(1, 0, 1, 255) 
    sleep(1000)'''},

 "LED.py": {"description": "LED ", "code": '''# LED 
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
while True:
    # Left LED is on
    pin8.write_digital(1) 
    sleep(500)
    # Left LED is off
    pin8.write_digital(0) 
    sleep(500)
    # Right LED is on
    pin12.write_digital(1) 
    sleep(500)
    # Right LED is oFF
    pin12.write_digital(0) 
    sleep(500)'''},

 "Rgb.py": {"description": "RGB", "code": '''# RGB
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin15, 4)

while True:
    #Iterate over each LED in the strip

    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)

        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (red, green, blue)

        # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(100)'''},

}
