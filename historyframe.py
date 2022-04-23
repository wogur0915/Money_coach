from tkinter import *
from tkinter.ttk import Combobox
root = Tk()
root.title("수입 / 지출")
root.geometry("300x300")

def incomeWindow() :
    def incomeInputVal() :
        getDate = inputDate.get()
        getIncome = inputIncome.get()
        getType = incomeType.get()
        print(getDate, getIncome, getType)

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
    incomeInputBtn = Button(incomeWindow, text = "확인", command = incomeInputVal)
    incomeInputBtn.grid(row=5, column=1)


def expenseWindow() :
    def expenseInputVal() :
        getDate = inputDate.get()
        getIncome = inputExpense.get()
        getType = expenseType.get()
        print(getDate, getIncome, getType)

    types = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','경조사/회비','공과금','월급','기타']
    expenseWindow = Tk()
    expenseWindow.title("지출")
    expenseWindow.geometry("500x250")
    expenseLb1 = Label(expenseWindow, text="날짜", font="나눔고딕 15")
    expenseLb2 = Label(expenseWindow, text="금액", font="나눔고딕 15")
    expenseLb3 = Label(expenseWindow, text="분류", font="나눔고딕 15")
    expenseType = Combobox(expenseWindow, height=10, values=types)
    expenseLb1.grid(row=3, column=0)
    expenseLb2.grid(row=3, column=1)
    expenseLb3.grid(row=3, column=2)
    inputDate = Entry(expenseWindow)
    inputDate.grid(row=4, column=0)
    inputExpense = Entry(expenseWindow)
    inputExpense.grid(row=4, column=1)
    expenseType.grid(row=4, column=2)
    expenseInputBtn = Button(expenseWindow, text = "확인", command = expenseInputVal)
    expenseInputBtn.grid(row=5, column=1)

incomeBtn = Button(root, text = "수입", font="나눔고딕 10", command = incomeWindow)
incomeBtn.config(width = 20, height = 5)
expenseBtn = Button(root, text = "지출", font="나눔고딕 10", command = expenseWindow)
expenseBtn.config(width = 20, height = 5)
incomeBtn.pack()
expenseBtn.pack()

root.mainloop() #위에서 생성한 객체.mainloop
