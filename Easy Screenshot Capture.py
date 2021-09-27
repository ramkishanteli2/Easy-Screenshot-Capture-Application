import numpy as np 
import pyautogui
import cv2
from PIL import Image,ImageChops
from tkinter import *
k=1
def Screenshot():
    global k
    image = pyautogui.screenshot()
    url = urlinput.get("1.0","end-1c")
    image.save(url+"\\"+f"{k}.jpg",'JPEG')
    k+=1

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")

root = Tk()
l = Label(root, text = "Enter URL to Save")
l.pack()
urlinput = Text(root,height = 2, width = 20)
urlinput.pack()
btn = Button(root,text="Take Screenshot",command=lambda:Screenshot())

btn.pack()

root.mainloop()