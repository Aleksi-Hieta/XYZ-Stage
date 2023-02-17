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
  
#Label(tab1, text ="Control Settings").grid(column = 0, row = 0, padx = 30, pady = 30)
Label(tab2, text ="Video Settings").grid(column = 0, row = 0, padx = 30, pady = 30)

Button(tab1, text="Exit Program", command=root.destroy).grid(column = 3, row = 4)

def initComPort():
    #print(choice.get())
    currentPort = choice.get()
    comPortVar = str(currentPort.split(' ')[0])

    #currentPort = str(ports[index])
    #comPortVar = str(currentPort.split(' ')[0])
    #print(comPortVar)
    serialObj.port = comPortVar
    serialObj.baudrate = 9600
    serialObj.open()

comArray = ["     -     ","","","","",""]

for onePort in ports:
    #comButton = Button(tab1, text=onePort, height=1, width=45, command = functools.partial(initComPort, index = ports.index(onePort)))
    #print(ports.index(onePort))
    comArray[ports.index(onePort)+1] = onePort
    #comButton.grid(row=ports.index(onePort)+1, column=0)

#print(onePort)
choice = StringVar()
choice.set("          -          ")
drop = OptionMenu(tab1, choice, *comArray)
drop.grid(row = 1, column = 3)
#print(choice.get())

comButton = Button(tab1, text="Initialize", height=1, width=30, command = functools.partial(initComPort))
comButton.grid(row = 2, column = 3)



def varUpdate():
    arduinoString = my_label.cget("text")
    
    xyz_val = arduinoString
    xyz_val = xyz_val[2:]
    #print(xyz_val)

    #print(arduinoString[2:])
    if(arduinoString[0] == 'X'):
        if(arduinoString[3] == 'i'): #Just compares key character of string sent m 'i' n
            x_limit.config(text="X Minimum Reached!")
            #print("X Minimum Reached!")
        elif(arduinoString[3] == 'a'): #Just compares key character of string sent m 'a' x
            x_limit.config(text="X Maxmimum Reached!")
            #print("X Maximum Reached!")
    elif(arduinoString[0] == 'Y'):
        if(arduinoString[3] == 'i'): #Just compares key character of string sent m 'i' n
            y_limit.config(text="Y Minimum Reached!")
            #print("Y Minimum Reached!")
        elif(arduinoString[3] == 'a'): #Just compares key character of string sent m 'a' x
            y_limit.config(text="Y Maxmimum Reached!")
            #print("Y Maximum Reached!")
    elif(arduinoString[0] == 'Z'):
        if(arduinoString[3] == 'i'): #Just compares key character of string sent m 'i' n
            z_limit.config(text="Z Minimum Reached!")
            #print("Z Minimum Reached!")
        elif(arduinoString[3] == 'a'): #Just compares key character of string sent m 'a' x
            z_limit.config(text="Z Maxmimum Reached!")
            #print("Z Maximum Reached!")
    elif(arduinoString[0] == '1'):
        x_var = xyz_val
        x_name.config(text="X: "+x_var)
    elif(arduinoString[0] == '2'):
        y_var = xyz_val
        y_name.config(text="Y: "+y_var)
    elif(arduinoString[0] == '3'):
        z_var = xyz_val
        z_name.config(text="Z: "+z_var)
    elif(arduinoString[0] == 'B'):
        if(arduinoString[1] == '1'):
            x_button.config(text="pressed!")
            #x button pressed
        elif(arduinoString[1] == '2'):
            y_button.config(text="pressed!")
            #y button pressed
        elif(arduinoString[1] == '3'):
            z_button.config(text="pressed!")
            #y button pressed

def xyz_limit_reset():
    x_limit.config(text="X in valid range")
    y_limit.config(text="Y in valid range")
    z_limit.config(text="Z in valid range")

def xyz_button_reset():
    x_button.config(text="X button")
    y_button.config(text="Y button")
    z_button.config(text="Z button")

my_text = ""
x_var = "0"
y_var = "0"
z_var = "0"

my_label = Label(tab1)
x_name = Label(tab1, text = "X: "+x_var)
y_name = Label(tab1, text = "Y: "+y_var)
z_name = Label(tab1, text = "Z: "+z_var)

limit_label = Label(tab1, text = "Limit messages")
x_limit = Label(tab1, text = "X in valid range")
y_limit = Label(tab1, text = "Y in valid range")
z_limit = Label(tab1, text = "Z in valid range")

limit_reset = Button(tab1, text = "Reset Min & Max", command = xyz_limit_reset)
limit_reset.grid(column = 1, row = 4)

button_reset = Button(tab1, text = "Reset Button Presses", command = xyz_button_reset)
button_reset.grid(column = 2, row = 4)

x_button = Label(tab1, text = "X button")
y_button = Label(tab1, text = "Y button")
z_button = Label(tab1, text = "Z button")

my_label.grid(column = 0, row = 0, padx = 30, pady = 0)
x_name.grid(column = 0, row = 1, padx = 30, pady = 0)
y_name.grid(column = 0, row = 2, padx = 30, pady = 0)
z_name.grid(column = 0, row = 3, padx = 30, pady = 0)

limit_label.grid(column = 1, row = 0, padx = 30, pady = 0)
x_limit.grid(column = 1, row = 1, padx = 30, pady = 0)
y_limit.grid(column = 1, row = 2, padx = 30, pady = 0)
z_limit.grid(column = 1, row = 3, padx = 30, pady = 0)

x_button.grid(column = 2, row = 1, padx = 30, pady = 0)
y_button.grid(column = 2, row = 2, padx = 30, pady = 0)
z_button.grid(column = 2, row = 3, padx = 30, pady = 0)


my_label.config(text=my_text)

def checkSerialPort():
    if serialObj.isOpen() and serialObj.in_waiting:
        recentPacket = serialObj.readline()
        my_text = recentPacket.decode('utf').rstrip('\n')
        my_label.config(text=my_text)
        varUpdate()
    root.update()
    root.after(1, checkSerialPort) #Recursive call to allow for root.mainloop()

root.after(1, checkSerialPort)
root.mainloop() 
#while True:
    #root.update()
    #checkSerialPort()