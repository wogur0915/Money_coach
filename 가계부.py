from tkinter import *

root = Tk()
root.title("House-hold account helper")
root.iconbitmap('c:/...')
def myClick():
    return

frame = LabelFrame(root, text = "", padx = 35, pady=35)
frame.grid(padx=10, pady=10)

myButton1 = Button(frame, text="수입",padx = 16, pady = 10,  command = myClick)
myButton1.grid(row = 0, column = 0)

myButton2 = Button(frame, text="지출", padx = 16, pady = 10, command = myClick)
myButton2.grid(row = 0, column = 1)

myButton3 = Button(frame, text="통계",padx = 16, pady = 10,  command = myClick)
myButton3.grid(row = 0, column = 2)
myButton4 = Button(frame, text="예비",padx = 16, pady = 10, command = myClick)
myButton4.grid(row = 0, column = 3)

root.mainloop() 