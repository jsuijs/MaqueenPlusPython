import utime

def StateDone(S):
   S.Done = True


class StateMachine:

   def __init__(self):
      self.ActiveState = StateDone
      self.NewState = True
      self.Done = False
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
