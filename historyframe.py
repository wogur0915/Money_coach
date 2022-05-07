from tkinter import *
import tkinter
from tkinter.ttk import Combobox

root = Tk()
textarea = Text(root)
root.title("내역")
root.geometry("300x300")

# DB 구성을 위한 Global List 변수 선언
dates = []
money = []
types = []
otherDetails =[]

# 가계부 내역 추가 버튼
def incomeWindow() :

    # 입력받은 데이터를 Global 변수로 리턴하여 내역에 적용
    def incomeInputVal() :
        global dates, money, types, otherDetails, i
        getDate = inputDate.get()
        getIncome = inputIncome.get()
        getInputOthers = inputOthers.get()
        getType = incomeType.get()

        dates.append(getDate)
        money.append(getIncome)
        types.append(getType)
        otherDetails.append(getInputOthers)

    incomeWindow = Tk()
    incomeWindow.title("수입")
    incomeWindow.geometry("300x300")

    # 입력창
    incomeLb1 = Label(incomeWindow, text="날짜", font="나눔고딕 15")
    incomeLb2 = Label(incomeWindow, text="금액", font="나눔고딕 15")
    incomeLb3 = Label(incomeWindow, text="카테고리", font="나눔고딕 15")
    incomeLb4 = Label(incomeWindow, text="비고", font="나눔고딕 15")
    incomeLb1.grid(row=0, column=1, padx=20, pady=5)
    incomeLb2.grid(row=2, column=1, padx=20, pady=5)
    incomeLb3.grid(row=4, column=1, padx=20, pady=5)
    incomeLb4.grid(row=6, column=1, padx=20, pady=5)
    inputDate = Entry(incomeWindow)
    inputIncome = Entry(incomeWindow)
    inputOthers = Entry(incomeWindow)
    types = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','경조사/회비','공과금','월급','기타']
    incomeType = Combobox(incomeWindow, height=10, values=types)
    inputDate.grid(row=1, column=1)
    inputIncome.grid(row=3, column=1)
    incomeType.grid(row=5, column=1)
    inputOthers.grid(row=7, column=1)
    incomeInputBtn = Button(incomeWindow, text = "확인", command = incomeInputVal)
    incomeInputBtn.grid(row=8, column=1)

def test() :
    print("=" * 10, "내역 출력", "="*10)
    if len(dates) == 0 :
        print("No data in Program")
    else :
        for i in range(0,len(dates)) :
            print(dates[i], money[i], types[i], otherDetails[i])

textarea.config(width = 250, height = 20)
incomeBtn = Button(root, text = "+", font="나눔고딕 10", command = incomeWindow)
incomeBtn.config(width = 5, height = 5)
deleteBtn = Button(root, text = "삭제", font="나눔고딕 10")
deleteBtn.config(width = 5, height = 5)
expenseBtn = Button(root, text = "내역출력", font="나눔고딕 10", command = test)
expenseBtn.config(width = 5, height = 5)
textarea.pack(side='top')
incomeBtn.pack(side='right')
deleteBtn.pack(side='right')
expenseBtn.pack(side='left')

root.mainloop()
