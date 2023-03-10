#Author:    Aleksi Hieta
#Reference: https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
#Date:      2/22/2023
#Purpose:   GUI with Tabs and Arduino reading

#import tkinter as tk                    
#from tkinter import ttk

from tkinter import *
from tkinter.ttk import Notebook

import serial
import serial.tools.list_ports
import functools

#motor_driver.write(str.encode("\r\n\r\n")) # Send wake up command to grbl
#motor_driver.write(str.encode(arduino_in)) # Send command to grbl/firmware

ports = serial.tools.list_ports.comports()
serialObj1 = serial.Serial()
serialObj2 = serial.Serial()
serialObj3 = serial.Serial()


root = Tk()
root.title("Test GUI")
tabControl = Notebook(root)
  
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)
tabControl.add(tab1, text ='Initialize')  
tabControl.add(tab2, text ='Control')
tabControl.add(tab3, text ='Video')
tabControl.add(tab4, text ='Temp')
tabControl.pack(expand = 1, fill ="both")
  
#Label(tab1, text ="Control Settings").grid(column = 0, row = 0, padx = 30, pady = 30)
Label(tab3, text ="Video Settings").grid(column = 0, row = 0, padx = 30, pady = 30)

Button(tab3, text="Exit Program", command=root.destroy).grid(column = 0, row = 1)

#Below are key functions for sending code to the stage and initializing serial communication
master_gcode = ""
def send_gcode():
    global master_code
    print(master_gcode)
    #serialObj1.write(str.encode(master_gcode))

def initComPort1():
    #print(choice.get())
    currentPort = choice1.get()
    comPortVar = str(currentPort.split(' ')[0])

    serialObj1.port = comPortVar
    serialObj1.baudrate = 9600
    serialObj1.open()

def closeComPort1():
    serialObj1.close()

def initComPort2():
    #print(choice.get())
    currentPort = choice2.get()
    comPortVar = str(currentPort.split(' ')[0])

    serialObj2.port = comPortVar
    serialObj2.baudrate = 9600
    serialObj2.open()

def closeComPort2():
    serialObj2.close()

def initComPort3():
    #print(choice.get())
    currentPort = choice3.get()
    comPortVar = str(currentPort.split(' ')[0])

    serialObj3.port = comPortVar
    serialObj3.baudrate = 9600
    serialObj3.open()

def closeComPort3():
    serialObj3.close()


#Initialize Tab1 Elements
stage_frame = LabelFrame(tab1, padx=10, pady=10, text="Stage Initialization")
stage_frame.grid(row=0, column=0, padx=10, pady=10) 
camera_frame = LabelFrame(tab1, padx=10, pady=10, text="Camera Initialization")
camera_frame.grid(row=1, column=0, padx=10, pady=10) 
control_frame = LabelFrame(tab1, padx=10, pady=10, text="Controls Initialization")
control_frame.grid(row=2, column=0, padx=10, pady=10) 

port_label1 = Label(stage_frame, text="Port:")
port_label1.grid(row=0, column=0, padx=10, pady=10) 
port_label2 = Label(camera_frame, text="Port:")
port_label2.grid(row=0, column=0, padx=10, pady=10)
port_label3 = Label(control_frame, text="Port:")
port_label3.grid(row=0, column=0, padx=10, pady=10)

baud_label1 = Label(stage_frame, text="Baudrate:")
baud_label1.grid(row=1, column=0, padx=10, pady=10) 
baud_label2 = Label(camera_frame, text="Baudrate:")
baud_label2.grid(row=1, column=0, padx=10, pady=10) 
baud_label3 = Label(control_frame, text="Baudrate:")
baud_label3.grid(row=1, column=0, padx=10, pady=10) 

#Initialize Tab2 Elements
gcode_frame = LabelFrame(tab2, padx=10, pady=10, text="Direct G-Code")
gcode_frame.grid(row=0, column=1, padx=5, pady=10, sticky=N) #Sticky = North for making it at top of screen

