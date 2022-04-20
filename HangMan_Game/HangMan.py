from tkinter import *
import tkinter as tk
Game = Tk()

w = Game.winfo_screenwidth()/2-600

h = Game.winfo_screenheight()/2-350

Game.title("HangGame")
Game.geometry("1200x700+{}+{}".format(int(w),int(h)))

Label1 = tk.Label(
    Game,
    text="hello",
    fg= "white",
    bg= "black",
    width=1200
)
Label2 = tk.Label(
    Game,
    text="word",
    fg= "black",
    bg= "white",
    width=1200
)
Label1.pack()
Label2.pack()

Game.mainloop()