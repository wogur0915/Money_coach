from frameswitch import *
from data import *
from PIL import ImageTk, Image

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
    statisticsButton = Button(frameName, image=test, text="통계", width=200, height=40, compound="c", command=lambda:[show_statistics_frame(statisticsFrame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum)])
    statisticsButton.grid(row=0, column=1)
    assetsButton = Button(frameName, image=test, text="자산", width=200, height=40, compound="c", command=lambda:[show_assets_frame(assetsFrame, commentsLogo)])
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
popTip(addBtn, text = "추가")
deleteBtn = Button(historyFrame, text = "-", font="나눔고딕 10", anchor="center", command=lambda:[clickDelButton(treeview)])
deleteBtn.config(width = 3, height = 1)
popTip(deleteBtn, text = "삭제")
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

Graph = Label(statisticsFrame, image=test, text="그래프", width=210, height=210, compound="c", background='#e5efff')
Graph.place(x=10, y=274)

# Catagory Graph
firstGraph = Label(statisticsFrame, image=test, text="1st", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#fff700')
firstGraph.place(x=14, y=278)
secondGraph = Label(statisticsFrame, image=test, text="2nd", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#dadada')
secondGraph.place(x=14, y=323)
thirdGraph = Label(statisticsFrame, image=test, text="3rd", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#e08830')
thirdGraph.place(x=14, y=368)
fourthGraph = Label(statisticsFrame, image=test, text="4th", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#6fc6ff')
fourthGraph.place(x=14, y=413)
fifthGraph = Label(statisticsFrame, image=test, text="5th", width=202, height=20, bd=1, highlightthickness=1, highlightcolor='black', highlightbackground='black', compound="c", background='#ffd584')
fifthGraph.place(x=14, y=458)

# Catagory Ranks
firstColor = Label(statisticsFrame, image=trophy1, width=48, height=25)
firstColor.place(x=230, y=276)
firstCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 10", width=150, height=25, compound="c")
firstCatagory.place(x=283, y=276)
firstSum = Label(statisticsFrame, image=price, text="금액", width=385, height=25, compound="c")
firstSum.place(x=428, y=276)

secondColor = Label(statisticsFrame, image=trophy2, width=48, height=25)
secondColor.place(x=230, y=321)
secondCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 10", width=150, height=25, compound="c")
secondCatagory.place(x=283, y=321)
secondSum = Label(statisticsFrame, image=price, text="금액", width=385, height=25, compound="c")
secondSum.place(x=428, y=321)

thirdColor = Label(statisticsFrame, image=trophy3, width=48, height=25)
thirdColor.place(x=230, y=366)
thirdCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 10", width=150, height=25, compound="c")
thirdCatagory.place(x=283, y=366)
thirdSum = Label(statisticsFrame, image=price, text="금액", width=385, height=25, compound="c")
thirdSum.place(x=428, y=366)

fourthColor = Label(statisticsFrame, image=trophy4, width=48, height=25)
fourthColor.place(x=230, y=411)
fourthCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 10", width=150, height=25, compound="c")
fourthCatagory.place(x=283, y=411)
fourthSum = Label(statisticsFrame, image=price, text="금액", width=385, height=25, compound="c")
fourthSum.place(x=428, y=411)

fifthColor = Label(statisticsFrame, image=trophy5, width=48, height=25)
fifthColor.place(x=230, y=456)
fifthCatagory = Label(statisticsFrame, image=catagory, text="카테고리명", font="나눔스퀘어 10", width=150, height=25, compound="c")
fifthCatagory.place(x=283, y=456)
fifthSum = Label(statisticsFrame, image=price, text="금액", width=385, height=25, compound="c")
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

commentsLogo = Label(assetsFrame, image=test, width=800, height=288)
commentsLogo.place(x=12, y=195)

# Statistics and Assets Page Button
week = PhotoImage(file='src/week.png')
month = PhotoImage(file='src/month.png')

for frameName in (statisticsFrame, assetsFrame):
    weekButton = Button(frameName, image=week, highlightthickness=0, bd=0, width=58, height=28)
    weekButton.place(x=757, y=60)
    monthButton = Button(frameName, image=month, highlightthickness=0, bd=0, width=58, height=28)
    monthButton.place(x=757, y=91)
    
# Setting page 

design = Label(settingFrame, image=test, width=740, height=335, compound="c", bd=10, relief = RIDGE)
design.place(x=20, y=60) 

Us = Label(settingFrame, image=test, text=" To contact the developers : ",font = ("나눔스퀘어", 10), width=170, height=20, compound="c")
Us.place(x=600, y=420) 
hyok = Label(settingFrame, image=test, text="임재혁:",font = ("나눔스퀘어", 10), width=30, height=10, compound="c")
hyok.place(x = 655, y = 460)
github1 = Image.open('src/github1.png')
github1 = github1.resize((25, 12), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(github1)
gh = Label(settingFrame, image=my_img1)
gh.place(x=694, y=439) 
gh.bind("<Button-1>", lambda e : callback(andrewgb))
popTip(gh, text = "Github")
gh1 = Label(settingFrame, image=my_img1)
gh1.place(x=694, y=459) 


Link = Label(settingFrame, image = my_img) 
Link.place(x=50, y=420)
Link.bind("<Enter>",lambda e: label_hover(e, Link, settingFrame))
Link.bind("<Leave>", lambda e: label_hover_leave(e, Link, settingFrame))
Link.bind("<Button-1>", lambda e : callback(link))

History = Label(settingFrame, image = test, text="내역 \n 이용 안내", font=("나눔스퀘어", 18), width=120, height=65, compound="c",)
History.place(x = 45, y = 105)
Historyinfo = Label(settingFrame, image = test, text=history, font=("나눔스퀘어", 12), width=520, height=100, compound="c",)
Historyinfo.place(x = 190, y = 85)
Historyphoto = Button(settingFrame, text="?", font=("나눔스퀘어", 10), width=-140, height=-140, compound = "c", fg = "red") 
Historyphoto.place(x = 750, y = 75)
popTip(Historyphoto, text = "This window explains how to use the program.")

Statistics = Label(settingFrame, image= test, text="통계 \n 이용 안내", font=("나눔스퀘어", 18), width=100, height=40, compound="c",)
Statistics.place(x = 55, y = 205)
Statisticsinfo = Label(settingFrame, image = test, text=statistics, font=("나눔스퀘어", 12), width=520, height=100, compound="c",)
Statisticsinfo.place(x = 190, y = 185)

Assets = Label(settingFrame, image= test, text="자산 \n 이용 안내", font=("나눔스퀘어", 18), width=80, height=40, compound="c",)
Assets.place(x = 65, y = 305)
Assetsinfo = Label(settingFrame, image = test, text=statistics, font=("나눔스퀘어", 12), width=520, height=100, compound="c",)
Assetsinfo.place(x = 190, y = 275)

# Main Roop & Set First Frame
show_frame(lobbyFrame)
main.mainloop()