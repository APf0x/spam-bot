
# made by APfox/redfox (same person)

import pyautogui, time

time.sleep(5)
f = open("output.txt", "r")
for text in f:
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    #you can togle time sleep increase it or if you want you can take it off (only if ur pc is good or it will lag the shit out of ur PC)
    time.sleep(0.2)

#if you wanna spam only one letter or word i mean you can do what you want.

"""

time.sleep(5)
f = ("z")
while True:
    time.sleep(0.4)
    for word in f:
        pyautogui.typewrite(word)
"""

