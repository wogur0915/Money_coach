from frameswitch import *
import data

# Default Windows Setting
main = Tk()
main.title("Money Coach")
main.resizable(width = False, height = False)
main.geometry('832x500+96+144')
#main.iconbitmap('c:/...')

# Default Frame Setting
lobbyFrame = Frame(main)
historyFrame = Frame(main)
statisticsFrame = Frame(main)
assetsFrame = Frame(main)
moreFrame = Frame(main)

# Image Load
load_image()

# Frame Place
lobbyFrame.grid(row=0, column=0, sticky="nsew")
historyFrame.grid(row=0, column=0, sticky="nsew")
statisticsFrame.grid(row=0, column=0, sticky="nsew")
assetsFrame.grid(row=0, column=0, sticky="nsew")
moreFrame.grid(row=0, column=0, sticky="nsew")

# For Place
pixelPlace=PhotoImage(file='src/1pixel.png')

# Main Page And Frames
mainLogo = PhotoImage(file='src/mainLogo.png')
lobbyLogo = Label(lobbyFrame, image=mainLogo, width=832, height=448)
lobbyLogo.grid(row=1, column=0, columnspan=20)

hisotryBtn = PhotoImage(file='src/historyBtn.png')
statisticsBtn = PhotoImage(file='src/statisticsBtn.png')
assetsBtn = PhotoImage(file='src/assetsBtn.png')
moreBtn = PhotoImage(file='src/moreBtn.png')
for frameName in (lobbyFrame, historyFrame, statisticsFrame, assetsFrame, moreFrame):
    historyButton = Button(frameName, image=hisotryBtn, width=208, height=48, highlightthickness=0, bd=0, command=lambda:[show_frame(historyFrame)])
    historyButton.grid(row=0, column=0)
    statisticsButton = Button(frameName, image=statisticsBtn, width=208, height=48, highlightthickness=0, bd=0, command=lambda:[show_statistics_frame(statisticsFrame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum, data.flagAM)])
    statisticsButton.grid(row=0, column=1)
    assetsButton = Button(frameName, image=assetsBtn, width=208, height=48, highlightthickness=0, bd=0, command=lambda:[show_assets_frame(assetsFrame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice, data.flagAM)])
    assetsButton.grid(row=0, column=2)
    moreButton = Button(frameName, image=moreBtn, width=208, height=48, highlightthickness=0, bd=0, command=lambda:[show_frame(moreFrame)])
    moreButton.grid(row=0, column=3)

# Menu Bar
menubar=tkinter.Menu(main)
menubar.add_cascade(label="새 가계부", command=lambda:[newfile(treeview)])
menubar.add_cascade(label="저장하기", command=lambda:[saveFile()])
menubar.add_cascade(label="불러오기", command=lambda:[loadFile(main, treeview)])
main.config(menu=menubar)    
    
# History Page
treeview=tkinter.ttk.Treeview(historyFrame, columns=["dates", "expOrInc", "money", "types", "otherDetails"])
treeview.config(height = 16)
treeview.column("dates", width=165, anchor="center")
treeview.heading("dates", text="날짜", anchor="center", command=lambda:[sortDate(treeview)])
treeview.column("expOrInc", width=110, anchor="center")
treeview.heading("expOrInc", text="수입/지출", anchor="center", command=lambda:[sortIorE(treeview)])
treeview.column("money", width=110, anchor="center")
treeview.heading("money", text="금액", anchor="center", command=lambda:[sortMoney(treeview)])
treeview.column("types", width=115, anchor="center")
treeview.heading("types", text="카테고리", anchor="center", command=lambda:[sortTag(treeview)])
treeview.column("otherDetails", width=305, anchor="center")
treeview.heading("otherDetails", text="비고", anchor="center", command=lambda:[sortOther(treeview)])

# Style of treeview
style = tkinter.ttk.Style()
style.theme_use('alt')
style.configure("Treeview.Heading", font=("나눔스퀘어 bold", 13), rowheight=20, background = "#87B3FC")
style.configure("Treeview", font=("나눔스퀘어", 11), rowheight=25)
style.map("Treeview", background=[('selected', "#BEC6D5")], foreground=[('selected', "black")])

