from tkinter import *
import tkinter
from tkinter.ttk import Combobox
from tkinter import messagebox
from data import *
from tkinter.filedialog import asksaveasfile, SaveAs
import csv

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
                addListWin.lift()
                break
            # no empty then
        
        if isOK:
            dates.append(value[0])
            expOrInc.append(value[1])
            money.append(value[2])
            types.append(value[3])
            otherDetails.append(value[4])

            treeview.insert('', 'end', values=[dates[columns], expOrInc[columns], money[columns], types[columns], otherDetails[columns]], iid=str(columns))
            columns = columns+1
            treeview.bind("<Double-1>", lambda event:[dbclickDelList(event,treeview)])

            # Clean After Data Add
            inputDate.delete(0,END)
            inputExpOrInc.delete(0,END)
            inputMoney.delete(0,END)
            inputOthers.delete(0,END)
            tegType.delete(0,END)
            
#             # for debug
#             print(dates, expOrInc, types, money, otherDetails)
            
#             # totalMoney = totalMoney + int(money[-1])
#             print("지출 합계 테스트 : ", sumExpends())
#             print("수입 합계 테스트 : ", sumIncomes())
#             print("수입 - 지출 : ", total())
#             print("-------------------") 
#             print("식비 테스트 : ", eatTotal())
#             print("주거/통신 테스트 : ", lifeTotal())    
#             print("의복/미용 테스트 : ", beautyTotal())    
#             print("건강/문화 테스트 : ", cultureTotal())        
#             print("교육/육아 테스트 : ", eduTotal())    
#             print("교통/차량 테스트 : ", carTotal())    
#             print("지출 기타 테스트 : ", expEtcTotal())
#             print("-------------------")
#             print("경조사/회비 테스트 : ", eventTotal())    
#             print("공과금 테스트 : ", utilTotal()) 
#             print("월급 테스트 : ", salaryTotal()) 
#             print("수입 기타 테스트 테스트 : ", incEtcTotal())    
            
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
    # Clear example function
    def clearDateEx(event):
        if inputDate.get() == "ex) 2022-05-31" :
            inputDate.delete(0,END)
            inputDate.configure(foreground="#000000")
    def clearMoneyEx(event):
        if inputMoney.get() == "ex) 15000" :
            inputMoney.delete(0,END)
            inputMoney.configure(foreground="#000000")

    addListWin = Tk()
    addListWin.title("가계부 추가")
    addListWin.geometry("280x350+942+190")
    addListWin.resizable(width = False, height = False)
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

    expOrIncTyp = ['지출', '수입']
    expTypes = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','기타']
    incTypes = ['경조사/회비','공과금','월급','기타']
    
    inputDate = Entry(addListWin, justify = "center")
    inputDate.insert(0,"ex) 2022-05-31")
    inputDate.configure(foreground="#747474")
    inputDate.bind("<Button-1>", clearDateEx)
    inputExpOrInc = Combobox(addListWin, width=17, height=10, values=expOrIncTyp, justify = "center", state='readonly')
    inputExpOrInc.bind("<<ComboboxSelected>>", changeSmooth)
    inputExpOrInc.current(0)
    inputMoney = Entry(addListWin, justify = "center")
    inputMoney.insert(0,"ex) 15000")
    inputMoney.configure(foreground="#747474")
    inputMoney.bind("<Button-1>", clearMoneyEx)
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
                delListWin.lift()
                break
            # no empty then,
        
        # Delete the column after verifying that the information entered by the user matches the information in the diary
        if isOK:
            if (value[0] in dates) and (value[1] in expOrInc) and (value[2] in money) and (value[3] in types) and (value[4] in otherDetails):
                if dates.index(value[0]) == expOrInc.index(value[1]) == money.index(value[2]) == types.index(value[3]) :
                    indexNum = dates.index(value[0])
                    dates[indexNum] = None
                    expOrInc[indexNum] = None
                    money[indexNum] = None
                    types[indexNum] = None
                    otherDetails[indexNum] = None
                    treeview.delete(str(indexNum))
            else :
                warning = messagebox.showwarning("경고!", "가계부에 존재하지 않는 정보입니다!")
                delListWin.lift()

            # # Clean After Data Delete
            inputDate.delete(0,END)
            inputExpOrInc.delete(0,END)
            inputMoney.delete(0,END)
            inputOthers.delete(0,END)
            tegType.delete(0,END)

    delListWin = Tk()
    delListWin.title("가계부 삭제")
    delListWin.geometry("280x350+942+190")
    delListWin.resizable(width = False, height = False)
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

    # Clear example function
    def clearDateEx(event):
        if inputDate.get() == "ex) 2022-05-31" :
            inputDate.delete(0,END)
            inputDate.configure(foreground="#000000")
    def clearMoneyEx(event):
        if inputMoney.get() == "ex) 15000" :
            inputMoney.delete(0,END)
            inputMoney.configure(foreground="#000000")

    expOrIncTyp = ['지출', '수입']   
    expTypes = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','기타']
    incTypes = ['경조사/회비','공과금','월급','기타']

    inputDate = Entry(delListWin, justify = "center")
    inputDate.insert(0,"ex) 2022-05-31")
    inputDate.configure(foreground="#747474")
    inputDate.bind("<Button-1>", clearDateEx)
    inputExpOrInc = Combobox(delListWin, width=17, height=10, values=expOrIncTyp, justify = "center", state='readonly')
    inputExpOrInc.bind("<<ComboboxSelected>>", changeSmooth)
    inputExpOrInc.current(0)
    inputMoney = Entry(delListWin, justify = "center")
    inputMoney.insert(0,"ex) 15000")
    inputMoney.configure(foreground="#747474")
    inputMoney.bind("<Button-1>", clearMoneyEx)
    tegType = Combobox(delListWin, width=17, height=7, values=expTypes, postcommand = selectCombo, justify = "center", state='readonly')
    tegType.current(0)    
    inputOthers = Entry(delListWin, justify = "center")
    confirmBtn = Button(delListWin, text = "확인", command = deleteInputVal)

    inputDate.grid(row=1, column=1)
    inputExpOrInc.grid(row=3, column=1)
    inputMoney.grid(row=5, column=1)
    tegType.grid(row=7, column=1)
    inputOthers.grid(row=9, column=1)
    confirmBtn.grid(row=10, column=1, padx=10, pady=10)
    
