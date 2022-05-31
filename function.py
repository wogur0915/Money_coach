from tkinter import *
import tkinter
from tkinter.ttk import Combobox
from data import *
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
#declaring a class Message
class Message(object):
    def show(self, text):
        self.text = text
        if self.tipwindow or not self.text:
#A function that opens a currency converter
def openconverter():    
    root = tk.Toplevel()
    root.title('Currency Converter')
    root.resizable(FALSE, FALSE)
    root.geometry('400x210')
    #converts wons to dollars
    def won_to_dollar(f):   
        US = 0.00079
        return f*US
    #converts wons to Euros
    def won_to_EUR(f):
        EUR = 0.00074
        return f*EUR
    #converts wons to RUB
    def won_to_RUB(f):
        RUB = 0.052
        return f*RUB
    #converts wons to YEN
    def won_to_YEN(f):
        YEN = 0.10
        return f*YEN
    # This is the frame
    frame = ttk.Frame(root)
    # The field option(s)
    options = {'padx': 5, 'pady': 5}
   # converter entry
    won = tk.StringVar()
    won_entry = ttk.Entry(frame, textvariable=won)
    won_entry.grid(column=1, row=0, **options)
    # performs an operation
    def convert_button_clicked(won_to_dollar):
        try:
            f = float(won.get())
            c = won_to_dollar(f)
            result = f'{f} won = {c:.2f}'
            result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)
    # result label
    result_label = ttk.Label(frame)
    result_label.grid(row=1, columnspan=3, **options)
    # adding padding and showing it
    frame.grid(padx=10, pady=10)
    r = IntVar()
    #radio buttons to show the options and execute conversion when clicked
    Radiobutton(root, text="US", variable = r, value = 1, 
                command = lambda : convert_button_clicked(won_to_dollar)).place(x = 220, y = 20)
    Radiobutton(root, text="EUR", variable = r, value = 2, 
                command = lambda : convert_button_clicked(won_to_EUR)).place(x = 220, y = 40)
    Radiobutton(root, text="YEN", variable = r, value = 3, 
                command = lambda : convert_button_clicked(won_to_YEN)).place(x = 220, y = 60)
    Radiobutton(root, text="RUB", variable = r, value = 4, 
                command = lambda : convert_button_clicked(won_to_RUB)).place(x = 220, y = 80)
    myLabel = Label(root, text = r.get())
    myLabel.grid
    root.mainloop()
    
#A function that changes the text's color when the mouse is hovering over a button/text
def button_hover(e, name): 
    name["bg"] = "white"
    
# A function that changes the text's color when the mouse is leaving
def button_hover_leave(e, name):
    name["bg"] = "SystemButtonFace"
 
# A function that shows the user the text when the mouse is on the label    
def label_hover(e, name, settingFrame): 
    status_label = Label(settingFrame, text="https://github.com/KorBasilion/OSS-Basic-Project", font = ("Helvetica", 10))
    status_label.place(x=575, y=470)
    name["fg"] = "green"

# A function that makes the text dissappear once the mouse leaves the label      
def label_hover_leave(e, name, settingFrame):
    status_label = Label(settingFrame, text="                                                                           ")
    status_label.place(x=575, y=470)
    name["fg"] = "black"
    
# Function that opens a URL
def openNewWindow(info):
    newWindow = Toplevel()
    newWindow.title("Help")
    newWindow.grid
    Label(newWindow, text = info, fg = "red").pack()
    
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