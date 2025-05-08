import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from easygui import *
import smtplib
import pygame
from datetime import datetime
from pathlib import Path
import datetime as dt
import subprocess
import os
midsession = False

class make_button:
    def __init__(self, pos,root):
        self.root = root
        
        if pos == 0:
            self.frame = tk.Frame(borderwidth=2, relief="groove")
            self.frame.pack(padx=20, pady=20)
            self.s = tk.Button( self.frame,
                    text=f'+', 
                    command=self.regester,
                    activebackground="yellow", 
                    activeforeground="yellow",
                    bd=3,
                    bg="yellow",
                    cursor="hand2",
                    disabledforeground="yellow",
                    fg="black",
                    font=("Arial", 15),
                    height=1,
                    highlightbackground="yellow",
                    highlightcolor="yellow",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=10,
                    pady=20,
                    width=1,
                    wraplength=100)
            self.s.grid(column=0, row=3) 

            self.sys = tk.Button( self.frame,
                    text='ENTER', 
                    command=self.clock,
                    activebackground="pink", 
                    activeforeground="pink",
                    bd=3,
                    bg="pink",
                    cursor="hand2",
                    disabledforeground="pink",
                    fg="black",
                    font=("Arial", 15),
                    height=1,
                    highlightbackground="pink",
                    highlightcolor="white",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=15,
                    pady=20,
                    width=10,
                    wraplength=100)
            self.sys.grid(column=1, row=3,rowspan=3) 
            self.syss = tk.Button( self.frame,
                    text='LEAVE', 
                    command=self.clockout,
                    activebackground="blue", 
                    activeforeground="blue",
                    bd=3,
                    bg="blue",
                    cursor="hand2",
                    disabledforeground="blue",
                    fg="blue",
                    font=("Arial", 15),
                    height=1,
                    highlightbackground="blue",
                    highlightcolor="white",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=15,
                    pady=20,
                    width=10,
                    wraplength=100)
            self.syss.grid(column=2, row=3,rowspan=3) 


            self.logs = tk.Button( self.frame,
                    text="LOGS", 
                    command=self.checklogs,
                    activebackground="orange", 
                    activeforeground="orange",
                    bd=3,
                    bg="orange",
                    cursor="hand2",
                    disabledforeground="orange",
                    fg="black",
                    font=("Arial", 15),
                    height=1,
                    highlightbackground="black",
                    highlightcolor="white",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=10,
                    pady=20,
                    width=10,
                    wraplength=100)
            self.logs.grid(column=3, row=3) 
            
            self.reset = tk.Button( self.frame,
                    text="↻", 
                    command=self.reset,
                    activebackground="red", 
                    activeforeground="red",
                    bd=3,
                    bg="red",
                    cursor="hand2",
                    disabledforeground="red",
                    fg="black",
                    font=("Arial", 15),
                    height=1,
                    highlightbackground="red",
                    highlightcolor="white",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=10,
                    pady=20,
                    width=10,
                    wraplength=100)
            self.reset.grid(column=4, row=3) 
        else:
                    
        
        
            pygame.init()
            pygame.mixer.music.load("/home/loopyloops/Documents/A.O.S/Real_Order_system/20187-Trumpet-21_Bb_BPM_135.wav")
            pygame.mixer.music.play()
            self.timesverificationwassent = 0
            self.pos = pos
            row_pos = int(pos / 5)
            
            self.frame = tk.Frame(borderwidth=2, relief="groove")
            self.frame.pack(padx=10, pady=20)
        

            self.button = tk.Button( self.frame,
                        text=f'Order #{pos}\n{dt.datetime.now().strftime("%I:%M %p")}',
                        command=self.button_clicked,
                        activebackground="blue", 
                        activeforeground="white",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Roman", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)
            
            
            self.button.grid(column=pos, row=row_pos)
            self.delete = tk.Button( self.frame,
                        text=f'❌', 
                        command=self.delete_button,
                        activebackground="red", 
                        activeforeground="black",
                        bd=3,
                        bg="red",
                        cursor="hand2",
                        disabledforeground="red",
                        fg="black",
                        font=("Arial", 12),
                        height=1,
                        highlightbackground="red",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="left",
                        overrelief="raised",
                        padx=10,
                        pady=20,
                        width=1,
                        wraplength=100)
            
            
            self.delete.grid(column=pos - 1, row=row_pos)
            
            self.verify = tk.Button( self.frame,
                        text=f'◛', 
                        command=self.send_verifcation,
                        activebackground="green", 
                        activeforeground="green",
                        bd=3,
                        bg="green",
                        cursor="hand2",
                        disabledforeground="green",
                        fg="black",
                        font=("Arial", 12),
                        height=1,
                        highlightbackground="green",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="left",
                        overrelief="raised",
                        padx=10,
                        pady=20,
                        width=2,
                        wraplength=100)
            
            
            self.verify.grid(column=pos + 1, row=row_pos) 

        
        
        
        
    def button_clicked(self):
        
       
        with open(f'/home/loopyloops/Documents/A.O.S/Real_Order_system/orders/order{self.pos}.txt',"r") as file:
            info = file.read()
        messagebox.showinfo("Order Details", info)
        
    def delete_button(self):
        response = messagebox.askyesnocancel("Warning!!", "Are you sure you wanna delete this?")
        doublecheck = messagebox.askyesnocancel("Confrim", "click yes to confirm")
        xfile = f'/home/loopyloops/Documents/A.O.S/Real_Order_system/orders/order{self.pos}.txt'
        if os.path.exists(xfile):
            os.remove(xfile)
        if response and doublecheck:
            self.verify.destroy()
            self.delete.destroy()
            self.button.destroy()
            self.frame.destroy()
        else:
            return
    
    def send_verifcation(self):
        with open(f'/home/loopyloops/Documents/A.O.S/Real_Order_system/orders/order{self.pos}.txt',"r") as file:
            Gmail = file.read().split("\n")
            
        if self.timesverificationwassent == 0:
            self.timesverificationwassent += 1
            waittime = simpledialog.askstring(title="Duration",
                                  prompt="Enter estimate wait time:")
            
            self.send_email(Gmail,waittime)
            self.verify.destroy()
    
    
    

    def send_email(self, recipients, waittime):
        
        subject = "Order being processed!!"
        body = f"Thank you for ordering at Anitas Mexican restaurants! Food has been recieved and we estimate a wait time of {waittime} minutes."

        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login("anitasmexicanrestaurants@gmail.com", "qsjd fxss uoml tjnt")
            smtp_server.sendmail("anitasmexicanrestaurants@gmail.com", recipients, msg=message)
                 
        #messagebox.showinfo("Order Details", info)
    
    def regester(self):
        global midsession
        if not midsession:
            midsession = True
            while True:
                Name = simpledialog.askstring(title="Name",
                                        prompt="Enter your Name")
                
                if Name:
                    newID = simpledialog.askstring(title="New ID",
                                        prompt="Enter your employee ID")
                    
                
                try:
                    if(newID.isalpha()):
                        box = messagebox.showerror("NO LETTERS!","Try again, only use numbers")
                        midsession = False 
                        break
                except:
                    midsession = False 
                    break
                
                
                file_path = Path(f'/home/loopyloops/Documents/A.O.S/Real_Order_system/Tracker/{newID}.txt')
        
                if file_path.exists():
                    messagebox.showerror("Error", f'This ID combination has already been used')
                    midsession = False 
                    break
                    

                else:
                    messagebox.showinfo('Good job', 'Process completed!')

                    with open(file_path,"w") as file:
                        file.write(f'Name={Name}, ID={newID}\n\n')
                    midsession = False    
                    break
            

               
        
    

    def clock(self):
        
        ID = simpledialog.askstring(title="System",
                                prompt="Enter your employee ID")
        
        file_path = Path(f'/home/loopyloops/Documents/A.O.S/Real_Order_system/Tracker/{ID}.txt')
    
        if file_path.exists():
           
            time = dt.datetime.now().strftime("%I:%M %p")
         
            
            
            
           
                   
                          
            with open(file_path,"r") as file:
                oldinfo = file.read()
                
            if(oldinfo.split("\n")[-2][8:10] == "in"):
                messagebox.showinfo('', 'You already clocked in bruh')
                return
                

               
                


            with open(file_path,"w") as file:
                file.write(oldinfo)
                file.write(f'\nClocked in-{time}\n')
            messagebox.showinfo('Hello!', 'succesfully clocked in')
               
        
        else:
            messagebox.showerror("Error", f'This ID does not exist')
    def clockout(self):
        ID = simpledialog.askstring(title="System",
                                prompt="Enter your employee ID")
        
        file_path = Path(f'/home/loopyloops/Documents/A.O.S/Real_Order_system/Tracker/{ID}.txt')
        if file_path.exists():
            with open(file_path,"r") as file:
                oldinfo = file.read()
            
            if(oldinfo.split("\n")[-2][8:10] != "in"):
                messagebox.showinfo('', 'You forgot to clock in')
                return
            
            rtime = dt.datetime.now().strftime("%I:%M %p")
            time = dt.datetime.now().strftime("%I:%M %p")
            
            now = datetime.now()
            month_name = now.strftime("%B")
            day_of_month = now.strftime("%d")
            messagebox.showinfo('Good Bye', 'succesfully clocked out')
            
                   

            with open(file_path,"w") as file:
                file.write(oldinfo)
                x1 = oldinfo.split("\n")[-2].split("-")[1]
                    
                  
                times = [x1,time]
                    
                for time in range(0,2):
                     
                    if times[time].split(" ")[1] == "PM":
                            
                        addon = 12
                
                    else:
                           
                        addon = 0
                            
                            
                    hour = str(int(times[time].split(":")[0]) + addon)
                    minutes = times[time].split(":")[1].split(" ")[0]
                    total = int(hour) * 60 + int(minutes)
                    times[time] = total
                       
                    
                addedtime = round((times[1] - times[0]) / 60,2)
                try:
                    oldtotal = oldinfo.split("\n")
                        #print(oldtotal[len(oldtotal)-4])
                    oldtotal = float(oldtotal[len(oldtotal)-4].split(":")[-1])
                       
                except:       
                    oldtotal = 0
                    
                    
                file.write(f'Clocked out-{rtime}\n{month_name} {day_of_month},Hours:{addedtime}\ntotal hours:{round((oldtotal + addedtime),2)} \n------------------------------------')
                   
                                           
                   
                
        else:
            messagebox.showerror("Error", f'This ID does not exist')
        

    def reset(self):
        Pass = simpledialog.askstring(title="System",
                                prompt="Enter Admin password")
        
        if Pass == "2025":
            for x in range(0,25):
                ID_path = f'/home/loopyloops/Documents/A.O.S/Real_Order_system/Tracker/{x}.txt'
                if os.path.exists(ID_path):
                        
                    with open(ID_path,"r") as file:
                        title = file.read().split("\n")[0]
                            
                    with open(ID_path,"w") as file:
                            
                        file.write(f'{title}\n')
            messagebox.showinfo("System","All LOGS deleted")
        else:
            messagebox.showerror("nuh uh","Wrong password")
                
        


    def checklogs(self):
        ID = simpledialog.askstring(title="System",
                                prompt="Enter employee ID")
        
        file_path = Path(f'/home/loopyloops/Documents/A.O.S/Real_Order_system/Tracker/{ID}.txt')
        if(file_path.exists()):
            self.show_log_box(file_path)
        
        else:
            messagebox.showerror("Error", f'This ID does not exist')


    def show_log_box(self,filename):
        
        # Create the main window
        root = tk.Tk()
        root.title("Text File Viewer")

        # Create a ScrolledText widget for a scrollable text area
        text_area = ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        text_area.pack(expand=True, fill="both")

        try:
            # Open and read the text file
            with open(filename, "r") as file:
                content = file.read()
            # Insert the content into the text area
            text_area.insert("1.0", content)
        except Exception as e:
            text_area.insert("1.0", f"Error opening file: {e}")

        # Set the widget to read-only
        text_area.config(state="disabled")

        # Start the Tkinter main loop
        root.mainloop()

            
        
        




        
        

        
        
        
    
    