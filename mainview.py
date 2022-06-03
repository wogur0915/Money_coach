from frameswitch import *
import data

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

# Image Load
load_image()

# Frame Place
lobbyFrame.grid(row=0, column=0, sticky="nsew")
historyFrame.grid(row=0, column=0, sticky="nsew")
statisticsFrame.grid(row=0, column=0, sticky="nsew")
assetsFrame.grid(row=0, column=0, sticky="nsew")
settingFrame.grid(row=0, column=0, sticky="nsew")

# For Place
test=PhotoImage(file='src/1pixel.png')

# Main Page And Frames
lobbyLogo = Label(lobbyFrame, image=test, text="Logo", width=832, height=446, compound="c", background='grey')
lobbyLogo.grid(row=1, column=0, columnspan=4)

for frameName in (lobbyFrame, historyFrame, statisticsFrame, assetsFrame, settingFrame):
    historyButton = Button(frameName, image=test, text="내역", width=200, height=40, compound="c", command=lambda:[show_frame(historyFrame)])
    historyButton.grid(row=0, column=0)
    statisticsButton = Button(frameName, image=test, text="통계", width=200, height=40, compound="c", command=lambda:[show_statistics_frame(statisticsFrame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum, data.flagAM)])
    statisticsButton.grid(row=0, column=1)
    assetsButton = Button(frameName, image=test, text="자산", width=200, height=40, compound="c", command=lambda:[show_assets_frame(assetsFrame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice, data.flagAM)])
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

# Load Page Images
trophy1 = PhotoImage(file='src/goldtrophy.png')
trophy2 = PhotoImage(file='src/silvertrophy.png')
trophy3 = PhotoImage(file='src/bronzetrophy.png')
trophy4 = PhotoImage(file='src/4thtrophy.png')
trophy5 = PhotoImage(file='src/5thtrophy.png')

catagory = PhotoImage(file='src/catagory.png')
price = PhotoImage(file='src/price.png')

typeLogo = Label(statisticsFrame, image=test, text="0", width=804, height=204, compound="c")
typeLogo.place(x=10, y=55)

Graph = Label(statisticsFrame, image=test, text="", width=210, height=210, compound="c", background='#e5efff')
Graph.place(x=10, y=274)

# Catagory Graph
firstGraph = Label(statisticsFrame, image=test, text="1st", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#fff700')
firstGraph.place(x=14, y=278)
secondGraph = Label(statisticsFrame, image=test, text="2nd", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#dadada')
secondGraph.place(x=14, y=323)
thirdGraph = Label(statisticsFrame, image=test, text="3rd", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#e08830')
thirdGraph.place(x=14, y=368)
fourthGraph = Label(statisticsFrame, image=test, text="4th", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#6fc6ff')
fourthGraph.place(x=14, y=413)
fifthGraph = Label(statisticsFrame, image=test, text="5th", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#ffd584')
fifthGraph.place(x=14, y=458)

# Catagory Ranks
firstColor = Label(statisticsFrame, image=trophy1, width=48, height=25)
firstColor.place(x=230, y=276)
firstCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 11", width=150, height=25, compound="c")
firstCatagory.place(x=283, y=276)
firstSum = Label(statisticsFrame, image=price, text="금액", font="나눔스퀘어 11", width=385, height=25, compound="c")
firstSum.place(x=428, y=276)

secondColor = Label(statisticsFrame, image=trophy2, width=48, height=25)
secondColor.place(x=230, y=321)
secondCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 11", width=150, height=25, compound="c")
secondCatagory.place(x=283, y=321)
secondSum = Label(statisticsFrame, image=price, text="금액", font="나눔스퀘어 11", width=385, height=25, compound="c")
secondSum.place(x=428, y=321)

thirdColor = Label(statisticsFrame, image=trophy3, width=48, height=25)
thirdColor.place(x=230, y=366)
thirdCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 11", width=150, height=25, compound="c")
thirdCatagory.place(x=283, y=366)
thirdSum = Label(statisticsFrame, image=price, text="금액", font="나눔스퀘어 11", width=385, height=25, compound="c")
thirdSum.place(x=428, y=366)

fourthColor = Label(statisticsFrame, image=trophy4, width=48, height=25)
fourthColor.place(x=230, y=411)
fourthCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 11", width=150, height=25, compound="c")
fourthCatagory.place(x=283, y=411)
fourthSum = Label(statisticsFrame, image=price, text="금액", font="나눔스퀘어 11", width=385, height=25, compound="c")
fourthSum.place(x=428, y=411)

fifthColor = Label(statisticsFrame, image=trophy5, width=48, height=25)
fifthColor.place(x=230, y=456)
fifthCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 11", width=150, height=25, compound="c")
fifthCatagory.place(x=283, y=456)
fifthSum = Label(statisticsFrame, image=price, text="금액", font="나눔스퀘어 11", width=385, height=25, compound="c")
fifthSum.place(x=428, y=456)

# Assets Page
sumBack = PhotoImage(file='src/sum.png')
plusBack = PhotoImage(file='src/plus.png')
minusBack = PhotoImage(file='src/minus.png')
sumPriceBack = PhotoImage(file='src/sumback.png')

assetsSum = Label(assetsFrame, image=sumBack, width=732, height=60)
assetsSum.place(x=10, y=56)
assetsSumPrice = Label(assetsFrame, image=sumPriceBack, text=(str(historySum)+" 원"), font="나눔스퀘어 18 bold", width=566, height=48, compound="c")
assetsSumPrice.place(x=166, y=62)

assetsPlus = Label(assetsFrame, image=plusBack, width=396, height=60)
assetsPlus.place(x=10, y=123)
assetsPlusPrice = Label(assetsFrame, image=sumPriceBack, text=(str(historyPlus)+" 원"), font="나눔스퀘어 18 bold", width=298, height=48, compound="c")
assetsPlusPrice.place(x=98, y=129)

assetsMinus = Label(assetsFrame, image=minusBack, width=396, height=60)
assetsMinus.place(x=418, y=123)
assetsMinusPrice = Label(assetsFrame, image=sumPriceBack, text=(str(historyMinus)+" 원"), font="나눔스퀘어 18 bold", width=298, height=48, compound="c")
assetsMinusPrice.place(x=506, y=129)

commentsLogo = Label(assetsFrame, image=test, text="0", width=800, height=288, compound="c")
commentsLogo.place(x=12, y=195)

# Statistics and Assets Page Button
week = PhotoImage(file='src/week.png')
month = PhotoImage(file='src/month.png')

statisticsWeekButton = Button(statisticsFrame, image=week, highlightthickness=0, bd=0, width=58, height=28, command=lambda:[show_statistics_frame(statisticsFrame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum, True)])
statisticsWeekButton.place(x=757, y=60)
statisticsMonthButton = Button(statisticsFrame, image=month, highlightthickness=0, bd=0, width=58, height=28, command=lambda:[show_statistics_frame(statisticsFrame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum, False)])
statisticsMonthButton.place(x=757, y=91)

assetsWeekButton = Button(assetsFrame, image=week, highlightthickness=0, bd=0, width=58, height=28, command=lambda:[show_assets_frame(assetsFrame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice, True)])
assetsWeekButton.place(x=757, y=60)
assetsMonthButton = Button(assetsFrame, image=month, highlightthickness=0, bd=0, width=58, height=28, command=lambda:[show_assets_frame(assetsFrame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice, False)])
assetsMonthButton.place(x=757, y=91)

# Main Roop & Set First Frame
show_frame(lobbyFrame)
main.mainloop()