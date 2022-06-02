from tkinter import *
import tkinter
from tkinter.ttk import Combobox
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
        
        treeview.insert('', 'end', text=dates[i], values=[expOrInc[i], money[i], types[i], otherDetails[i]], iid=str(i))
        i = i+1

        # Clean After Data Add
        inputDate.delete(0,END)
        inputExpOrInc.delete(0,END)
        inputMoney.delete(0,END)
        inputOthers.delete(0,END)
        tegType.delete(0,END)

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