jog_frame = LabelFrame(tab2, padx=10, pady=10, text="Directional Steps")
jog_frame.grid(row=0, column=0, padx=5, pady=10) 

button_jog_frame = LabelFrame(jog_frame, padx=10, pady=10)
button_jog_frame.grid(row=0, column=0, padx=10, pady=10) 

speed_jog_frame = LabelFrame(jog_frame, padx=10, pady=10, text="Directional Step Speeds")
speed_jog_frame.grid(row=1, column=0, padx=5, pady=10) 


#   Note: Format for G-Code
#   "G21 G91 G01 Z-0.002 F6\n"

#   Note: Alternative scaling method, for loop() with 10 or 100 iterations

#How to get Speed
    #X_Y_axis_speed_entry.get()
    #Z_axis_speed_entry.get()



def gcode_x_pos_100():
    global master_gcode
    master_gcode = "G21 G91 G01 X-0.2 F6\n"
    send_gcode()
def gcode_x_pos_10():
    global master_gcode
    master_gcode = "G21 G91 G01 X-0.02 F6\n"
    send_gcode()
def gcode_x_pos_1():
    global master_gcode
    master_gcode = "G21 G91 G01 X-0.002 F6\n"
    send_gcode()
def gcode_x_neg_1():
    global master_gcode
    master_gcode = "G21 G91 G01 X0.002 F6\n"
    send_gcode()
def gcode_x_neg_10():
    global master_gcode
    master_gcode = "G21 G91 G01 X0.02 F6\n"
    send_gcode()
def gcode_x_neg_100():
    global master_gcode
    master_gcode = "G21 G91 G01 X0.2 F6\n"
    send_gcode()

def gcode_y_pos_100():
    global master_gcode
    master_gcode = "G21 G91 G01 Y0.2 F6\n"
    send_gcode()
def gcode_y_pos_10():
    global master_gcode
    master_gcode = "G21 G91 G01 Y0.02 F6\n"
    send_gcode()
def gcode_y_pos_1():
    global master_gcode
    master_gcode = "G21 G91 G01 Y0.002 F6\n"
    send_gcode()
def gcode_y_neg_1():
    global master_gcode
    master_gcode = "G21 G91 G01 Y-0.002 F6\n"
    send_gcode()
def gcode_y_neg_10():
    global master_gcode
    master_gcode = "G21 G91 G01 Y-0.02 F6\n"
    send_gcode()
def gcode_y_neg_100():
    global master_gcode
    master_gcode = "G21 G91 G01 Y-0.2 F6\n"
    send_gcode()

def gcode_z_pos_100():
    global master_gcode
    master_gcode = "G21 G91 G01 Z0.2 F6\n"
    send_gcode()
def gcode_z_pos_10():
    global master_gcode
    master_gcode = "G21 G91 G01 Z0.02 F6\n"
    send_gcode()
def gcode_z_pos_1():
    global master_gcode
    master_gcode = "G21 G91 G01 Z0.002 F6\n"
    send_gcode()
def gcode_z_neg_1():
    global master_gcode
    master_gcode = "G21 G91 G01 Z-0.002 F6\n"
    send_gcode()
def gcode_z_neg_10():
    global master_gcode
    master_gcode = "G21 G91 G01 Z-0.02 F6\n"
    send_gcode()
def gcode_z_neg_100():
    global master_gcode
    master_gcode = "G21 G91 G01 Z-0.002 F6\n"
    send_gcode()

x_direction_label = Label(button_jog_frame, text="X")
x_pos_100 = Button(button_jog_frame, text="+100", command = gcode_x_pos_100)
x_pos_10 = Button(button_jog_frame, text="+10", command = gcode_x_pos_10)
x_pos_1 = Button(button_jog_frame, text="+1", command = gcode_x_pos_1)
x_neg_1 = Button(button_jog_frame, text="-1", command = gcode_x_neg_1)
x_neg_10 = Button(button_jog_frame, text="-10", command = gcode_x_neg_10)
x_neg_100 = Button(button_jog_frame, text="-100", command = gcode_x_neg_100)
x_direction_label.grid(row=0, column=0, padx=10, pady=2)
x_pos_100.grid(row=1, column=0, padx=10, pady=2)
x_pos_10.grid(row=2, column=0, padx=10, pady=2)
x_pos_1.grid(row=3, column=0, padx=10, pady=2)
x_neg_1.grid(row=4, column=0, padx=10, pady=2)
x_neg_10.grid(row=5, column=0, padx=10, pady=2)
x_neg_100.grid(row=6, column=0, padx=10, pady=2)

