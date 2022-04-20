from tkinter import *
from tkinter.ttk import Combobox
root = Tk()
root.title("수입 / 지출")
root.geometry("300x300")

def incomeWindow() :
    types = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','경조사/회비','공과금','월급','기타']
    incomeWindow = Tk()
    incomeWindow.title("수입")
    incomeWindow.geometry("500x250")
    incomeLb1 = Label(incomeWindow, text="날짜", font="나눔고딕 15")
    incomeLb2 = Label(incomeWindow, text="금액", font="나눔고딕 15")
    incomeLb3 = Label(incomeWindow, text="분류", font="나눔고딕 15")
    incomeType = Combobox(incomeWindow, height=10, values=types)
    incomeLb1.grid(row=3, column=0)
    incomeLb2.grid(row=3, column=1)
    incomeLb3.grid(row=3, column=2)
    inputDate = Entry(incomeWindow)
    inputDate.grid(row=4, column=0)
    inputIncome = Entry(incomeWindow)
    inputIncome.grid(row=4, column=1)
    incomeType.grid(row=4, column=2)
    incomeInputBtn = Button(incomeWindow, text = "확인")
    incomeInputBtn.grid(row=5, column=1)

incomeBtn = Button(root, text = "수입", font="나눔고딕 10", command = incomeWindow)
incomeBtn.config(width = 20, height = 5)

incomeBtn.pack()


root.mainloop() #위에서 생성한 객체.mainloop