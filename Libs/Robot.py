import utime
from microbit import *
import struct
I2caddr = 0x10

class StateMachine:

   def __init__(self):
      self.TaktInterval = 0      # in ms
      self._States      = []
      self._PreNewState = True
      self._NewState    = True
      self._LastTaktMs  = 0

   # Goto - Execute NextState (leave current state)
   def Goto(self, NextState, Silent=False):
      if Silent == False : print("Goto ", end='')
      self.Return(True) # silent return

      # NextState can be a function or list of functions
      if isinstance(NextState, list) :
         for S in reversed(NextState) :
            self._States.append(S)        # add new items in reverse order
      else :
         self._States.append(NextState)   # add new item

   # Gosub - Execute ViaState and then return to NextState (leave current state)
   def GoSub(self, ViaState, NextState):
      print("GoSub ", end='')
      self.Goto(NextState, True)          # Silent Goto

      # ViaState can be a function or list of functions
      if isinstance(ViaState, list) :
         for S in reversed(ViaState) :
            self._States.append(S)        # add new items in reverse order
      else :
         self._States.append(ViaState)    # add new item


   # Return - Return to previous state in list (leave current state)
   #          note: when list is empty, IsDone() is true
   def Return(self, Silent=False):
      if Silent == False : print("Return.")
      if len(self._States) > 0 :
         self._States.pop() # drop current item (if there is one)
      self._PreNewState = True

   def Takt(self):

      if utime.ticks_ms() - (self.TaktInterval + self._LastTaktMs) < 0 :
         return # not yet time for next takt execution

      self._LastTaktMs = utime.ticks_ms()

      if len(self._States) == 0:
         print('Takt error - no more states')
         return

      # execute state
      self._PreNewState = False
      if self._NewState:
         self._StateStartMs = utime.ticks_ms()
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
      return (utime.ticks_ms() - (self._StateStartMs + Delay)) > 0

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

   # GetFloorSensors - analog read of 6 floor sensors
   # Modified version of DFRobot's grayscaleValue()
   # Returns list of 6 values, from left-most to rightmost sensor.
   # 12 bits, high values are white
   def GetFloorSensors(self):
       buf = bytearray(1)
       buf[0] = 0x1E
       i2c.write(I2caddr, buf)
       return struct.unpack('>HHHHHH', i2c.read(I2caddr, 12))

   # Motors - set motors to speeds specified, negative = reverse
   def Motors(self, SpeedL, SpeedR):

      #print("Motors", SpeedL, SpeedR)

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

   # DistanceSpeedLR - drive arc for <Distance> mm, no correction.
   def DistanceSpeedLR(self, SpeedL, SpeedR, Distance):
      self.KeepHeading = False
      self.Motors(SpeedL, SpeedR)
      CurrentL, CurrentR = self.GetEncoders()
      self.EndPoint = CurrentL + CurrentR + Distance * 1.17 # ticks to mm
      print("Distance :", self.EndPoint, CurrentL, CurrentR, Distance)

   # DistanceSpeed - drive straight for <Distance> mm, correct for heading deviation
   def DistanceSpeed(self, Speed, Distance):

      CurrentL, CurrentR = self.GetEncoders()
      self.SpeedSp   = Speed
      self.HeadingSp = CurrentL - CurrentR
      self.EndPoint  = CurrentL + CurrentR + Distance * 1.17 # ticks to mm
      self.KeepHeading = True

      print("Distance :", self.EndPoint, CurrentL, CurrentR, Distance)
      self.Motors(self.SpeedSp, self.SpeedSp)

   # IsDone - return true if requested distance had been traveled
   def IsDone(self):
      CurrentL, CurrentR = self.GetEncoders()

      if self.KeepHeading :
         CurHeading = CurrentL - CurrentR
         Correction = (self.HeadingSp - CurHeading) * 5.0
         self.Motors(self.SpeedSp + Correction, self.SpeedSp - Correction)
         #print("Correction", Correction)

      return (CurrentL + CurrentR) >= self.EndPoint
