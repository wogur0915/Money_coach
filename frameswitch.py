from function import *
import data

# Load Image Files
def load_image():
    global plan0
    global type0
    
    plan0 = PhotoImage(file='src/plan0.png')
    type0 = PhotoImage(file='src/type0.png')

# Statistics Frame Switching
def show_statistics_frame(frame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum, flag):
    data.flagAM = flag
    eatAll = eatTotal()
    lifeAll = lifeTotal()
    beautyAll = beautyTotal()
    cultureAll = cultureTotal()
    eduAll = eduTotal()
    carAll = carTotal()
    ectAll = expEctTotal()
    incomesAll = sumIncomes()
    expendsAll = sumExpends()
    
    if data.typeLogoNum == 0:
        typeLogo.config(image=type0)
    elif data.typeLogoNum == 1:
        typeLogo.config(image=type0, text="1")
    frame.tkraise()
    
# Assets Frame Switching
def show_assets_frame(frame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice, flag):
    data.flagAM = flag
    incomesAll = sumIncomes()
    expendsAll = sumExpends()
    moneyAll = incomesAll-expendsAll
    if expendsAll == 0:
        percentAll = 2
    else:
        percentAll = incomesAll/expendsAll
    
    if data.flagAM:
        assetsPlusPrice.config(text=(str(incomesAll)+" 원"))
        assetsMinusPrice.config(text=(str(expendsAll)+" 원"))
        assetsSumPrice.config(text=(str(moneyAll)+" 원"))
        if incomesAll == 0 and expendsAll == 0:
            data.commentsLogoNum = 0
        elif percentAll >= 1.4:
            data.commentsLogoNum = 1
        elif percentAll >= 0.6:
            data.commentsLogoNum = 2
        else:
            data.commentsLogoNum = 3
    else:
        assetsPlusPrice.config(text=("1 원"))
        assetsMinusPrice.config(text=("1 원"))
        assetsSumPrice.config(text=("1 원"))
        
    if data.commentsLogoNum == 0:
        commentsLogo.config(image=plan0)
    elif data.commentsLogoNum == 1:
        commentsLogo.config(image=plan0, text="1")
    elif data.commentsLogoNum == 2:
        commentsLogo.config(image=plan0, text="2")
    elif data.commentsLogoNum == 3:
        commentsLogo.config(image=plan0, text="3")
    frame.tkraise()