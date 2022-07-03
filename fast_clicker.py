from pynput import mouse
from pynput.mouse import Controller, Button
import time

mouse = Controller()
length = 120
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
  if(cycle % 5 == 0):   
    print(f'{length - cycle}s')
  
print('Done!')