y_direction_label = Label(button_jog_frame, text="Y")
y_pos_100 = Button(button_jog_frame, text="+100", command = gcode_y_pos_100)
y_pos_10 = Button(button_jog_frame, text="+10", command = gcode_y_pos_10)
y_pos_1 = Button(button_jog_frame, text="+1", command = gcode_y_pos_1)
y_neg_1 = Button(button_jog_frame, text="-1", command = gcode_y_neg_1)
y_neg_10 = Button(button_jog_frame, text="-10", command = gcode_y_neg_10)
y_neg_100 = Button(button_jog_frame, text="-100", command = gcode_y_neg_100)
y_direction_label.grid(row=0, column=1, padx=10, pady=2)
y_pos_100.grid(row=1, column=1, padx=10, pady=2)
y_pos_10.grid(row=2, column=1, padx=10, pady=2)
y_pos_1.grid(row=3, column=1, padx=10, pady=2)
y_neg_1.grid(row=4, column=1, padx=10, pady=2)
y_neg_10.grid(row=5, column=1, padx=10, pady=2)
y_neg_100.grid(row=6, column=1, padx=10, pady=2)

z_direction_label = Label(button_jog_frame, text="Z")
z_pos_100 = Button(button_jog_frame, text="+100", command = gcode_z_pos_100)
z_pos_10 = Button(button_jog_frame, text="+10", command = gcode_z_pos_10)
z_pos_1 = Button(button_jog_frame, text="+1", command = gcode_z_pos_1)
z_neg_1 = Button(button_jog_frame, text="-1", command = gcode_z_neg_1)
z_neg_10 = Button(button_jog_frame, text="-10", command = gcode_z_neg_10)
z_neg_100 = Button(button_jog_frame, text="-100", command = gcode_z_neg_100)
z_direction_label.grid(row=0, column=2, padx=10, pady=2)
z_pos_100.grid(row=1, column=2, padx=10, pady=2)
z_pos_10.grid(row=2, column=2, padx=10, pady=2)
z_pos_1.grid(row=3, column=2, padx=10, pady=2)
z_neg_1.grid(row=4, column=2, padx=10, pady=2)
z_neg_10.grid(row=5, column=2, padx=10, pady=2)
z_neg_100.grid(row=6, column=2, padx=10, pady=2)

speed_label = Label(speed_jog_frame, text="Speed (mm/min)")
X_Y_axis_speed_label = Label(speed_jog_frame, text="X & Y Axis")
Z_axis_speed_label = Label(speed_jog_frame, text="Z Axis")
X_Y_axis_speed_entry = Entry(speed_jog_frame)
X_Y_axis_speed_entry.insert(0, "100.0")
Z_axis_speed_entry = Entry(speed_jog_frame)
Z_axis_speed_entry.insert(0, "10.0")
speed_label.grid(row=0, column=1, padx=10, pady=10)
X_Y_axis_speed_label.grid(row=1, column=0, padx=10, pady=10)
Z_axis_speed_label.grid(row=2, column=0, padx=10, pady=10)
X_Y_axis_speed_entry.grid(row=1, column=1, padx=10, pady=10)
Z_axis_speed_entry.grid(row=2, column=1, padx=10, pady=10)

comArray = ["","","","","","",""]
for onePort in ports:
    #comButton = Button(tab1, text=onePort, height=1, width=45, command = functools.partial(initComPort, index = ports.index(onePort)))
    #print(ports.index(onePort))
    comArray[ports.index(onePort)+1] = onePort
    #comButton.grid(row=ports.index(onePort)+1, column=0)

