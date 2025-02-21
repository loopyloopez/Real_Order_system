



import time
import Buttons
import tkinter as tk
# Get the root window of Tkinter, the GUI backend for turtle
window = tk.Tk()
window.attributes('-fullscreen', True)
window.title("ORDERS")
buttonsmade = 0
orders = 0
print("called")

buttonsmade_list = []

def check():
    global buttonsmade_list
    global orders
    with open("orders/total.txt","r")as txt:
        orders = int(txt.read())
    global buttonsmade
    print("checking...")
    
    if buttonsmade < orders:
        print(f'there has been {buttonsmade} buttons made and {orders} orders that actually exist')
        time.sleep(1)
        for file in range(buttonsmade,orders + 1):
            if(file not in buttonsmade_list):
                buttonsmade_list.append(file)
                print(f'order {file} has no button..making button')
                try:
                    with open(f'orders/order{file}.txt',"r") as txt:
                        print(f'found order {file}')
                        Buttons.make_button(file)
                        print("button made succesfully")
                        buttonsmade+= 1
                except:
                    print("no file..Moving on")
            else:
                print("button fo file alr made")
    
    window.after(3000, check)


check()   
        

    
window.mainloop()     


        
    



















# Keep the window open until it is closed manually


