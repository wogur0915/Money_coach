from tkinter import *
import tkinter
from tkinter.ttk import Combobox
from tkinter import messagebox
from data import *

# Raise Frame Function
def show_frame(frame):
    frame.tkraise()
    
# History Add Button Function
def addList(treeview) :

    # Return Enter Data(Global Value) to Apply History
    def incomeInputVal() :
        global dates, money, types, otherDetails, i
        getDate = inputDate.get()
        getExpOrInc = inputExpOrInc.get()
        getMoney = inputMoney.get()
        getInputOthers = inputOthers.get()
        getType = tegType.get()

        if getDate and getExpOrInc and getMoney and getType :
            dates.append(getDate)
            expOrInc.append(getExpOrInc)
            money.append(getMoney)
            types.append(getType)
            otherDetails.append(getInputOthers)

            treeview.insert('', 'end', text=dates[i], values=[expOrInc[i], money[i], types[i], otherDetails[i]], iid=str(i))
            i = i+1

            # Clean After Data Add
            inputDate.delete(0,END)
            inputExpOrInc.delete(0,END)
            inputMoney.delete(0,END)
            inputOthers.delete(0,END)
            tegType.delete(0,END)

        else :
            warning = messagebox.askretrycancel("경고!", "입력되지 않은 정보가 있습니다!")

    addListWin = Tk()
    addListWin.title("가계부 추가")
    addListWin.geometry("300x350")

    # Enter Window
    dateLb = Label(addListWin, text="날짜", font="나눔고딕 13")
    inoutLb = Label(addListWin, text="수입/지출", font="나눔고딕 13")
    moneyLb = Label(addListWin, text="금액", font="나눔고딕 13")
    tegLb = Label(addListWin, text="카테고리", font="나눔고딕 13")
    memoLb = Label(addListWin, text="비고", font="나눔고딕 13")
    dateLb.grid(row=0, column=1, padx=100, pady=7)
    inoutLb.grid(row=2, column=1, padx=100, pady=7)
    moneyLb.grid(row=4, column=1, padx=100, pady=7)
    tegLb.grid(row=6, column=1, padx=100, pady=7)
    memoLb.grid(row=8, column=1, padx=100, pady=7)

    expOrIncTyp = ['수입', '지출']
    types = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','경조사/회비','공과금','월급','기타']

    inputDate = Entry(addListWin, justify = "center")
    inputExpOrInc = Combobox(addListWin, width=17, height=10, values=expOrIncTyp, justify = "center")
    inputMoney = Entry(addListWin, justify = "center")
    tegType = Combobox(addListWin, width=17, height=10, values=types, justify = "center")
    inputOthers = Entry(addListWin, justify = "center")
    confirmBtn = Button(addListWin, text = "확인", command = incomeInputVal)

    inputDate.grid(row=1, column=1)
    inputExpOrInc.grid(row=3, column=1)
    inputMoney.grid(row=5, column=1)
    tegType.grid(row=7, column=1)
    inputOthers.grid(row=9, column=1)
    confirmBtn.grid(row=10, column=1, padx=10, pady=10)
