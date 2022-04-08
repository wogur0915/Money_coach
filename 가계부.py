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

myButton6 = Button(frame, text="예산", padx = 16, pady=10, command = myClick)
myButton6.grid(row = 0, column = 4)

myButton5 = Button(root, text="  사진  ", padx = 230, pady=80, fg = "red")
myButton5.grid(row = 3, column = 0)

button_quit = Button(root, text="Exit Program", command=root.quit, padx=50, pady = 0)
button_quit.grid(padx=0, pady = 0)

root.mainloop() 