#Setting Up drop-down menus for Initialization
choice1 = StringVar()
choice1.set("-")
choice2 = StringVar()
choice2.set("-")
choice3 = StringVar()
choice3.set("-")
drop1 = OptionMenu(stage_frame, choice1, *comArray)
drop1.grid(row = 0, column = 1)
drop1.config(width=50)
drop2 = OptionMenu(camera_frame, choice2, *comArray)
drop2.grid(row = 0, column = 1)
drop2.config(width=50)
drop3 = OptionMenu(control_frame, choice3, *comArray)
drop3.grid(row = 0, column = 1)
drop3.config(width=50)
#print(choice.get())

baudrate_array = [2400, 4800, 9600, 19200, 28800, 38400, 57600, 76800, 115200]

choicebaud1 = StringVar()
choicebaud1.set("-")
choicebaud2 = StringVar()
choicebaud2.set("-")
choicebaud3 = StringVar()
choicebaud3.set("-")
dropbaud1 = OptionMenu(stage_frame, choicebaud1, *baudrate_array)
dropbaud1.grid(row = 1, column = 1)
dropbaud1.config(width=50)
dropbaud2 = OptionMenu(camera_frame, choicebaud2, *baudrate_array)
dropbaud2.grid(row = 1, column = 1)
dropbaud2.config(width=50)
dropbaud3 = OptionMenu(control_frame, choicebaud3, *baudrate_array)
dropbaud3.grid(row = 1, column = 1)
dropbaud3.config(width=50)

InitializeButton1 = Button(stage_frame, text="Initialize", height=1, width=30, command = functools.partial(initComPort1))
InitializeButton1.grid(row = 2, column = 1, pady = 5)
InitializeButton2 = Button(camera_frame, text="Initialize", height=1, width=30, command = functools.partial(initComPort2))
InitializeButton2.grid(row = 2, column = 1, pady = 5)
InitializeButton3 = Button(control_frame, text="Initialize", height=1, width=30, command = functools.partial(initComPort3))
InitializeButton3.grid(row = 2, column = 1, pady = 5)

CloseButton1 = Button(stage_frame, text="Disconnect", height=1, width=30, command = closeComPort1)
CloseButton1.grid(row = 3, column = 1, pady = 5)
CloseButton2 = Button(camera_frame, text="Disconnect", height=1, width=30, command = closeComPort2)
CloseButton2.grid(row = 3, column = 1, pady = 5)
CloseButton3 = Button(control_frame, text="Disconnect", height=1, width=30, command = closeComPort3)
CloseButton3.grid(row = 3, column = 1, pady = 5)

def entry_gcode_get():
    global master_gcode
    master_gcode = gcode_entry.get()
    send_gcode()

gcode_entry = Entry(gcode_frame, text="Enter G-Code Here")
gcode_entry.grid(row = 0, column = 0)
gcode_button = Button(gcode_frame, text="Send G-Code", command = entry_gcode_get)
gcode_button.grid(row = 1, column = 0)

def send_input():
    global master_code
    print(master_gcode)
    master_code
    print(master_gcode)
    serialObj1.write(str.encode(master_gcode))

