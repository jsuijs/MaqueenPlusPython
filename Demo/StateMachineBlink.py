# StateMachineBlink - State machine demo met blink & start-knop
from microbit import *
from MaqueenApi import *
import utime

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

def StateDone(S):
   S.Done = True

class StateMachine:

   def __init__(self):
      self.ActiveState = StateDone
      self.NewState = True
      pass

   def Goto(self, NextState):
      print("Goto", NextState)
      self.StartMs = utime.ticks_ms()
      self.PreNewState = True
      self.ActiveState = NextState

   def Takt(self):
        self.Done = False
        self.PreNewState = False
        self.ActiveState(self)
        self.NewState = self.PreNewState
        return self.Done

   def StateTime(self, Delay):
      return (utime.ticks_ms() - (self.StartMs + Delay)) > 0

# ------------------------------------------------------------------------------
# start van main
# ------------------------------------------------------------------------------
Sm = StateMachine()

Running = True
Sm.Goto(StateWachtA)

print("Begin")
while Running:

   if Sm.Takt() :
      # done
      Running = False

print("Einde")
