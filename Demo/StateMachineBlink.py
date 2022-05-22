# StateMachineBlink - State machine demo met blink & start-knop
from microbit import *
from MaqueenApi import *
from Robot import *

def StateWachtA(S):
    if pin5.read_digital() == False:
        S.Goto(StateRed)

def StateRed(S):
    if S.NewState :
        RGB(1, 1)

    if S.StateTime(2000) :
        RGB(0,0)
        S.Goto(StateBlue)
    return

def StateBlue(S):
    if S.NewState :
        RGB(7, 7)

    if S.StateTime(2000) :
        RGB(0,0)
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