def varUpdate():
    #send_input()
    arduinoString = my_label3.cget("text")
    #print(arduinoString)
    serialObj1.write(str.encode(arduinoString))
    xyz_val = arduinoString
    xyz_val = xyz_val[8:]
    #print(xyz_val)

    #Limit Checks
    if(arduinoString[0] == '1'):
        x_limit.config(text="X Minimum Reached!")
    elif(arduinoString[1] == '1'):
        x_limit.config(text="X Maxmimum Reached!")
    else:
        x_limit.config(text="Gucci X")

    if(arduinoString[2] == '1'):
        y_limit.config(text="Y Minimum Reached!")
    elif(arduinoString[3] == '1'):
        y_limit.config(text="Y Maxmimum Reached!")
    else:
        y_limit.config(text="Gucci Y")

    if(arduinoString[4] == '1'):
        z_limit.config(text="Z Minimum Reached!")
    elif(arduinoString[5] == '1'):
        z_limit.config(text="Z Maxmimum Reached!")
    else:
        z_limit.config(text="Gucci Z")

    if(arduinoString[6] == '1'):
        if(x_var>xyz_val):      #Send G-Code for direction updated
            gcode_x_neg_1()
        elif(x_var<xyz_val):
            gcode_x_pos_1()
        x_var = xyz_val
        x_name.config(text="X: "+x_var)
    elif(arduinoString[6] == '2'):
        if(y_var>xyz_val):      #Send G-Code for direction updated
            gcode_y_neg_1()
        elif(y_var<xyz_val):
            gcode_y_pos_1()
        y_var = xyz_val
        y_name.config(text="Y: "+y_var)
    elif(arduinoString[6] == '3'):
        if(z_var>xyz_val):      #Send G-Code for direction updated
            gcode_z_neg_1()
        elif(z_var<xyz_val):
            gcode_z_pos_1()
        z_var = xyz_val
        z_name.config(text="Z: "+z_var)
    elif(arduinoString[6] == 'B'):          #Button Presses
        if(arduinoString[7] == '1'):
            x_button.config(text="pressed!")
            #x button pressed
        elif(arduinoString[7] == '2'):
            y_button.config(text="pressed!")
            #y button pressed
        elif(arduinoString[7] == '3'):
            z_button.config(text="pressed!")
            #z button pressed

def xyz_limit_reset():
    x_limit.config(text="X in valid range")
    y_limit.config(text="Y in valid range")
    z_limit.config(text="Z in valid range")

def xyz_button_reset():
    x_button.config(text="X button")
    y_button.config(text="Y button")
    z_button.config(text="Z button")

my_text1 = ""
my_text2 = ""
my_text3 = ""
x_var = "0"
y_var = "0"
z_var = "0"

my_label1 = Label(tab4)
my_label2 = Label(tab4)
my_label3 = Label(tab4)
x_name = Label(tab4, text = "X: "+x_var)
y_name = Label(tab4, text = "Y: "+y_var)
z_name = Label(tab4, text = "Z: "+z_var)

limit_label = Label(tab4, text = "Limit messages")
x_limit = Label(tab4, text = "X in valid range")
y_limit = Label(tab4, text = "Y in valid range")
z_limit = Label(tab4, text = "Z in valid range")

limit_reset = Button(tab4, text = "Reset Min & Max", command = xyz_limit_reset)
limit_reset.grid(column = 1, row = 4)

button_reset = Button(tab4, text = "Reset Button Presses", command = xyz_button_reset)
button_reset.grid(column = 2, row = 4)

x_button = Label(tab4, text = "X button")
y_button = Label(tab4, text = "Y button")
z_button = Label(tab4, text = "Z button")

my_label3.grid(column = 0, row = 0, padx = 30, pady = 0) #Input controls String
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


#my_label1.config(text=my_text1)

def checkSerialPort():
    if serialObj1.isOpen() and serialObj1.in_waiting:
        recentPacket = serialObj1.readline()
        my_text1 = recentPacket.decode('utf').rstrip('\n')
        my_label1.config(text=my_text1)
        varUpdate()
    if serialObj2.isOpen() and serialObj2.in_waiting:
        recentPacket = serialObj2.readline()
        my_text2 = recentPacket.decode('utf').rstrip('\n')
        my_label2.config(text=my_text2)
        varUpdate()
    if serialObj3.isOpen() and serialObj3.in_waiting:
        recentPacket = serialObj3.readline()
        my_text3 = recentPacket.decode('utf').rstrip('\n')
        my_label3.config(text=my_text3)
        varUpdate()
    root.update()
    root.after(1, checkSerialPort) #Recursive call to allow for root.mainloop()

root.after(1, checkSerialPort)
root.mainloop() 
#while True:
    #root.update()
    #checkSerialPort()