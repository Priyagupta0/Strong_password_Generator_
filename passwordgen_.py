from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title('--Strong Password Generator--')
root.geometry("500x300")


password = chr(randint(33,126))

def alert():
    messagebox.showinfo("Alert","Done,Your password generated !!")

# function generate password
def new_rand():
    pw_entry.delete(0,END)

    pw_length = int(my_entry.get())

    password=''

    for x in range(pw_length):
            password += chr(randint(33,126))
    

    pw_entry.insert(0,password)

    alert()

# reset function
def reset_all():
    my_entry.delete(0,END)
    pw_entry.delete(0,END)
    
# Label for user input
lf = LabelFrame(root,text="How many Characters?")
lf.pack(pady=20)

# Input 
my_entry = Entry(lf,font=("Helvetica,24"))
my_entry.pack(pady=20,padx=20)

# Output 
pw_entry = Entry(root , text = '' , font = ("Helvetica,24"),bd=0,bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

# Generate strong password button
my_button = Button(my_frame, text='Generate strong Password',command=new_rand)
my_button.grid(row=0,column=0,padx=10)

# reset button
reset_button = Button(my_frame, text='Reset',command=reset_all)
reset_button.grid(row=0,column=1,padx=10)

root.mainloop()