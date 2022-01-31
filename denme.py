import subprocess
import tkinter as tk
from tkinter import PhotoImage
import time   
from tkinter.constants import HORIZONTAL
from typing import Text
import os
import sys
from urllib.robotparser import RobotFileParser
sys.path.append( os.getcwd()) 
Root_dır =  os.getcwd()
print(Root_dır)
Onn =0
say=0
def fanOff():
    global text,Onn,text2
    fanMin()
    Onn= 0
    text2.configure(text="Fan=OFF")
    text2.place(x= 70 ,y= 180 )
def fanOnn():
    global Onn,text2
    Onn = 1
    tempSen()
    
    text2.configure(text="Fan=ON")
    text2.place(x= 70 ,y= 180 )
def fanMin():
    comand=['bash','/home/drobotic/Desktop/Agx_fan_managmentV1/fan25.sh']
    fanBeam = subprocess.run(comand, stdout=subprocess.PIPE)
def fanNormal():
    comand=['bash','/home/drobotic/Desktop/Agx_fan_managmentV1/fan80.sh']
    fanBeam = subprocess.run(comand, stdout=subprocess.PIPE)
def fanMax():
    comand=['bash','/home/drobotic/Desktop/Agx_fan_managmentV1/fanMax.sh']
    fanBeam = subprocess.run(comand, stdout=subprocess.PIPE)
    text2.configure(text="Fan=Max")
    text2.place(x= 70 ,y= 180 )
def tempSen():
    global text,say
    result = subprocess.run(['cat' , '/sys/class/thermal/thermal_zone1/temp'], stdout=subprocess.PIPE)
    result1 = subprocess.run(['cat' , '/sys/class/thermal/thermal_zone2/temp'], stdout=subprocess.PIPE)

    cpu = result.stdout.decode('utf-8')
    cpu = int(cpu)

    gpu = result1.stdout.decode('utf-8')
    gpu = int(cpu)
    text = tk.Label(window,bg='#14213D',fg="white", text=("Cpu=",cpu/1000),font=("Arial", 25)) 
    text.place(x= 30 ,y= 10 )
    text1 = tk.Label(window, bg='#14213D',fg="white",text=("Gpu=",gpu/1000),font=("Arial", 25) ) 
    text1.place(x= 30 ,y= 50 )
    text.after(1000,tempSen)
    if Onn ==1 :
        
        if cpu/1000 > 25  and cpu/1000< 30:
            fanMin()
            print("min")
            say=1
        elif cpu/1000 >= 31 and say !=2 :
            fanNormal()
            print("nor")
            say=2
        elif cpu/1000 > 50 and say !=3:
            fanMax()
            say=3
        if Onn == 0:
            pass


 

window = tk.Tk()

window.geometry("200x200")
window.wm_title("Jetson Fan Managment")
window.configure(bg='#14213D')
photo = tk.PhotoImage(file = r"onnS.png")
photo1 = tk.PhotoImage(file = r"offS.png")
photo2 = tk.PhotoImage(file = r"speedometer.png")
button1 = tk.Button(window,text="Off",bg='#14213D',highlightthickness=0,borderwidth=0,image=photo1,command=fanOff)
button1.place(x=10,y=100)

button2 = tk.Button(window,text="On",bg='#14213D',highlightthickness=0,borderwidth=0,image=photo,command=fanOnn)
button2.place(x=120,y=100)

button3 = tk.Button(window,image=photo2,fg="white",highlightthickness=0,borderwidth=0,bg='#14213D',command=fanMax)
button3.place(x=2,y=178)
text2 = tk.Label(window, text="Fan=OFF",font=("Arial", 10) ) 
text2.place(x= 70 ,y= 180 )


tempSen()
window.mainloop()