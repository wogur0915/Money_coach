from tkinter import *
import tkinter
from tkinter.ttk import Combobox

# Default Windows Setting
main = Tk()
main.title("House-hold Account Book System")
main.resizable(width = False, height = False)
main.geometry('832x500')
#main.iconbitmap('c:/...')

# Default Frame Setting
lobbyFrame = Frame(main)
historyFrame = Frame(main)
statisticsFrame = Frame(main)
assetsFrame = Frame(main)
settingFrame = Frame(main)

lobbyFrame.grid(row=0, column=0, sticky="nsew")
historyFrame.grid(row=0, column=0, sticky="nsew")
statisticsFrame.grid(row=0, column=0, sticky="nsew")
assetsFrame.grid(row=0, column=0, sticky="nsew")
settingFrame.grid(row=0, column=0, sticky="nsew")

def show_frame(frame):
    frame.tkraise()

# For Place
test=PhotoImage(file='1pixel.png')

# Main Page And Frames
lobbyLogo = Label(lobbyFrame, image=test, text="Logo", width=800, height=446, compound="c")
lobbyLogo.grid(row=1, column=0, columnspan=4)

for frameName in (lobbyFrame, historyFrame, statisticsFrame, assetsFrame, settingFrame):
    historyButton = Button(frameName, image=test, text="내역", width=200, height=40, compound="c", command=lambda:[show_frame(historyFrame)])
    historyButton.grid(row=0, column=0)
    statisticsButton = Button(frameName, image=test, text="통계", width=200, height=40, compound="c", command=lambda:[show_frame(statisticsFrame)])
    statisticsButton.grid(row=0, column=1)
    assetsButton = Button(frameName, image=test, text="자산", width=200, height=40, compound="c", command=lambda:[show_frame(assetsFrame)])
    assetsButton.grid(row=0, column=2)
    settingButton = Button(frameName, image=test, text="설정", width=200, height=40, compound="c", command=lambda:[show_frame(settingFrame)])
    settingButton.grid(row=0, column=3)

# Histroy Page
treeview=tkinter.ttk.Treeview(historyFrame, columns=["one", "two", "three","four"])

# DB 구성을 위한 Global List 변수 선언
dates = []
money = []
types = []
otherDetails = []
expOrInc = []

treelist=[]
i = 0

# 가계부 내역 추가 버튼
def addList() :

    # 입력받은 데이터를 Global 변수로 리턴하여 내역에 적용
    def incomeInputVal() :
        global dates, money, types, otherDetails, i
        getDate = inputDate.get()
        getExpOrInc = inputExpOrInc.get()
        getMoney = inputMoney.get()
        getInputOthers = inputOthers.get()
        getType = tegType.get()

        dates.append(getDate)
        expOrInc.append(getExpOrInc)
        money.append(getMoney)
        types.append(getType)
        otherDetails.append(getInputOthers)

        # textarea.insert(END, dates[i], END, " "*20, END, money[i], END, " "*20, END, types[i], END, " "*20, END, otherDetails[i], END, "\n")
        treeview.insert('', 'end', text=dates[i], values=[expOrInc[i], money[i], types[i], otherDetails[i]], iid=str(i))
        i = i+1

        # 데이터 추가 후 Clean
        inputDate.delete(0,END)
        inputExpOrInc.delete(0,END)
        inputMoney.delete(0,END)
        inputOthers.delete(0,END)
        tegType.delete(0,END)

    addListWin = Tk()
    addListWin.title("가계부 추가")
    addListWin.geometry("300x350")

    # 입력창
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

treeview.config(height = 18)
treeview.column("#0", width=150, anchor="center")
treeview.heading("#0", text="날짜", anchor="center")

treeview.column("#1", width=100, anchor="center")
treeview.heading("one", text="수입/지출", anchor="center")

treeview.column("#2", width=100, anchor="center")
treeview.heading("two", text="금액", anchor="center")

treeview.column("#3", width=100, anchor="center")
treeview.heading("three", text="카테고리", anchor="center")

treeview.column("#4", width=300, anchor="center")
treeview.heading("four", text="비고", anchor="center")


# for i in range(len(treelist)):
#     treeview.insert('', 'end', text=dates[i], values=treelist[i], iid=str(i))

# textarea.insert(INSERT, "날짜", INSERT, " "*20, INSERT, "금액", INSERT, " "*20, INSERT, "카테고리", INSERT, " "*20, INSERT, "비고", INSERT, "\n")
addBtn = Button(historyFrame, text = "+", font="나눔고딕 10", anchor="center", command = addList)
addBtn.config(width = 5, height = 5)
deleteBtn = Button(historyFrame, text = "삭제", font="나눔고딕 10", anchor="center")
deleteBtn.config(width = 5, height = 5)
treeview.grid(row=1, column=0, columnspan=4)
deleteBtn.grid(row=2, column=2)
addBtn.grid(row=2, column=3)
    
# Statistics Page
typeLogo = Label(statisticsFrame, image=test, text="소비 성향", width=804, height=204, compound="c", background='grey')
typeLogo.place(x=10, y=55)

Graph = Label(statisticsFrame, image=test, text="그래프", width=210, height=210, compound="c", background='grey')
Graph.place(x=10, y=274)

firstColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c", background='grey')
firstColor.place(x=238, y=276)
firstCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c", background='grey')
firstCatagory.place(x=281, y=276)
firstSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c", background='grey')
firstSum.place(x=647, y=276)

secondColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c", background='grey')
secondColor.place(x=238, y=321)
secondCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c", background='grey')
secondCatagory.place(x=281, y=321)
secondSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c", background='grey')
secondSum.place(x=647, y=321)

thridColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c", background='grey')
thridColor.place(x=238, y=366)
thridCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c", background='grey')
thridCatagory.place(x=281, y=366)
thridSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c", background='grey')
thridSum.place(x=647, y=366)

fourthColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c", background='grey')
fourthColor.place(x=238, y=411)
fourthCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c", background='grey')
fourthCatagory.place(x=281, y=411)
fourthSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c", background='grey')
fourthSum.place(x=647, y=411)

fifthColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c", background='grey')
fifthColor.place(x=238, y=456)
fifthCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c", background='grey')
fifthCatagory.place(x=281, y=456)
fifthSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c", background='grey')
fifthSum.place(x=647, y=456)

# Assets Page
assetsSum = Label(assetsFrame, image=test, text="합계", width=804, height=80, compound="c", background='grey')
assetsSum.place(x=10, y=55)
assetsPlus = Label(assetsFrame, image=test, text="수입", width=396, height=80, compound="c", background='grey')
assetsPlus.place(x=10, y=147)
assetsMinus = Label(assetsFrame, image=test, text="지출", width=396, height=80, compound="c", background='grey')
assetsMinus.place(x=418, y=147)
assetsComments = Label(assetsFrame, image=test, text="Logo", width=804, height=244, compound="c", background='grey')
assetsComments.place(x=10, y=239)

# Statistics and Assets Page Button
for frameName in (statisticsFrame, assetsFrame):
    weekButton = Button(frameName, image=test, text="주간", width=50, height=20, compound="c")
    weekButton.place(x=695, y=65)
    monthButton = Button(frameName, image=test, text="월간", width=50, height=20, compound="c")
    monthButton.place(x=755, y=65)

# Main Roop & Set First Frame
show_frame(lobbyFrame)
main.mainloop()