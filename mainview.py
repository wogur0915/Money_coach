from function import *
from data import *
import time

# Default Windows Setting
main = Tk()
main.title("House-hold Account Book System")
main.resizable(width = False, height = False)
main.geometry('832x500')
#main.iconbitmap('c:/...')
#Theme for the program
style = ttk.Style(main)
style.theme_names()
current_theme = style.theme_use()
style.theme_use("clam")

# Default Frame Setting
lobbyFrame = Frame(main)
historyFrame = Frame(main)
statisticsFrame = Frame(main)
assetsFrame = Frame(main)
settingFrame = Frame(main)

# Frame Place
lobbyFrame.grid(row=0, column=0, sticky="nsew")
historyFrame.grid(row=0, column=0, sticky="nsew")
statisticsFrame.grid(row=0, column=0, sticky="nsew")
assetsFrame.grid(row=0, column=0, sticky="nsew")
settingFrame.grid(row=0, column=0, sticky="nsew")

# For Place
test=PhotoImage(file='or.png')

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

# History Page
treeview=tkinter.ttk.Treeview(historyFrame, columns=["one", "two", "three","four"])
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

addBtn = Button(historyFrame, text = "+", font="나눔고딕 10", anchor="center", command=lambda:[addList(treeview)])
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
    
# Setting page 

design = Label(settingFrame, image=test, width=740, height=320, compound="c", bd=10, relief = RIDGE)
design.place(x=20, y=60) 
   
Help = Label(settingFrame, image=test, text="Help", font = ("Helvetica", 25), width=200, height=40, compound="c", activeforeground = "green")
Help.place(x=310, y=115)

Us = Label(settingFrame, image=test, text="About Us: We are CBNU students currently majoring in computer science. \nThis program is our first project that we made together. \n To contact us: andrewendlesss@gmail.com \n 희범의 email \n 재혁의 email \n License: MIT",font = ("Helvetica", 10), width=350, height=80, compound="c")
Us.place(x=315, y=340) 

Version = Label(settingFrame, image=test, text= "BETA 0.1.0", width=190, height=30, compound="c", fg="light green", font=("Arial", 15), relief = RIDGE)
Version.place(x=500, y=400) 

Link = Button(settingFrame, text="Our GitHub repository", font=("Helvetica", 20),) 
Link.place(x=30, y=430)
Link.bind("<Enter>", lambda e: label_hover(e, Link, settingFrame))
Link.bind("<Leave>", lambda e: label_hover_leave(e, Link, settingFrame))
Link.bind("<Button-1>", lambda e : callback(link))

# Main Roop & Set First Frame
show_frame(lobbyFrame)
main.mainloop()