#-------------------------------------------------------
# delete with doublClick
def dbclickDelList(event, treeview):

    curItem = treeview.focus()
    
    if curItem : 
        # dbclickDelList
        delListWin = Tk()
        delListWin.title("가계부 삭제")
        delListWin.geometry("280x350+942+190")
        delListWin.resizable(width = False, height = False)

        # button action  
        def deleteContent() :
            global dates, money, types, otherDetails, expOrInc, columns

            selected_item = treeview.selection()[0]
            treeview.delete(selected_item)
            delListWin.destroy()

            # destroy data
            dates[int(curItem)] = None
            expOrInc[int(curItem)] = None
            money[int(curItem)] = None
            types[int(curItem)] = None
            otherDetails[int(curItem)] = None

#             # for debug
#             print(dates, expOrInc, types, money, otherDetails)

#             # totalMoney = totalMoney + int(money[-1])
#             print("지출 합계 테스트 : ", sumExpends())
#             print("수입 합계 테스트 : ", sumIncomes())
#             print("수입 - 지출 : ", total())
#             print("-------------------") 
#             print("식비 테스트 : ", eatTotal())
#             print("주거/통신 테스트 : ", lifeTotal())    
#             print("의복/미용 테스트 : ", beautyTotal())    
#             print("건강/문화 테스트 : ", cultureTotal())        
#             print("교육/육아 테스트 : ", eduTotal())    
#             print("교통/차량 테스트 : ", carTotal())    
#             print("지출 기타 테스트 : ", expEtcTotal())
#             print("-------------------")
#             print("경조사/회비 테스트 : ", eventTotal())    
#             print("공과금 테스트 : ", utilTotal()) 
#             print("월급 테스트 : ", salaryTotal()) 
#             print("수입 기타 테스트 테스트 : ", incEtcTotal())    
            
            def delAsk() :
                response = messagebox.askokcancel("가계부 삭제 경고", "선택하신 내역 정보를 삭제하시겠습니까?")
                if response == 1 :
                    deleteContent()

        # Entered window
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
        inputDate.insert( 0, treeview.item(curItem).get("values")[0] )
        inputExpOrInc = Combobox(delListWin, width=17, height=10, values=expOrIncTyp, justify = "center", state='readonly')
        inputExpOrInc.set( treeview.item(curItem).get("values")[1] )
        inputMoney = Entry(delListWin, justify = "center")
        inputMoney.insert( 0, treeview.item(curItem).get("values")[2] )
        tegType = Combobox(delListWin, width=17, height=10, values=expTypes, justify = "center", state='readonly')
        tegType.set( treeview.item(curItem).get("values")[3] )
        inputOthers = Entry(delListWin, justify = "center")
        inputOthers.insert( 0, treeview.item(curItem).get("values")[4] )
        confirmBtn = Button(delListWin, text = "확인", command = delAsk)

        # Read Only delete popup window
        inputDate.configure(state='disabled')
        inputExpOrInc.configure(state='disabled')
        inputMoney.configure(state='disabled')
        tegType.configure(state='disabled')
        inputOthers.configure(state='disabled')
        
        inputDate.grid(row=1, column=1)
        inputExpOrInc.grid(row=3, column=1)
        inputMoney.grid(row=5, column=1)
        tegType.grid(row=7, column=1)
        inputOthers.grid(row=9, column=1)
        confirmBtn.grid(row=10, column=1, padx=10, pady=10)
        
