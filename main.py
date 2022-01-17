from email import message
import pyautogui
import time
import pyperclip

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

friend_icon = pyautogui.locateOnScreen("friend1.png")
print(friend_icon)
pyautogui.moveTo(friend_icon)
pyautogui.click()
pyautogui.move(0,55)
pyautogui.click()

search_icon = pyautogui.locateOnScreen("search.png")
pyautogui.moveTo(search_icon)
pyautogui.click()
my_write("KKT")
time.sleep(1)
pyautogui.press("Enter")
my_write("Test message")
pyautogui.press("Enter")
w = pyautogui.getActiveWindow()
w.close()
time.sleep(1)
pyautogui.press("down")
pyautogui.press("down")
pyautogui.press("Enter")
my_write("Test message")
pyautogui.press("Enter")
w = pyautogui.getActiveWindow()
w.close()

