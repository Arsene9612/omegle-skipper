import pyautogui
import time
import pyfiglet
from colorama import Fore, Style

banner=pyfiglet.figlet_format("Omegle Skipper")
print(Fore.BLUE+banner)

choices=("[1] Infinite skips \n[2] Specified amount of skips")
print(choices)
choice=input("\nChoice:")

def whileLoop():
    message=input("Enter a message: ")
    x=True
    try:
        print("starts in 10 seconds")
        while x:
            time.sleep(10)
            pyautogui.write(message)
            pyautogui.press("enter")
            pyautogui.press("esc")
            pyautogui.press("esc")
    except KeyboardInterrupt:
        x=False

def forLoop():
    skips=int(input("How many times do you want so skip? NOT gonna be 100%% accurate "))
    message=input("Enter a message: ")
    print("starts in 10 seconds")
    for skip in range(skips):
        time.sleep(10)
        pyautogui.write(message)
        pyautogui.press("enter")
        pyautogui.press("esc")
        pyautogui.press("esc")


if choice == "1":
    whileLoop()
elif choice =="2":
    forLoop()
else:
    print(Fore.RED+"bye nig")
    exit(1)

