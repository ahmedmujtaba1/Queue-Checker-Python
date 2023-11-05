import pyautogui
button_location = pyautogui.locateOnScreen('img/button.png')
button_exact_location = pyautogui.center(button_location)
print(button_exact_location)
pyautogui.moveTo(button_exact_location)