import tkinter as tk
from tkinter import messagebox, simpledialog
from easygui import *
import smtplib
import pygame
from datetime import datetime
from pathlib import Path

class make_button:
    def __init__(self, pos):
        self.Clocked = []
        if pos == 0:
            self.frame = tk.Frame(borderwidth=2, relief="groove")
            self.frame.pack(padx=10, pady=20)
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
                    font=("Arial", 12),
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
                    text=f'clock in/out', 
                    command=self.clock,
                    activebackground="blue", 
                    activeforeground="blue",
                    bd=3,
                    bg="blue",
                    cursor="hand2",
                    disabledforeground="blue",
                    fg="black",
                    font=("Arial", 12),
                    height=1,
                    highlightbackground="blue",
                    highlightcolor="blue",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=10,
                    pady=20,
                    width=10,
                    wraplength=100)
            self.sys.grid(column=1, row=3,rowspan=3) 
            self.logs = tk.Button( self.frame,
                    text="LOGS", 
                    command=self.checklogs,
                    activebackground="orange", 
                    activeforeground="orange",
                    bd=3,
                    bg="orange",
                    cursor="hand2",
                    disabledforeground="orange",
                    fg="orange",
                    font=("Arial", 12),
                    height=1,
                    highlightbackground="orange",
                    highlightcolor="orange",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=10,
                    pady=20,
                    width=10,
                    wraplength=100)
            self.logs.grid(column=2, row=3) 
        else:
                    
        
        
            pygame.init()
            pygame.mixer.music.load("20187-Trumpet-21_Bb_BPM_135.wav")
            pygame.mixer.music.play()
            self.timesverificationwassent = 0
            self.pos = pos
            row_pos = int(pos / 5)
            print("button made for order" + str(pos))
            self.frame = tk.Frame(borderwidth=2, relief="groove")
            self.frame.pack(padx=10, pady=20)
        

            self.button = tk.Button( self.frame,
                        text=f'Order #{pos}',
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
                        text=f'ERASE', 
                        command=self.delete_button,
                        activebackground="red", 
                        activeforeground="red",
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
                        text=f'Aknowledge', 
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
       
        with open(f'orders/order{self.pos}.txt',"r") as file:
            info = file.read()
        messagebox.showinfo("Order Details", info)
        
    def delete_button(self):
        response = messagebox.askyesnocancel("Warning!!", "Are you sure you wanna delete this?")
        doublecheck = messagebox.askyesnocancel("Confrim", "click yes to confirm")
        if response and doublecheck:
            self.verify.destroy()
            self.delete.destroy()
            self.button.destroy()
            self.frame.destroy()
        else:
            return
    
    def send_verifcation(self):
        with open(f'orders/order{self.pos}.txt',"r") as file:
            Gmail = file.read().split("\n")
            
        if self.timesverificationwassent == 0:
            self.timesverificationwassent += 1
            waittime = simpledialog.askstring(title="Duration",
                                  prompt="Enter estimate wait time:")
            
            self.send_email(Gmail,waittime)
            self.verify.destroy()
    
    
    

    def send_email(self, recipients, waittime):
        print("sending email")
        subject = "Order being processed!!"
        body = f"Thank you for ordering at Anitas Mexican restaurants! Food has been recieved and we estimate a wait time of {waittime} minues."

        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login("anitasmexicanrestaurants@gmail.com", "qsjd fxss uoml tjnt")
            smtp_server.sendmail("anitasmexicanrestaurants@gmail.com", recipients, msg=message)
        print("Message sent!")             
        #messagebox.showinfo("Order Details", info)
    
    def regester(self):
        while True:
            Name = simpledialog.askstring(title="Name",
                                    prompt="Enter your Name")
            
            newID = simpledialog.askstring(title="New ID",
                                    prompt="Enter your employee ID")
            
            if(newID.isalpha()):
                messagebox.showerror("NO LETTERS!","Try again, only use numbers")
            
            
            file_path = Path(f'Tracker/{newID}')
    
            if file_path.exists():
                messagebox.showerror("Error", f'This ID combination has already been used')
                response = messagebox.askyesnocancel("Oh no...", "do you wanna try again?")
                if response:
                    return

            else:
                messagebox.showinfo('Good job', 'Process completed!')

                with open(file_path,"w") as file:
                    file.write(f'Name:{Name}, ID:{newID}\n\n')

                return
        
    

    def clock(self):
        
        ID = simpledialog.askstring(title="System",
                                prompt="Enter your employee ID")
        
        file_path = Path(f'Tracker/{ID}')
    
        if file_path.exists():
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
         
            now = datetime.now()
            month_name = now.strftime("%B")
            day_of_month = now.strftime("%d")
            
            if ID in self.Clocked:
                messagebox.showinfo('Good Bye', 'succesfully clocked out')
                with open(file_path,"r") as file:
                    oldinfo = file.read()
                   

                with open(file_path,"w") as file:
                    file.write(oldinfo)
                    file.write(f'Clocked out:{time}\n {month_name} {day_of_month}\n ------------------------------------\n')
                self.Clocked.remove(ID)
            
            else:
              
                with open(file_path,"r") as file:
                    oldinfo = file.read()

                days = int((len(oldinfo.split("\n")) - 2) / 5)
                days += 1


                with open(file_path,"w") as file:
                    file.write(oldinfo)
                    file.write(f'log #{days}\nClocked in:{time}\n')
                messagebox.showinfo('Hello!', 'succesfully clocked in')
                self.Clocked.append(ID)
        
        else:
            messagebox.showerror("Error", f'This ID does not exist')



    def checklogs(self):
        ID = simpledialog.askstring(title="System",
                                prompt="Enter employee ID")
        
        file_path = Path(f'Tracker/{ID}')
        if(file_path.exists()):
            with open(file_path,"r") as file:
                oldinfo = file.read()

            messagebox.showinfo(f'#{ID} Logs', oldinfo)
            

            
        

        else:
            messagebox.showerror("Error", f'This ID does not exist')


        
        
        




        
        

        
        
        
    
    