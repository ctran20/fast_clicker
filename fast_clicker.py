from pynput import mouse
from pynput.mouse import Controller, Button

mouse = Controller()
length = 21
start = int(1/length)

for cycle in range(length):
  # Click 5k times
  for _ in range(5000):
    mouse.click(Button.left)

  # Print progress   
  print(f'{start + int(cycle/length * 100)}%')
  
print('Done!')
