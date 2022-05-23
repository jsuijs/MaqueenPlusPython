# StateMachineBlink - State machine demo met blink & start-knop
from microbit import *
from MaqueenApi import *
from Robot import *

def SequenceWachtA(S):  # Sequence naam betekent de eerste state van een serie
    if S.IsNewState('SequenceWachtA') :
        RGB(1, 1)

    if pin5.read_digital() == False:
        S.Goto(StateWacht1s)

def StateWacht1s(S):
    if S.IsNewState('StateWacht1s') :
        RGB(2, 2)

    if S.StateTime(1000) :
        S.IsDone = True # einde van sequence
    return

def SequenceHeenEnWeer(S):
    if S.IsNewState('SequenceHeenEnWeer') :
        pass
    S.GoSub(SequenceWachtA, StateRijVoorwaards);

def StateRijVoorwaards(S):
    if S.IsNewState('StateRijVoorwaards') :
        RGB(4,4)
        motor(1, 100, 1, 100)

    print(GetEncoders())

    if S.StateTime(5000) :
        RGB(0,0)
        motor(1, 0, 1, 0)
        S.IsDone = True
    return

# ------------------------------------------------------------------------------
# start van main
# ------------------------------------------------------------------------------
Sm = StateMachine(SequenceHeenEnWeer)

print("Begin")
# voer statemachine uit zolang deze nog niet 'Done' is
while Sm.IsDone == False:
    Sm.Takt()

print("Einde")
