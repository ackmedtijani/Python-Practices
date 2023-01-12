import pyautogui , os
os.chdir("C:\\Users\\pc\\Pictures")

im = pyautogui.screenshot()
im.show()
im.save("tijani.bmp")