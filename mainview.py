from tkinter import *

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

test=PhotoImage(file='1pixel.png')

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

typeLogo = Label(statisticsFrame, image=test, text="소비 성향", width=804, height=204, compound="c")
typeLogo.place(x=10, y=55)

# MHB's Part
for frameName in (statisticsFrame, assetsFrame):
    weekButton = Button(frameName, image=test, text="주간", width=50, height=20, compound="c")
    weekButton.place(x=695, y=65)
    monthButton = Button(frameName, image=test, text="월간", width=50, height=20, compound="c")
    monthButton.place(x=755, y=65)

Graph = Label(statisticsFrame, image=test, text="그래프", width=210, height=210, compound="c")
Graph.place(x=10, y=274)

firstColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c")
firstColor.place(x=238, y=276)
firstCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c")
firstCatagory.place(x=281, y=276)
firstSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c")
firstSum.place(x=647, y=276)

secondColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c")
secondColor.place(x=238, y=321)
secondCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c")
secondCatagory.place(x=281, y=321)
secondSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c")
secondSum.place(x=647, y=321)

thridColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c")
thridColor.place(x=238, y=366)
thridCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c")
thridCatagory.place(x=281, y=366)
thridSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c")
thridSum.place(x=647, y=366)

fourthColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c")
fourthColor.place(x=238, y=411)
fourthCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c")
fourthCatagory.place(x=281, y=411)
fourthSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c")
fourthSum.place(x=647, y=411)

fifthColor = Label(statisticsFrame, image=test, text="color", width=25, height=25, compound="c")
fifthColor.place(x=238, y=456)
fifthCatagory = Label(statisticsFrame, image=test, text="카테고리명", width=350, height=25, compound="c")
fifthCatagory.place(x=281, y=456)
fifthSum = Label(statisticsFrame, image=test, text="금액", width=166, height=25, compound="c")
fifthSum.place(x=647, y=456)

# Main Roop & Set First Frame
show_frame(lobbyFrame)
main.mainloop()
