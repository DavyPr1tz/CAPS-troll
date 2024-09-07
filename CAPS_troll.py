import os
import pyautogui as pyg
from time import sleep
from random import randint

#SPAM mode sets a consistant delay rather than a random delay and can be activated by setting SPAM to true. Set SPAM delay by changing the Spam delay variable
SPAM = False
SPAM_delay = 1

#delay1-5 are the random delays. You can change these and change the possible delays the program will run
delay1 = 1
delay2 = 3
delay3 = 5
delay4 = 7
delay5 = 10

def SPAM_mode():
    sleep(SPAM_delay)

def random_delay():
    random = randint(1, 5)
    if random == 1:
        sleep(delay1)
    elif random == 2:
        sleep(delay2)
    elif random == 3:
        sleep(delay3)
    elif random == 4:
        sleep(delay4)
    elif random == 5:
        sleep(delay5)

#Checks whether SPAM is ture and chooses mode accordingly
#Change range variable to set the number of times the program loops
#If you want the program to run until you manually stop it, comment "for i in range():" and uncomment "while True" vise versa
#while True:
for i in range(20):
    pyg.press('capslock')
    if SPAM == False:
        random_delay()
    elif SPAM == True:
        SPAM_mode()