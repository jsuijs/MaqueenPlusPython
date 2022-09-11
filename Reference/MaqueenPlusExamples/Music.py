#---
# file: Music.py
# description: Music
#---
# Music
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
    pass