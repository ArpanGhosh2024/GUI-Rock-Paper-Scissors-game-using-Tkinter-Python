# A Simple GUI Rock,Paper,Scissors game.
from tkinter import *
from tkinter import messagebox
import random
window=Tk()
window.geometry("600x600")
window.title("Rock-Paper-Scissors by Arpan Ghosh")
window.configure(bg="pink")
user_choice=StringVar()
user_choice.set(None) 
computer_choice=StringVar()
computer_choice.set(None) 
win=StringVar()
win.set(None)
def playAgain():
    l3.destroy()
    l4.destroy()
    l5.destroy()
    b1['state']=NORMAL
    b2['state']=DISABLED

def user():
    b1['state']=DISABLED 
    b2['state']=NORMAL
    global l3
    l3=Label(window,text="User's Choice = "+user_choice.get(),font=('Times New Roman',15,'bold'),bg="pink")
    l3.pack(pady=10)
    computer()

def computer():
    global l4
    computer_choices=['rock','paper','scissor']
    computer_choice.set(random.choice(computer_choices))
    l4=Label(window,text="Computer's Choice = "+computer_choice.get(),font=('Times New Roman',15,'bold'),bg="pink")
    l4.pack(pady=10)
    winner()

def winner():
    global l5
    if(user_choice.get()=="rock"):
        if(computer_choice.get()=="rock"):
            win.set("Both rocks cancel each other out, Tie!!!")
            l5=Label(window,text=win.get(),bg="yellow",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)
        elif(computer_choice.get()=="scissor"):
            win.set("Rock smashes scissor, You Win!!!")
            l5=Label(window,text=win.get(),bg="light green",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)
        elif(computer_choice.get()=="paper"):
            win.set("Paper Engulfs rock, You Lose!!!")
            l5=Label(window,text=win.get(),bg="red",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)

    elif(user_choice.get()=="paper"):
        if(computer_choice.get()=="paper"):
            win.set("Both paper cancel each other out, Tie!!!")
            l5=Label(window,text=win.get(),bg="yellow",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)
        elif(computer_choice.get()=="rock"):
            win.set("Paper Engulfs rock, You Win!!!")
            l5=Label(window,text=win.get(),bg="light green",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)
        elif(computer_choice.get()=="scissor"):
            win.set("Scissor cuts paper, You Lose!!!")
            l5=Label(window,text=win.get(),bg="red",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)
    

    elif(user_choice.get()=="scissor"):
        if(computer_choice.get()=="scissor"):
            win.set("Both scissors cancel each other out, Tie!!!")
            l5=Label(window,text=win.get(),bg="yellow",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)
        elif(computer_choice.get()=="paper"):
            win.set("Scissor cuts paper, You Win!!!")
            l5=Label(window,text=win.get(),bg="light green",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)
        elif(computer_choice.get()=="rock"):
            win.set("Rock smashes scissor, You Lose!!!")
            l5=Label(window,text=win.get(),bg="red",font=('Times New Roman',15,'bold'))
            l5.pack(pady=10)

    else:
        win.set("No Result!!!")
        l5=Label(window,text=win.get(),bg="yellow",font=('Times New Roman',15,'bold'))
        l5.pack(pady=10)
        messagebox.showwarning("No Input","You have not chosen anything!!!")

l1=Label(window,text="Rock, Paper, Scissors",font=('Times New Roman',17,'bold'),bg="light blue")
l1.pack(pady=10)
l2=Label(window,text="Please make your choice(Rock, Paper, Scissor)...",font=('Times New Roman',15,'bold'),bg="light blue")
l2.pack(pady=10)
r1=Radiobutton(window,text="Rock",variable=user_choice,value="rock",font=("bold"),bg="pink")
r1.pack(pady=5)
r2=Radiobutton(window,text="Paper",variable=user_choice,value="paper",font=("bold"),bg="pink")
r2.pack(pady=5)
r3=Radiobutton(window,text="Scissor",variable=user_choice,value="scissor",font=("bold"),bg="pink")
r3.pack(pady=5)
b1=Button(window,text="Play",font=('Times New Roman',15,'bold'),bg="light green",activebackground="black",activeforeground="light green",command=user)
b1.pack(pady=10)
b2=Button(window,text="Play Again",font=('Times New Roman',15,'bold'),bg="aqua",activebackground="black",activeforeground="aqua",state=DISABLED,command=playAgain)
b2.pack(pady=10)
b3=Button(window,text="Quit",font=('Times New Roman',15,'bold'),bg="red",activebackground="black",activeforeground="red",command=window.destroy)
b3.pack(pady=10)
window.mainloop()
