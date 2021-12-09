import tkinter.messagebox as tmsg
from tkinter import *

root=Tk()
root.title("my GUI")
root.geometry("400x400")
root.minsize(200,200)
root.maxsize(600,700)
label=Label(text="this is my label",bg="red",fg="white",padx=30,pady=40,borderwidth=50)
def hello():
    print("how are u")




b1= Button(fg="red",text="click me",command=hello)
b1.pack(side=LEFT,padx=23)




label.pack()









root.mainloop()
