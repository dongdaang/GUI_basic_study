from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼44444444")
btn4.pack()

root.mainloop()