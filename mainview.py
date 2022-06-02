from function import *
from data import *

# Default Windows Setting
main = Tk()
main.title("House-hold Account Book System")
main.resizable(width = False, height = False)
main.geometry('832x500+96+144')
#main.iconbitmap('c:/...')

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
test=PhotoImage(file='1pixel.png')

# Main Page And Frames
lobbyLogo = Label(lobbyFrame, image=test, text="Logo", width=800, height=446, compound="c")
lobbyLogo.grid(row=1, column=0, columnspan=4)

for frameName in (lobbyFrame, historyFrame, statisticsFrame, assetsFrame, settingFrame):
    historyButton = Button(frameName, image=test, text="내역", width=200, height=40, compound="c", command=lambda:[show_frame(historyFrame)])
    historyButton.grid(row=0, column=0)
    statisticsButton = Button(frameName, image=test, text="통계", width=200, height=40, compound="c", command=lambda:[show_statistics_frame(statisticsFrame, typeLogo, test)])
    statisticsButton.grid(row=0, column=1)
    assetsButton = Button(frameName, image=test, text="자산", width=200, height=40, compound="c", command=lambda:[show_assets_frame(assetsFrame, commentsLogo, test)])
    assetsButton.grid(row=0, column=2)
    settingButton = Button(frameName, image=test, text="설정", width=200, height=40, compound="c", command=lambda:[show_frame(settingFrame)])
    settingButton.grid(row=0, column=3)

# Menu Bar
menubar=tkinter.Menu(main)
menubar.add_cascade(label="저장하기", command=lambda:[saveFile()])
menubar.add_cascade(label="불러오기", command=lambda:[loadFile(main, treeview)])
main.config(menu=menubar)    
    
# History Page
treeview=tkinter.ttk.Treeview(historyFrame, columns=["dates", "expOrInc", "money", "types", "otherDetails"])
treeview.config(height = 16)
treeview.column("dates", width=165, anchor="center")
treeview.heading("dates", text="날짜", anchor="center")
treeview.column("expOrInc", width=110, anchor="center")
treeview.heading("expOrInc", text="수입/지출", anchor="center")
treeview.column("money", width=110, anchor="center")
treeview.heading("money", text="금액", anchor="center")
treeview.column("types", width=115, anchor="center")
treeview.heading("types", text="카테고리", anchor="center")
treeview.column("otherDetails", width=305, anchor="center")
treeview.heading("otherDetails", text="비고", anchor="center")

# Style of treeview
style = tkinter.ttk.Style()
style.theme_use('alt')
style.configure("Treeview.Heading", font=("나눔스퀘어 bold", 13), rowheight=20, background = "#87B3FC")
style.configure("Treeview", font=("나눔스퀘어 bold", 11), rowheight=25)
style.map("Treeview", background=[('selected', "#BEC6D5")], foreground=[('selected', "black")])

# Only Show column headings
treeview["show"] = "headings"

# For dividing section
blankLabel = Label(historyFrame, image=test, height=5, width=20, compound='c')
blankLabel.grid(row=1, column=0)

# Buttons on historyFrame
addBtn = Button(historyFrame, text = "+", font="나눔고딕 10", anchor="center", command=lambda:[addList(treeview)])
addBtn.config(width = 3, height = 1)
deleteBtn = Button(historyFrame, text = "-", font="나눔고딕 10", anchor="center", command=lambda:[clickDelButton(treeview)])
deleteBtn.config(width = 3, height = 1)
treeview.grid(row=2, column=0, columnspan=4)
addBtn.place(x=780, y=410)
deleteBtn.place(x=780, y=440)

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

commentsLogo = Label(assetsFrame, image=test, text="Logo", width=804, height=244, compound="c", background='grey')
commentsLogo.place(x=10, y=239)

# Statistics and Assets Page Button
for frameName in (statisticsFrame, assetsFrame):
    weekButton = Button(frameName, image=test, text="주간", width=50, height=20, compound="c")
    weekButton.place(x=695, y=65)
    monthButton = Button(frameName, image=test, text="월간", width=50, height=20, compound="c")
    monthButton.place(x=755, y=65)

# Main Roop & Set First Frame
show_frame(lobbyFrame)
main.mainloop()
