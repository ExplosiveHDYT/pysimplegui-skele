#imports
from PySimpleGUI import Text, Window, Button, WIN_CLOSED, InputText, Submit, popup, Input, theme
from os import popen, system
from time import sleep
#dark mode because I like it
theme("Black")

#horribly scripted instructions
def PySuperSimpleGUI_instructions():
    print("welcome to PySuperSimpleGUI \n an even easier version of PySimpleGui \n the functions/ variables are GUI, PySuperSimpleGUI_instructions() and X_Button()")

#adds an X button
def X_Button():
    if event == WIN_CLOSED or event == "Exit":
        while True:
            break

