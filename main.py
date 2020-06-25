import os
import sys

def main():
  while True:
        cliprompt()
        
def cliprompt():
      
      print("XenText interpreter 1.0.0")
      
      code = input(">>> ")
      
      if code == "run()":
        run()
        return
      
      if code == "exit()":
        exit()
      f = open(".temp.xt", "a")
      f.write(code + "\n")
      f.close()
      

def run():
  file = ".temp.xt"
  try:
    os.system("python3 xent.py " + file)
    os.remove(".temp.xt")
  except:
    print("An Error occured while evaluating the code!")

def exit():
  try:
    os.unlink(".temp.xt")
  except:
    0
  finally:
    print("exiting...")
    sys.exit()

if __name__ == '__main__': 
  main()