# Only Show column headings
treeview["show"] = "headings"

# For dividing section
blankLabel = Label(historyFrame, image=pixelPlace, height=5, width=20, compound='c')
blankLabel.grid(row=1, column=0)

# Buttons on historyFrame
addBtnPng = PhotoImage(file='src/plusBtn.png')	
minusBtnPng = PhotoImage(file='src/minusBtn.png')	

addBtn = Button(historyFrame, image=addBtnPng, highlightthickness=0, bd=0, command=lambda:[addList(treeview)])	
addBtn.config(width = 40, height = 40)	
deleteBtn = Button(historyFrame, image=minusBtnPng, highlightthickness=0, bd=0, command=lambda:[clickDelButton(treeview)])	
deleteBtn.config(width = 40, height = 40)	
treeview.grid(row=2, column=0, columnspan=4)	
addBtn.place(x=720, y=430)	
deleteBtn.place(x=770, y=430)

# Statistics Page

# Load Page Images
trophy1 = PhotoImage(file='src/goldtrophy.png')
trophy2 = PhotoImage(file='src/silvertrophy.png')
trophy3 = PhotoImage(file='src/bronzetrophy.png')
trophy4 = PhotoImage(file='src/4thtrophy.png')
trophy5 = PhotoImage(file='src/5thtrophy.png')

catagory = PhotoImage(file='src/catagory.png')
price = PhotoImage(file='src/price.png')

typeLogo = Label(statisticsFrame, image=pixelPlace, text="", width=804, height=204, compound="c")
typeLogo.place(x=10, y=55)

Graph = Label(statisticsFrame, image=pixelPlace, text="", width=210, height=210, compound="c", background='#e5efff')
Graph.place(x=10, y=274)

# Catagory Graph
firstGraph = Label(statisticsFrame, image=pixelPlace, text="1st", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#fff700')
firstGraph.place(x=14, y=278)
secondGraph = Label(statisticsFrame, image=pixelPlace, text="2nd", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#dadada')
secondGraph.place(x=14, y=323)
thirdGraph = Label(statisticsFrame, image=pixelPlace, text="3rd", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#e08830')
thirdGraph.place(x=14, y=368)
fourthGraph = Label(statisticsFrame, image=pixelPlace, text="4th", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#6fc6ff')
fourthGraph.place(x=14, y=413)
fifthGraph = Label(statisticsFrame, image=pixelPlace, text="5th", font="나눔스퀘어 10", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#ffd584')
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

commentsLogo = Label(assetsFrame, image=pixelPlace, text="0", width=800, height=288, compound="c")
commentsLogo.place(x=12, y=195)

# Statistics and Assets Page Button
total = PhotoImage(file='src/total.png')
month = PhotoImage(file='src/month.png')

statisticsTotalButton = Button(statisticsFrame, image=total, highlightthickness=0, bd=0, width=58, height=28, command=lambda:[show_statistics_frame(statisticsFrame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum, True)])
statisticsTotalButton.place(x=757, y=60)
statisticsMonthButton = Button(statisticsFrame, image=month, highlightthickness=0, bd=0, width=58, height=28, command=lambda:[show_statistics_frame(statisticsFrame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum, False)])
statisticsMonthButton.place(x=757, y=91)

assetsTotalButton = Button(assetsFrame, image=total, highlightthickness=0, bd=0, width=58, height=28, command=lambda:[show_assets_frame(assetsFrame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice, True)])
assetsTotalButton.place(x=757, y=60)
assetsMonthButton = Button(assetsFrame, image=month, highlightthickness=0, bd=0, width=58, height=28, command=lambda:[show_assets_frame(assetsFrame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice, False)])
assetsMonthButton.place(x=757, y=91)

# Setting page
moreLogoPng = PhotoImage(file='src/moreLogo.png')
moreLogo = Label(moreFrame, image=moreLogoPng, width=811, height=426)
moreLogo.grid(row=1, column=0, pady=10, columnspan=20)

# Main Roop & Set First Frame
show_frame(lobbyFrame)
main.mainloop()
