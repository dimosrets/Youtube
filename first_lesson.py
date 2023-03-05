#from tkinter import *
import tkinter as tk
#import tkinter

# take the stuff from tkinter 
window = tk.Tk()
# set the title of the app
window.title("The First App")
# set the geometry of the window
window.geometry("300x300")

# set the window size fixed
window.minsize(width = 300 , height = 300 )
window.maxsize(width = 500 , height = 500 )

# set window now resizable
#window.resizable(False,False)

hello_label = tk.Label(window,text = "Hello World!!")
hello_label.pack()

window.mainloop()
