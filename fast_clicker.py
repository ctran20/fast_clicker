import re
from pynput import mouse
from pynput.mouse import Controller, Button
import time

def print_time(sec):
  mins = sec//60
  secs = sec - mins * 60
  
  if(sec > 60):
    if secs % 10 == 0:
      print(f'{mins}m {secs}s')
  elif(secs % 5 == 0):
    print(f'{sec}s')

mouse = Controller()
length = 30
start = int(1/length)

for cycle in range(length):
  # Click 5k times
  for _ in range(60):
    mouse.click(Button.left)
    mouse.click(Button.left)
    mouse.click(Button.left)
    mouse.click(Button.left)
    mouse.click(Button.left)
    time.sleep(0.001)

  # Print progress
  print_time(length-cycle)
  
print('Done!')