#-------------------------------------------------------
# Calculation

def sumExpends() :
    global expSum
    expSum = 0
    for i in range(columns) :
        if expOrInc[i] == "지출" :
            expSum += int(money[i])
    return expSum

def sumIncomes() :
    global incSum
    incSum = 0
    for i in range(columns) :
        if expOrInc[i] == "수입" :
            incSum += int(money[i])
    return incSum

def total() :
    global totalMoney
    totalMoney = incSum - expSum
    return totalMoney

# Expend Type Calculate
# expTypes = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','기타']
def eatTotal() :
    eatMoney = 0
    for i in range(columns) :
        if types[i] == "식비" and expOrInc[i] == "지출" :
            eatMoney += int(money[i])
    return eatMoney

def lifeTotal() :
    lifeMoney = 0
    for i in range(columns) :
        if types[i] == "주거/통신" and expOrInc[i] == "지출" :
            lifeMoney += int(money[i])
    return lifeMoney

def beautyTotal() :
    beautyMoney = 0
    for i in range(columns) :
        if types[i] == "의복/미용" and expOrInc[i] == "지출" :
            beautyMoney += int(money[i])
    return beautyMoney

def cultureTotal() :
    cultureMoney = 0
    for i in range(columns) :
        if types[i] == "건강/문화" and expOrInc[i] == "지출" :
            cultureMoney += int(money[i])
    return cultureMoney

def eduTotal() :
    eduMoney = 0
    for i in range(columns) :
        if types[i] == "교육/육아" and expOrInc[i] == "지출" :
            eduMoney += int(money[i])
    return eduMoney

def carTotal() :
    carMoney = 0
    for i in range(columns) :
        if types[i] == "교통/차량" and expOrInc[i] == "지출" :
            carMoney += int(money[i])
    return carMoney

def expEtcTotal() :
    etcMoney = 0
    for i in range(columns) :
        if types[i] == "기타" and expOrInc[i] == "지출" :
            etcMoney += int(money[i])
    return etcMoney

# incTypes = ['경조사/회비','공과금','월급','기타']
# Income Type Calculate
def eventTotal() :
    eventMoney = 0
    for i in range(columns) :
        if types[i] == "경조사/회비" and expOrInc[i] == "수입" :
            eventMoney += int(money[i])
    return eventMoney

def utilTotal() :
    utilMoney = 0
    for i in range(columns) :
        if types[i] == "공과금" and expOrInc[i] == "수입" :
            utilMoney += int(money[i])
    return utilMoney

def salaryTotal() :
    salaryMoney = 0
    for i in range(columns) :
        if types[i] == "월급" and expOrInc[i] == "수입" :
            salaryMoney += int(money[i])
    return salaryMoney

def incEtcTotal() :
    etcMoney = 0
    for i in range(columns) :
        if types[i] == "기타" and expOrInc[i] == "수입" :
            etcMoney += int(money[i])
    return etcMoney

#----------------------------------------------------
# file save by using CSV

def asksaveasfile(mode = "w", **options):
    filename = SaveAs(**options).show()
    if filename:
        return open(filename, mode, newline="")
    return None

def saveFile():
    f = asksaveasfile(mode="w", defaultextension=".csv",initialfile="house_hold_data.csv" , filetypes=(("CSV 파일", "*.csv"), ("All Files", "*.*")))
    if f is None:
        return
    wr = csv.writer(f)
    wr.writerow(["날짜", "수입/지출", "금액", "카테고리", "비고"])
    for i in range(len(dates)) :
        if dates[i] != None :
            wr.writerow([dates[i], expOrInc[i], money[i], types[i], otherDetails[i]])
    f.close()
