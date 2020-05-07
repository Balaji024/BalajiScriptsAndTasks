#pip install pyautogui===0.9.0
import pyautogui

pyautogui.position()
pyautogui.moveTo(10,10, duration=1.5)
pyautogui.click(10,10)
pyautogui.doubleClick(10,10)#rightClick, middleClick
pyautogui.click(727, 64); pyautogui.typewrite('Hi Balaji', interval=0.2);pyautogui.hotkey('ctrl', 's')
pyautogui.screenshot()
