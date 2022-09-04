
import tkinter as tk 


Root = tk.Tk()
Root.title("Guess it")
Root.geometry("215x300")
Root.resizable(width=False,height=False)




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

pc_guess_Label = tk.Label(Root,text="pc")
pc_guess_Label.place(x=50,y=170)


player_guess_Label = tk.Label(Root,text="palyer")
player_guess_Label.place(x=50,y=195)


result_Label = tk.Label(Root,text="winner")
result_Label.place(x=50,y=220)

#Buttons 
submit_Button = tk.Button(Root,text="Submit guess")
submit_Button.place(x=50,y=140)


Root.mainloop()