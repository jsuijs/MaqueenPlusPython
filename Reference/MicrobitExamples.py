

MICROBIT_EXAMPLES = {
        "Hello World.py":{"description":"Hello world demo to print a word","code":'''# Hello world.py
from microbit import *
display.scroll("Hello, World!")'''},

        "Happy Image.py":{"description":"Show smile face over led matrix","code":'''# Happy Image.py
from microbit import *
display.show(Image.HAPPY)'''},

        "Button.py": {"description": "Get how many times button pressed", "code": '''from microbit import *

sleep(10000)
display.scroll(str(button_a.get_presses()))'''},

        "Music.py": {"description": "Play Nyan Nyan from meow planet", "code": '''import music
music.play(music.NYAN)'''},

        "NeoPixel.py": {"description": "Test over robotbit neopixel", "code": '''
from microbit import *

import neopixel
my_variable = 0
np = neopixel.NeoPixel(pin16, 4)

np[0] = (170, 0, 0)
np[1] = (4, 144, 220)
np[2] = (170, 170, 0)
np[3] = (0, 170, 0)
np.show()'''},

        "Servo Sweep.py": {"description": "Servo Sweep on channel S1~S4", "code": '''
from microbit import *
import robotbit

while True:
    robotbit.servo(0, 0)
    robotbit.servo(1, 0)
    robotbit.servo(2, 0)
    robotbit.servo(3, 0)
    sleep(2*1000)
    robotbit.servo(0, 180)
    robotbit.servo(1, 180)
    robotbit.servo(2, 180)
    robotbit.servo(3, 180)
    sleep(2*1000)'''},

    }