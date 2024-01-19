import time
import pyautogui as p

time.sleep(2.5)
k = open("twi.txt","r")
a = [x for x in k.read().split("\n") if x != ""]
for i in a:
    for j in range(0, len(i.split()), 10):
        p.press(i)
        p.typewrite(" ".join((i.split()[j:j+10])) + " ")
        p.press('enter')
        time.sleep(0.3)




