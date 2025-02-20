import tkinter as tk
from tkinter import messagebox, simpledialog
from easygui import *
import smtplib
import pygame

class make_button:
    def __init__(self, pos):
        
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
                    anchor="center",
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
                    anchor="center",
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
                    anchor="center",
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
        
        
        
    
    