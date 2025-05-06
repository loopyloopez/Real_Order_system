#! /usr/bin/python3



import time
import sys
sys.path.append('/home/loopyloops/Documents/A.O.S/Real_Order_system/Buttons.py')
import Buttons

import tkinter as tk
import os
import datetime
from datetime import datetime as date

"""
xdate = str(date.today()).split(" ")[0]
day = date.today().strftime("%A")
weekfile_path = "/home/loopyloops/Documents/A.O.S/Real_Order_system/Tracker/Week.txt"


def writetoweek():
    global xdate
    global weekfile_path
    with open(weekfile_path,"w") as file:
        file.write(str(xdate))
        


if day == "Friday":
    
    with open(weekfile_path,"r") as file:
        week = file.read()
        if week != xdate:
             for x in range(0,25):
                ID_path = f'/home/loopyloops/Documents/A.O.S/Real_Order_system/Tracker/{x}.txt'
                if os.path.exists(ID_path):
                    
                    with open(ID_path,"r") as file:
                        title = file.read().split("\n")[0]
                        
                    with open(ID_path,"w") as file:
                        
                        file.write(f'{title}\n')
                        
    writetoweek()
    """
    

# Get the root window of Tkinter, the GUI backend for turtle
window = tk.Tk()
window.attributes('-zoomed', True)
window.title("ORDERS")

buttonsmade = 0
orders = 0


buttonsmade_list = []



Buttons.make_button(0,window)
def check():
    global buttonsmade_list
    global orders
   
        
    with open("/home/loopyloops/Documents/A.O.S/Real_Order_system/orders/total.txt","r")as txt:
        orders = int(txt.read())
    global buttonsmade
    
   
                
    if buttonsmade < orders:
        print(f'there has been {buttonsmade} buttons made and {orders} orders that actually exist')
        time.sleep(1)
        for file in range(buttonsmade,orders + 1):
            if(file not in buttonsmade_list):
               
                print(f'order {file} has no button..making button')
                try:
                    with open(f'/home/loopyloops/Documents/A.O.S/Real_Order_system/orders/order{file}.txt',"r") as txt:
                        print(f'found order {file}')
                        Buttons.make_button(file,root=window)
                        print("button made succesfully")
                        buttonsmade_list.append(file)
                        buttonsmade+= 1
                except Exception as e:
                    print("error making file..Moving on")
                    print(e)
           
              
    
    window.after(3000, check)



check()   
        

    
window.mainloop()     


        
    



















# Keep the window open until it is closed manually


