# MaqueenPlusPython/Libs/MyShell.py
#
# Wrapper for limited functions of micro:bit filesystem.
#     https://microbit-micropython.readthedocs.io/en/latest/index.html
#
# Note that other micropython implementations use uos which
# has more functionality. One day, we might add this...
#     https://docs.micropython.org/en/v1.15/library/uos.html
#
from os import *

def ls():
   print(listdir())

def cat(filename):
   with open(filename) as f :
      print(f.read())

def rm(filename):
   remove(filename)

# not supported on micro:bit
#def cd(dirname):
#   chdir(dirname)

def run(filename):
   # equivalent to execfile, but that's not available on the micro:bit
   # there is still an issue on micro:bit with import / environment...
   exec(open(filename).read())