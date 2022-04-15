import pyautogui
import time
import sys

def program():
    a = input("Do you want to spam?")
    def menu():
        c = input("Do you want to 1) use your own text, or 2) use preset text?")
        if c == '1':
            custom()
        else:
            preset()
    def start():
        if a == 'y':
            menu()
        else:
            sys.exit()
    def preset():
        print("PLEASE SWITCH TO YOUR TEXT BOX NOW")
        x = open("jazz.txt", 'r')
        time.sleep(5)
        for word in x:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
        restart()
    def custom():
        x = input("What is the text you want to spam?")
        y = input("How many times do you want to spam?")
        w = int(y)
        print("PLEASE SWITCH TO YOUR TEXT BOX NOW")
        time.sleep(5)
        for z in range(0, w):
            pyautogui.typewrite(x)
            pyautogui.press("enter")
        restart()
    def restart():
        q = input("do you want to repeat")
        if q == 'y':
            program()
        else:
			sys.exit()
    start()
program()
