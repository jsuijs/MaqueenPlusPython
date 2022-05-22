# StateMachineBlink - State machine demo met blink & start-knop
from microbit import *
from MaqueenApi import *
from Robot import *

def StateWachtA(S):
    if S.NewState :
        RGB(1, 1)

    if pin5.read_digital() == False:
        S.Goto(StateWacht1s)

def StateWacht1s(S):
    if S.NewState :
        RGB(2, 2)

    if S.StateTime(1000) :
        S.Goto(RijVoorwaards)
    return

def RijVoorwaards(S):
    if S.NewState :
        RGB(4,4)
        motor(1, 100, 1, 100)

    print(GetEncoders())

    if S.StateTime(5000) :
        RGB(0,0)
        motor(1, 0, 1, 0)
        S.Goto(StateDone)
    return

# ------------------------------------------------------------------------------
# start van main
# ------------------------------------------------------------------------------
Sm = StateMachine()

Sm.Goto(StateWachtA)

print("Begin")
# voer statemachine uit zolang deze nog niet 'Done' is
while Sm.Done == False:
    Sm.Takt()

print("Einde")
