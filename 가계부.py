from tkinter import *

root = Tk()
root.title("House-hold account helper")
root.iconbitmap('c:/...')
def myClick():
    return
Label(root, text= "", font= ('H')).grid(row=0, column=3, padx= 40, pady= 85)

myButton1 = Button(root, text="내역",padx = 16, pady = 10,  command = myClick)
myButton1.grid(row = 10, column = 0)

myButton2 = Button(root, text="통계", padx = 16, pady = 10, command = myClick)
myButton2.grid(row = 10, column = 1)

myButton3 = Button(root, text="자산",padx = 16, pady = 10,  command = myClick)
myButton3.grid(row = 10, column = 2)
myButton4 = Button(root, text="설정",padx = 16, pady = 10, command = myClick)
myButton4.grid(row = 10, column = 3)
root.mainloop() 