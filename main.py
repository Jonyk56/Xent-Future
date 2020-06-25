import os
import sys

def main():
  while True:
        cliprompt()
    
def cliprompt():
      print("Xenterpret 1.0")
      print("beta edition, by 17lwinn")
      
      code = input(">>> ")
      
      f = open("temp.xt", "w")
      f.write(code)
      f.close()
        
      f = open("temp.xt", "r")
      exec(f.read())
      os.remove("temp.xt")
      
if __name__ == '__main__': main()