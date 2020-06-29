import os
import sys
import logging
from datetime import datetime
import argparse
import platform
import subprocess
try:
   from config import *
except ImportError:
  print("Configuration file does not exist, you may have issues down the line")
#-----------------------------
# XentInterpret 2.0.0
# copyright 2020, 17lwinn


parser = argparse.ArgumentParser(prog='python3 main.py', description='XenText... remastered')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0', help='view the CLI version')
parser.add_argument('-r', '--run', metavar='script/path', help='Run your XenText scripts');
args = parser.parse_args()

if args.run:
  if DISABLE_SCRIPT_EXECUTION == "false":
      scriptname = args.run
      os.system("python3  " + PARSER_LOCATION + scriptname)
      exit()
    
  if DISABLE_SCRIPT_EXECUTION == "true":
    print("Remote script execution has been disabled, please change DISABLE_SCRIPT_EXECUTION to false")
    print("")


print("XenText interpreter")
print(platform.system(), platform.architecture())
print("type xenText code here and type run() to execute")
print("or exit() to exit the interpreter")
def main():
  while True:
    cliprompt()
        
def cliprompt():
      code = input(">>> ")
      
      if code == "run()":
        run()
        return
      
      
      if code == "forcerun()":
        forcerun()
        return
      
      if code == "exit()":
        exit()
        
      f = open(".temp.xt", "a")
      f.write(code + "\n")
      f.close()
      
      if code == "moomoo()":
        moomoo()
        


def run():
  file = ".temp.xt"
  try:
    os.system("python3 xent.py " + file)
    os.remove(".temp.xt")
  except:
    print("An error occured while evaluating the code!")

def forcerun():
  file = ".temp.xt"
  try:
    os.system("python3 xent.py " + file)
  except:
    print("An error occured while evaluating the code!")


def exit():
  try:
    os.unlink(".temp.xt")
  except:
    0
  finally:
    print("exiting...")
    sys.exit()

def moomoo():
  os.unlink(".temp.xt")
  print('\|/          (__)    ')
  print('     `\------(oo)    ')
  print('       ||    (__)    ')
  print('       ||w--||    \|/')



if __name__ == '__main__': 
  main()
