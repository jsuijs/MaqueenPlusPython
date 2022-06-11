# StateMachineBlink - State machine demo met blink & start-knop
from microbit import *
from Robot import *

def SequenceWachtA(S):  # Sequence naam betekent de eerste state van een serie
    if S.IsNewState('SequenceWachtA') :
        Mq.RGB(1, 1)
        Mq.Motors(0, 0)

    if pin5.read_digital() == False:
        S.Goto(StateWacht1s)

def StateWacht1s(S):
    if S.IsNewState('StateWacht1s') :
        Mq.RGB(2, 2)

    if S.StateTime(1000) :
        S.Return() # einde van sequence

def StateRijVoorwaards(S):
    if S.IsNewState('StateRijVoorwaards') :
        Mq.RGB(4, 4)
        Mq.DistanceSpeed(100, 1500)

    if Mq.IsDone() :
        Mq.Motors(0, 0)
        S.Return()

def StateDraai180(S):
    if S.IsNewState('StateDraai180') :
        Mq.DistanceSpeedLR(40, -40, 162)

    if Mq.IsDone() :
        Mq.Motors(0, 0)
        S.Return()

# ------------------------------------------------------------------------------
# start van main
# ------------------------------------------------------------------------------
Mq = MaqueenPlus()
Sm = StateMachine()

print("Begin")
Sm.GoSub(SequenceWachtA, [StateRijVoorwaards, StateDraai180, StateRijVoorwaards])

while Sm.IsDone() == False:
    Sm.Takt()

print("Einde")
