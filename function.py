from module import *
from data import *
import webbrowser
import tkinter as tk
from tkinter import ttk
import time
#declaring a class Message
class Message(object):

    def show(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.tool.bbox("insert")
        x = x + self.tool.winfo_rootx() + 60
        y = y + cy + self.tool.winfo_rooty() + 23
        self.tipwindow = tw = Toplevel(self.tool)
        message = Label(tw,borderwidth=1, text=self.text, fg = "black", justify=LEFT, background = "white", font=("Times", "12"), relief=SOLID)
        message.pack(ipadx=4)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        
    def hide(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
        
    def __init__(self, tool):
        self.tool = tool
        self.tipwindow = 0
        self.id = 0
        self.x = self.y = 0

def popTip(tool, text):
    toolTip = Message(tool)
    def enter(event):
        time.sleep(0.4)
        toolTip.show(text)
    def leave(event):
        toolTip.hide()
    tool.bind('<Enter>', enter)
    tool.bind('<Leave>', leave)
    
#A function that changes the text's color when the mouse is hovering over a button/text
def button_hover(e, name): 
    name["bg"] = "white"
    
# A function that changes the text's color when the mouse is leaving
def button_hover_leave(e, name):
    name["bg"] = "SystemButtonFace"
 
# A function that shows the user the text when the mouse is on the label    
def label_hover(e, name, Frame): 
    status_label = Label(Frame, text="https://github.com/KorBasilion/OSS-Basic-Project", font = ("Helvetica", 10))
    status_label.place(x=20, y=470)
    name["fg"] = "green"

# A function that makes the text dissappear once the mouse leaves the label      
def label_hover_leave(e, name, Frame):
    status_label = Label(Frame, text="                                                                           ")
    status_label.place(x=20, y=470)
    name["fg"] = "black"
    
# Function that opens a window
def openNewWindow(info, photo):
    newWindow = Toplevel()
    newWindow.resizable(FALSE,FALSE)
    newWindow.title("    ")
    newWindow.grid
    Label(newWindow, image = photo, text = info, fg = "red").pack()
           
 # Function that opens URL links   
def callback(url):
   webbrowser.open_new_tab(url) 

# Raise Frame Function
def show_frame(frame):
    frame.tkraise()

# History Add Button Function
def addList(treeview) :

    # Return Enter Data(Global Value) to Apply History
    def incomeInputVal() :
        global dates, money, types, otherDetails, expOrInc, columns
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
        if inputDate.get() == "yyyy-mm-dd" :
            inputDate.delete(0,END)
            inputDate.configure(foreground="#000000")
    def clearMoneyEx(event):
        if inputMoney.get() == "숫자만 입력해주세요" :
            inputMoney.delete(0,END)
            inputMoney.configure(foreground="#000000")
            
    addListWin = Tk()
    addListWin.title("가계부 추가")
    addListWin.geometry("280x350+942+190")
    addListWin.resizable(width = False, height = False)
    # addListWin.wm_attributes("-topmost", 1)  # window on first

   # Enter Window
    dateLb = Label(addListWin, text="날짜", font=("나눔스퀘어 bold", 13))
    inoutLb = Label(addListWin, text="수입/지출", font=("나눔스퀘어 bold", 13))
    moneyLb = Label(addListWin, text="금액", font=("나눔스퀘어 bold", 13))
    tegLb = Label(addListWin, text="카테고리", font=("나눔스퀘어 bold", 13))
    memoLb = Label(addListWin, text="비고", font=("나눔스퀘어 bold", 13))
    dateLb.grid(row=0, column=1, padx=100, pady=7)
    inoutLb.grid(row=2, column=1, padx=100, pady=7)
    moneyLb.grid(row=4, column=1, padx=100, pady=7)
    tegLb.grid(row=6, column=1, padx=100, pady=7)
    memoLb.grid(row=8, column=1, padx=100, pady=7)

    expOrIncTyp = ['지출', '수입']   
    expTypes = ['식비','주거/통신','의복/미용','건강/문화','교육/육아','교통/차량','기타']
    incTypes = ['경조사/회비','공과금','월급','기타']

    inputDate = Entry(addListWin, font=("나눔스퀘어 bold", 10), justify = "center")
    inputDate.insert(0,"yyyy-mm-dd")
    inputDate.configure(foreground="#747474")
    inputDate.bind("<Button-1>", clearDateEx)
    inputExpOrInc = Combobox(addListWin, width=17, height=10, values=expOrIncTyp, justify = "center", font=("나눔스퀘어 bold", 10), state='readonly')
    inputExpOrInc.option_add('*TCombobox*Listbox.Justify', 'center')    
    inputExpOrInc.bind("<<ComboboxSelected>>", changeSmooth)
    inputExpOrInc.current(0)
    inputMoney = Entry(addListWin, font=("나눔스퀘어 bold", 10), justify = "center")
    inputMoney.insert(0,"숫자만 입력해주세요")
    inputMoney.configure(foreground="#747474")
    inputMoney.bind("<Button-1>", clearMoneyEx)
    tegType = Combobox(addListWin, width=17, height=7, values=expTypes, postcommand = selectCombo, justify = "center", font=("나눔스퀘어 bold", 10), state='readonly')
    tegType.option_add('*TCombobox*Listbox.Justify', 'center')
    tegType.current(0)
    inputOthers = Entry(addListWin, font=("나눔스퀘어 bold", 10), justify = "center")
    confirmBtn = Button(addListWin, text = "확인", font=("나눔스퀘어 bold", 10), command = incomeInputVal)


    inputDate.grid(row=1, column=1)
    inputExpOrInc.grid(row=3, column=1)
    inputMoney.grid(row=5, column=1)
    tegType.grid(row=7, column=1)
    inputOthers.grid(row=9, column=1)
    confirmBtn.grid(row=10, column=1, padx=10, pady=10)

# ------------------------------------------------------------------------------------------
# History delete with doublClick
def dbclickDelList(event, treeview):

    curItem = treeview.focus()
    
    if curItem : 
        # button action 
        def deleteContent() :
            global dates, money, types, otherDetails, expOrInc

            selected_item = treeview.selection()[0]
            treeview.delete(selected_item)

            # destroy data
            dates[int(curItem)] = None
            expOrInc[int(curItem)] = None
            money[int(curItem)] = None
            types[int(curItem)] = None
            otherDetails[int(curItem)] = None

        response = messagebox.askokcancel("가계부 삭제 경고", "선택하신 내역 정보를 삭제하시겠습니까?")
        if response == 1 :
            deleteContent()
    
#-------------------------------------------------------
# History Delete Button Function
def clickDelButton(treeview):

    curItem = treeview.focus()
    
    if curItem : 
        # button action 
        def deleteContent() :
            global dates, money, types, otherDetails, expOrInc

            selected_item = treeview.selection()[0]
            treeview.delete(selected_item)

            # destroy data
            dates[int(curItem)] = None
            expOrInc[int(curItem)] = None
            money[int(curItem)] = None
            types[int(curItem)] = None
            otherDetails[int(curItem)] = None
            
        response = messagebox.askokcancel("가계부 삭제 경고", "선택하신 내역 정보를 삭제하시겠습니까?")
        if response == 1 :
            deleteContent()
        
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

def loadFile(main, treeview):
    global dates, money, types, otherDetails, expOrInc, columns
    columns = 0
    temp = []
    del dates[:], money[:], types[:], otherDetails[:], expOrInc[:]

    file = askopenfilename(initialdir="/desktop", title="가계부 데이터 파일 선택", filetypes=(("CSV 파일", "*.csv"), ("All Files", "*.*")))
    f = open(file,"r")
    rd = csv.reader(f)
    treeview.delete(*treeview.get_children())
    treeview.update()
    for i in rd :
        temp.append(i)
    if len(temp) > 1 :
        for j in range(1, len(temp)) :
            dates.append(temp[j][0])
            expOrInc.append(temp[j][1])
            money.append(temp[j][2])
            types.append(temp[j][3])
            otherDetails.append(temp[j][4])
            treeview.insert('', 'end', values=[dates[columns], expOrInc[columns], money[columns], types[columns], otherDetails[columns]], iid=str(columns))
            columns = columns + 1
    f.close()
    treeview.bind("<Double-1>", lambda event:[dbclickDelList(event,treeview)])
    