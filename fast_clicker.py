import pyautogui

for i in range(800):
  if i % 50 == 0:
    print(i)
  pyautogui.click(400, 600)