

MAQUEENPLUS_EXAMPLES = {
 "IR.py" :{
   "description" :"Infrared-controlled Maqueen Plus" ,
   "code" :'''# Infrared-controlled Maqueen Plus
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

 "Ultrasound.py": {"description": "Ultrasonic obstacle avoiding Maqueen Plus", "code": '''# Ultrasonic obstacle avoiding Maqueen Plus
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
            sleep(500)'''},

 "Patrol.py": {"description": "Line-tracking Maqueen Plus", "code": '''# Line-tracking Maqueen Plus
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
        motor(1, 150, 1, 30)'''},

 "Servo.py": {"description": "Maqueen Plus servo control", "code": '''# Maqueen Plus servo control
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
    sleep(1000)'''},

 "Motor.py": {"description": "Motor control", "code": '''# Motor control
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
    sleep(1000)'''},

 "Rgb.py": {"description": "RGB", "code": '''# RGB
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)


from microbit import *
I2caddr = 0x10

# Each number represents a color, and color out of the RGB color range cannot be displayed.
# RGB color range 1~7
def RGB(colourL, colourR):
    buf = bytearray(3)
    buf[0] = 0x0b
    buf[1] = colourL
    buf[2] = colourR
    i2c.write(I2caddr, buf)

while True:
    # Maqueen Plus left and right RGB lights flash alternately
    for i in range(1, 8):
        RGB(i, 0)
        sleep(200)
        RGB(0, 0)
        sleep(200)
        RGB(0, i)
        sleep(200)
        RGB(0, 0)
        sleep(200)
    # Maqueen Plus left and right RGB lights show colors at the same time
    for i in range(1, 8):
        RGB(i, i)
        sleep(200)
        RGB(0, 0)
        sleep(200)'''},

 "Grayscale value.py": {"description": "Value from grayscale sensor", "code": '''# Value from grayscale sensor
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
    sleep(500)'''},

 "PID.py": {"description": "PID motor control", "code": '''# PID motor control
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

# PID parameters opeen:0 close:1
def PID(switch):
    buf = bytearray(2)
    buf[0] = 0x0A
    buf[1] = switch
    i2c.write(I2caddr, buf)

while True:
   PID(0)
   motor(1, 100, 1, 100)
   sleep(1000)
   PID(1)
   motor(1, 100, 1, 100)
   sleep(1000)'''},

 "Motor state.py": {"description": "Get motor speed and direction", "code": '''# Get motor speed and direction
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
    sleep(500)'''},

 "Motor compensation.py": {"description": "Motor compensation", "code": '''# Motor compensation
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
    sleep(1000)'''},

}


print('# based on mu\modes\examples\maqueenplus.py')
for e in  MAQUEENPLUS_EXAMPLES :
   print('# file:', e)
   print('# description:', MAQUEENPLUS_EXAMPLES[e]['description'])
   print(MAQUEENPLUS_EXAMPLES[e]['code'])

