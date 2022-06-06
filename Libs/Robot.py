import utime
from microbit import *
import struct
I2caddr = 0x10

class StateMachine:

   def __init__(self, StartState):
      self._States      = [StartState]
      self._PreNewState = True
      self._NewState    = True

   # Goto - Execute NextState (leave current state)
   def Goto(self, NextState):
      print("Goto ", end='')
      self._States[-1]  = NextState # replace current state
      self._PreNewState = True

   # Gosub - Execute ViaState and then return to NextState (leave current state)
   def GoSub(self, ViaState, NextState):
      print("GoSub ", end='')
      self._States[-1]  = NextState # replace current state
      self._PreNewState = True
      self._States.append(ViaState) # add via-state on top

   # Add - Add state to the end of list (after all other states are executed)
   def Add(self, AddState):
      print("Add.")
      self._States.insert(0, AddState)
      self._PreNewState = True

   # Return - Return to previous state in list (leave current state)
   #          note: when list is empty, IsDone() is true
   def Return(self):
      print("Return.")
      self._States.pop()
      self._PreNewState = True

   def Takt(self):
      if len(self._States) == 0:
         print('Takt error - no more states')
         return

      # execute state
      self._PreNewState = False
      if self._NewState:
         self._StartMs = utime.ticks_ms()
      self._States[-1](self)
      self._NewState = self._PreNewState

   # IsNewState - check if this is first call to state, print Statename if so.
   def IsNewState(self, StateName):
      if self._NewState:
         print("NewState", StateName)
      return self._NewState

   # IsDone - returns true when all states are executed
   def IsDone(self):
      return len(self._States) == 0

   # StateTime - returns true when we're more than Delay in the current state
   def StateTime(self, Delay):
      return (utime.ticks_ms() - (self._StartMs + Delay)) > 0

class MaqueenPlus:

   def __init__(self):
      pass

   # --------------------------------------------------------------------------
   # From MaqueenApi.py

   # Each number represents a color, and color out of the RGB color range cannot be displayed.
   # RGB color range 1~7
   def RGB(self, colourL, colourR):
       buf = bytearray(3)
       buf[0] = 0x0b
       buf[1] = colourL
       buf[2] = colourR
       i2c.write(I2caddr, buf)

   # Maqueen Plus motor control
   # direction:1 forward  2 back
   # speed:0~255
   def motor(self, directionL, speedL, directionR, speedR):
       buf = bytearray(5)
       buf[0] = 0x00
       buf[1] = directionL
       buf[2] = int(speedL)
       buf[3] = directionR
       buf[4] = int(speedR)
       i2c.write(I2caddr, buf)

   def GetEncoders(self):
       buf = bytearray(1)
       buf[0] = 0x04
       i2c.write(I2caddr, buf)
       return struct.unpack('>HH', i2c.read(I2caddr, 4))

   # /From MaqueenApi.py
   # --------------------------------------------------------------------------

   def Motors(self, SpeedL, SpeedR):

      print("Motors", SpeedL, SpeedR)

      if SpeedL > 0 :
         DirL     = 1
      else :
         DirL     = 2
         SpeedL   = -SpeedL

      if SpeedR > 0 :
         DirR     = 1
      else:
         DirR     = 2
         SpeedR   = -SpeedR

      self.motor(DirL, SpeedL, DirR, SpeedR)

   def ToDoDistance(self, SpeedL, SpeedR, Distance):
      self.Motors(SpeedL, SpeedR)
      CurrentL, CurrentR = self.GetEncoders()
      self.EndPoint = CurrentL + CurrentR + Distance * 1.17 # ticks to mm
      print("Distance :", self.EndPoint, CurrentL, CurrentR, Distance)

   def ToDoIsDone(self):
      CurrentL, CurrentR = self.GetEncoders()
      return (CurrentL + CurrentR) >= self.EndPoint


   def Distance(self, Speed, Distance):

      CurrentL, CurrentR = self.GetEncoders()
      self.SpeedSp   = Speed
      self.HeadingSp = CurrentL - CurrentR
      self.EndPoint  = CurrentL + CurrentR + Distance * 1.17 # ticks to mm

      print("Distance :", self.EndPoint, CurrentL, CurrentR, Distance)

      self.Motors(self.SpeedSp, self.SpeedSp)

   def IsDone(self):
      CurrentL, CurrentR = self.GetEncoders()
      CurHeading = CurrentL - CurrentR
      Correction = (self.HeadingSp - CurHeading) * 5.0
      self.Motors(self.SpeedSp + Correction, self.SpeedSp - Correction)

      print("Correction", Correction)

      return (CurrentL + CurrentR) >= self.EndPoint
