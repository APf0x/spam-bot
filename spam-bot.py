# made by APfox/redfox (same person)
# Contribs: MatMasIt
import pyautogui
import time

#  <config>
config = {
    "initialSleep": 5,
    "text": open("input.txt", "r").readlines(),
    "submitKey": "enter",
    "intervalSleep": 0.2,  # you can set it to 0, too if your pc is powerful enough
    "spamMode": 0  # 0 -> lines, 1 -> words , 2 -> characters
}
# </config>
time.sleep(config["initialSleep"])
for line in config["text"]:
    spamList = []
    if config["spamMode"] == 0:
        spamList = [line]
    elif config["spamMode"] == 1:
        spamList = line.split()
    elif config["spamMode"] == 2:
        spamList = list(line)
    for element in spamList:
        pyautogui.typewrite(element)
        pyautogui.press(config["submitKey"])
        time.sleep(config["intervalSleep"])
