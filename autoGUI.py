import pyautogui, time


time.sleep(5)
# TO create a folder in google drive
pyautogui.moveTo(79,208)
pyautogui.click()
pyautogui.moveTo(154,208)
pyautogui.click()
pyautogui.write('Hello world!')
pyautogui.click(804,457)

# To delete a folder in google drive
pyautogui.moveTo(1100,580)
pyautogui.click(button='right')
time.sleep(5)
pyautogui.moveTo(895,684)
pyautogui.click()


