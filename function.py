from tkinter import *
import tkinter
from tkinter.ttk import Combobox
from tkinter import messagebox
from data import *

# Raise Frame Function
def show_frame(frame):
    frame.tkraise()
    
def show_statistics_frame(frame, typeLogo, image):
    if typeLogoNum == 0:
        typeLogo.config(image=image, text="0")
    elif typeLogoNum == 1:
        typeLogo.config(image=image, text="1")
    frame.tkraise()
    
def show_assets_frame(frame, commentsLogo, image):
    if commentsLogoNum == 0:
        commentsLogo.config(image=image, text="0")
    elif commentsLogoNum == 1:
        commentsLogo.config(image=image, text="1")
    frame.tkraise()

# ------------------------------------------------------------------------------------------
# History Add Button Function
def addList(treeview) :

    # Return Enter Data(Global Value) to Apply History
    def incomeInputVal() :
        global dates, money, types, otherDetails, columns
        value = [
            inputDate.get(),
            inputExpOrInc.get(),
            inputMoney.get(),
            tegType.get(),
            inputOthers.get()
            ]

        isOK = True
        for item in value[:4] :
            # if empyty spaces exist
            if not(item):
                warning = messagebox.showwarning("경고!", "입력되지 않은 정보가 있습니다!")
                isOK = False
                break
            # no empty then
        
        if isOK:
            dates.append(value[0])
            expOrInc.append(value[1])
            money.append(value[2])
            types.append(value[3])
            otherDetails.append(value[4])

            treeview.insert('', 'end', text=dates[columns], values=[expOrInc[columns], money[columns], types[columns], otherDetails[columns]], iid=str(columns))
            columns = columns+1

            # Clean After Data Add
            inputDate.delete(0,END)
            inputExpOrInc.delete(0,END)
            inputMoney.delete(0,END)
            inputOthers.delete(0,END)
            tegType.delete(0,END)
            
    # event function
    # combo box selection 
    def selectCombo():
        if inputExpOrInc.get()=="수입" :
            tegType["values"]=incTypes
        else :
            tegType["values"]=expTypes
            
    # change combobox smoothly
    def changeSmooth(event):
        if inputExpOrInc.get()=="수입":
            tegType.set(incTypes[0])
        else:
            tegType.set(expTypes[0])

    addListWin = Tk()
    addListWin.title("가계부 추가")
    addListWin.geometry("300x350+942+190")
    # addListWin.wm_attributes("-topmost", 1)  # window on first

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
    expTypes = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','기타']
    incTypes = ['경조사/회비','공과금','월급','기타']
    
    inputDate = Entry(addListWin, justify = "center")
    inputExpOrInc = Combobox(addListWin, width=17, height=10, values=expOrIncTyp, justify = "center", state='readonly')
    inputMoney = Entry(addListWin, justify = "center")
    inputExpOrInc.bind("<<ComboboxSelected>>", changeSmooth)
    inputExpOrInc.current(0)
    inputMoney = Entry(addListWin, justify = "center")
    tegType = Combobox(addListWin, width=17, height=7, values=expTypes, postcommand = selectCombo, justify = "center", state='readonly')
    tegType.current(0)
    inputOthers = Entry(addListWin, justify = "center")
    confirmBtn = Button(addListWin, text = "확인", command = incomeInputVal)

    inputDate.grid(row=1, column=1)
    inputExpOrInc.grid(row=3, column=1)
    inputMoney.grid(row=5, column=1)
    tegType.grid(row=7, column=1)
    inputOthers.grid(row=9, column=1)
    confirmBtn.grid(row=10, column=1, padx=10, pady=10)

# ------------------------------------------------------------------------------------------
# History Delete Button Function
def delList(treeview) :
    
    # Return Enter Data(Global Value) to Apply History
    def deleteInputVal() :
        global dates, money, types, otherDetails, columns
        value = [
            inputDate.get(),
            inputExpOrInc.get(),
            inputMoney.get(),
            tegType.get(),
            inputOthers.get()
            ]

        isOK = True
        for item in value[:4] :
            # if empyty spaces exist
            if not(item):
                warning = messagebox.showwarning("경고!", "입력되지 않은 정보가 있습니다!")
                isOK = False
                break
            # no empty then,
        
        if isOK:
            if (value[0] in dates) and (value[1] in expOrInc) and (value[2] in money) and (value[3] in types) and (value[4] in otherDetails):
                if dates.index(value[0]) == expOrInc.index(value[1]) == money.index(value[2]) == types.index(value[3]) :
                    indexNum = dates.index(value[0])
                    dates.pop(indexNum)
                    expOrInc.pop(indexNum)
                    money.pop(indexNum)
                    types.pop(indexNum)
                    otherDetails.pop(indexNum)
                    treeview.delete(str(indexNum))
            else :
                warning = messagebox.showwarning("경고!", "가계부에 존재하지 않는 정보입니다!")

            # Clean After Data Add
            inputDate.delete(0,END)
            inputExpOrInc.delete(0,END)
            inputMoney.delete(0,END)
            inputOthers.delete(0,END)
            tegType.delete(0,END)

    delListWin = Tk()
    delListWin.title("가계부 삭제")
    delListWin.geometry("300x350+942+190")
    # addListWin.wm_attributes("-topmost", 1)  # window on first

    # Enter Window
    dateLb = Label(delListWin, text="날짜", font="나눔고딕 13")
    inoutLb = Label(delListWin, text="수입/지출", font="나눔고딕 13")
    moneyLb = Label(delListWin, text="금액", font="나눔고딕 13")
    tegLb = Label(delListWin, text="카테고리", font="나눔고딕 13")
    memoLb = Label(delListWin, text="비고", font="나눔고딕 13")
    dateLb.grid(row=0, column=1, padx=100, pady=7)
    inoutLb.grid(row=2, column=1, padx=100, pady=7)
    moneyLb.grid(row=4, column=1, padx=100, pady=7)
    tegLb.grid(row=6, column=1, padx=100, pady=7)
    memoLb.grid(row=8, column=1, padx=100, pady=7)

    expOrIncTyp = ['지출', '수입']   
    expTypes = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','기타']
    incTypes = ['경조사/회비','공과금','월급','기타']

    inputDate = Entry(delListWin, justify = "center")
    inputExpOrInc = Combobox(delListWin, width=17, height=10, values=expOrIncTyp, justify = "center")
    inputMoney = Entry(delListWin, justify = "center")
    tegType = Combobox(delListWin, width=17, height=10, values=expTypes, justify = "center")
    inputOthers = Entry(delListWin, justify = "center")
    confirmBtn = Button(delListWin, text = "확인", command = deleteInputVal)

    inputDate.grid(row=1, column=1)
    inputExpOrInc.grid(row=3, column=1)
    inputMoney.grid(row=5, column=1)
    tegType.grid(row=7, column=1)
    inputOthers.grid(row=9, column=1)
    confirmBtn.grid(row=10, column=1, padx=10, pady=10)
