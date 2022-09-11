
import tkinter as tk 
import tkinter.messagebox as mb
from Guessclass import Guess 

Root = tk.Tk()
Root.title("Guess it")
Root.geometry("215x300")
Root.resizable(width=False,height=False)


#Definitions
resstr = tk.StringVar()
playerstr = tk.StringVar()
pcstr = tk.StringVar()

#Functions 

def Submitbutton():
    period = 0
    lvlint = lvlentry.get()
    playernumber=guessentry.get()

    if lvlint=="" or playernumber=="" :
        lvlint = lvlentry.get()
        playernumber=guessentry.get()
        resstr.set(" ")
        playerstr.set(f" ")
        pcstr.set(f" ")
     
        
    try:
        
        lvlint = int(lvlentry.get())
        playernumber=int(guessentry.get())
        if lvlint!= 1 and lvlint!= 2 and lvlint!= 3:
            mb.showerror("Wrong level" , "Please enter correct level")
            resstr.set(" ")
            playerstr.set(f" ")
            pcstr.set(f" ")
            lvlint = int(lvlentry.get())
        else:

            if lvlint==1:
                period = 10
                if int(guessentry.get()) > 10 or int(guessentry.get()) < 1:
                    mb.showerror("Period error","Please enter a number between 1-10")
                    resstr.set(" ")
                    playerstr.set(f" ")
                    pcstr.set(f" ")
                    playernumber=int(guessentry.get())
            elif lvlint==2:
                period=100
                if int(guessentry.get()) > 100 or int(guessentry.get()) < 1:
                    mb.showerror("Period error","Please enter a number between 1-100")
                    resstr.set(" ")
                    playerstr.set(f" ")
                    pcstr.set(f" ")
                    playernumber=int(guessentry.get())
            else:
                period=1000
                if int(guessentry.get()) > 1000 or int(guessentry.get()) < 1:
                    mb.showerror("Period error","Please enter a number between 1-1000")
                    resstr.set(" ")
                    playerstr.set(f" ")
                    pcstr.set(f" ")
                    playernumber=int(guessentry.get())
        
            playobj1 = Guess(period)
            ans = playobj1.CheckTrue(playernumber)
        

            if ans:
                mb.showinfo("Win","You won")
                resstr.set("Your answer is correct")
            else:
                resstr.set("Your answer is wrong")
            
            playerstr.set(f"your answer : {playernumber}")
            pcstr.set(f"Number : {playobj1.number}")

            return ans 

    except:
        pass

#Entries 

lvlentry = tk.Entry(Root,width=10)
lvlentry.place(x=5,y=100)

guessentry = tk.Entry(Root,width=20)
guessentry.place(x=80,y=100)

#labels
lvllabel = tk.Label(Root,text="Level1: 1-10\nLevel2: 1-100\nLevel3: 1-1000")
lvllabel.place(x=2,y=8)

enterlvllabel = tk.Label(Root,text="Level: ")
enterlvllabel.place(x=2,y=77)

enterguesslabel = tk.Label(Root,text="Your guess: ")
enterguesslabel.place(x=80,y=77)

pc_guess_Label = tk.Label(Root,textvariable=pcstr)
pc_guess_Label.place(x=50,y=170)


player_guess_Label = tk.Label(Root,textvariable=playerstr)
player_guess_Label.place(x=50,y=195)


result_Label = tk.Label(Root,textvariable=resstr)
result_Label.place(x=50,y=220)

#Buttons 
submit_Button = tk.Button(Root,text="Submit guess",command=Submitbutton)
submit_Button.place(x=50,y=140)


Root.mainloop()