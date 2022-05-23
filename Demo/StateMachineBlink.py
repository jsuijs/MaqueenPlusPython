# StateMachineBlink - State machine demo met blink & start-knop
from microbit import *
from MaqueenApi import *
from Robot import *

def SequenceWachtA(S):
    if S.IsNewState('SequenceWachtA') :
      pass
    if pin5.read_digital() == False:
        S.Goto(StateRed)

def StateRed(S):
    if S.IsNewState('StateRed') :
        RGB(1, 1)

    if S.StateTime(2000) :
        RGB(0,0)
        S.Goto(StateBlue)
    return

def StateBlue(S):
    if S.IsNewState('StateBlue') :
        RGB(7, 7)

    if S.StateTime(2000) :
        RGB(0,0)
        S.IsDone = True
    return

# ------------------------------------------------------------------------------
# start van main
# ------------------------------------------------------------------------------
Sm = StateMachine(SequenceWachtA)

print("Begin")
# voer statemachine uit zolang deze nog niet 'Done' is
while Sm.IsDone == False:
    Sm.Takt()

print("Einde")
