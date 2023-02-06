#Author:    Aleksi Hieta
#Reference: https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
#Date:      2/5/2023
#Purpose:   GUI with Tabs and Arduino reading

#import tkinter as tk                    
#from tkinter import ttk

from tkinter import *
from tkinter.ttk import Notebook

import serial.tools.list_ports
import functools



ports = serial.tools.list_ports.comports()
serialObj = serial.Serial()


root = Tk()
root.title("Test GUI")
tabControl = Notebook(root)
  
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
  
tabControl.add(tab1, text ='Control')
tabControl.add(tab2, text ='Video')
tabControl.pack(expand = 1, fill ="both")
  
Label(tab1, text ="Control Settings").grid(column = 0, row = 0, padx = 30, pady = 30)
Label(tab2, text ="Video Settings").grid(column = 0, row = 0, padx = 30, pady = 30)

def initComPort(index):
    #currentPort = str(ports[index])
    currentPort = index
    comPortVar = str(currentPort.split(' ')[0])
    print(comPortVar)
    serialObj.port = comPortVar
    serialObj.baudrate = 9600
    serialObj.open()

comArray = ["","","","",""]

for onePort in ports:
    #comButton = Button(tab1, text=onePort, height=1, width=45, command = functools.partial(initComPort, index = ports.index(onePort)))
    comArray[ports.index(onePort)] = onePort
    #comButton.grid(row=ports.index(onePort)+1, column=0)

choice = StringVar()
choice.set("     -     ")
drop = OptionMenu(tab1, choice, *comArray)
drop.grid(row = 0, column = 2)
print(choice.get())

comButton = Button(tab1, text="Initialize", height=1, width=45, command = functools.partial(initComPort, index = choice.get()))
comButton.grid(row = 1, column = 2)



def varUpdate():
    #print(my_label.cget("text"))
    arduinoString = my_label.cget("text")

    xyz_val = arduinoString
    xyz_val = xyz_val[2:]
    #print(xyz_val)

    if(arduinoString[0] == '1'):
        x_var = xyz_val
        x_label.config(text=x_var)
    elif(arduinoString[0] == '2'):
        y_var = xyz_val
        y_label.config(text=y_var)
    elif(arduinoString[0] == '3'):
        z_var = xyz_val
        z_label.config(text=z_var)


my_text = ""
x_var = "0"
y_var = "0"
z_var = "0"

my_label = Label(tab1)
x_label = Label(tab1, text=x_var)
y_label = Label(tab1, text=y_var)
z_label = Label(tab1, text=z_var)

my_label.grid(column = 1, row = 0, padx = 30, pady = 30)
x_label.grid(column = 1, row = 1, padx = 30, pady = 0)
y_label.grid(column = 1, row = 2, padx = 30, pady = 0)
z_label.grid(column = 1, row = 3, padx = 30, pady = 0)

my_label.config(text=my_text)

def checkSerialPort():
    if serialObj.isOpen() and serialObj.in_waiting:
        recentPacket = serialObj.readline()
        my_text = recentPacket.decode('utf').rstrip('\n')
        my_label.config(text=my_text)
        varUpdate()

#root.mainloop() 
while True:
    root.update()
    checkSerialPort()