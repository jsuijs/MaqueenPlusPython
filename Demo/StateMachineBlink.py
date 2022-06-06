# StateMachineBlink - State machine demo met blink & start-knop
from microbit import *
from Robot import *

def SequenceWachtA(S):
    if S.IsNewState('SequenceWachtA') :
      pass

    if pin5.read_digital() == False:
        S.Goto(StateLarge)

def StateLarge(S):
   if S.IsNewState('StateLarge') :
      display.show(Image.HEART)

   if S.StateTime(1000) :
        S.Goto(StateSmall)

def StateSmall(S):
    if S.IsNewState('StateSmall') :
       display.show(Image.HEART_SMALL)

    if S.StateTime(1000) :
        display.clear()
        S.Return()

# ------------------------------------------------------------------------------
# start van main
# ------------------------------------------------------------------------------
Sm = StateMachine(SequenceWachtA)

print("Begin")
# voer statemachine uit zolang deze nog niet 'Done' is
while Sm.IsDone() == False:
    Sm.Takt()
