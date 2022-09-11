#---
# file: Rgb.py
# description: RGB
#---
# RGB
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
        sleep(200)