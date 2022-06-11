# StateMachineBlink - State machine demo met blink & start-knop
from microbit import *
from Robot import *

def SequenceWachtA(S):  # Sequence naam betekent de eerste state van een serie
    if S.IsNewState('SequenceWachtA') :
        Mq.RGB(1, 1)

    if pin5.read_digital() == False:
        S.Goto(StateWacht1s)

def StateWacht1s(S):
    if S.IsNewState('StateWacht1s') :
        Mq.RGB(2, 2)

    if S.StateTime(1000) :
        S.Return() # einde van sequence
    return

def SequenceHeenEnWeer(S):
    print('aap')
    if S.IsNewState('SequenceHeenEnWeer') :
        pass
    S.GoSub(SequenceWachtA, StateRijVoorwaards);

def StateRijVoorwaards(S):
    if S.IsNewState('StateRijVoorwaards') :
        Mq.RGB(4,4)
        Mq.Motors(100, 100)

    print(Mq.GetEncoders())

    if S.StateTime(5000) :
        Mq.RGB(0,0)
        Mq.Motors(0, 0)
        S.Return()
    return

# ------------------------------------------------------------------------------
# start van main
# ------------------------------------------------------------------------------
Sm = StateMachine()
Sm.Goto(SequenceHeenEnWeer)

Mq = MaqueenPlus()

print("Begin")
# voer statemachine uit zolang deze nog niet 'Done' is
while Sm.IsDone() == False:
    Sm.Takt()

print("Einde")
