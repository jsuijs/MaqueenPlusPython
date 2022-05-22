from microbit import *
import struct
I2caddr = 0x10

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

# PID parameters opeen:0 close:1
def PID(switch):
    buf = bytearray(2)
    buf[0] = 0x0A
    buf[1] = switch
    i2c.write(I2caddr, buf)

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

# Each number represents a color, and color out of the RGB color range cannot be displayed.
# RGB color range 1~7
def RGB(colourL, colourR):
    buf = bytearray(3)
    buf[0] = 0x0b
    buf[1] = colourL
    buf[2] = colourR
    i2c.write(I2caddr, buf)

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


def GetEncoders():
    buf = bytearray(1)
    buf[0] = 0x04
    i2c.write(I2caddr, buf)
    return struct.unpack('>HH', i2c.read(I2caddr, 4))

