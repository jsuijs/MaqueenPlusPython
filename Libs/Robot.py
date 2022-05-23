import utime

class StateMachine:

   def __init__(self, StartState):
      self._ActiveState = StartState
      self._NewState    = True
      self._SubS        = None
      self.IsDone       = False
      pass

   def IsNewState(self, StateName):
      if self._NewState:
         print("NewState", StateName)
      return self._NewState

   def Goto(self, NextState):
      print("Goto ", end='')
      self._StartMs     = utime.ticks_ms()
      self._PreNewState = True
      self._ActiveState = NextState

   def GoSub(self, ViaState, NextState):
      print("GoSub ", end='')
      self._SubS        = StateMachine(ViaState)
      self._NextState   = NextState

   def Takt(self):
      if self._SubS != None:
         # handle sub-statemachine until it completes
         self._SubS.Takt()
         if self._SubS.IsDone == False:
            return

         # Sub Done -> next for this StateMachine
         self._SubS = None;
         self.Goto(self._NextState)
         self._NewState = True # required to start NextState properly

      # Work on this StateMachine
      self.IsDone = False
      self._PreNewState = False
      self._ActiveState(self)
      self._NewState = self._PreNewState
      return self.IsDone

   def StateTime(self, Delay):
      return (utime.ticks_ms() - (self._StartMs + Delay)) > 0
