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
    
    if data.flagAM:
        eatPrice = eatTotal()
        lifePrice = lifeTotal()
        beautyPrice = beautyTotal()
        culturePrice = cultureTotal()
        eduPrice = eduTotal()
        carPrice = carTotal()
        etcPrice = expEtcTotal()
        expendsAll = sumExpends()
    else:
        eatPrice = 1
        lifePrice = 1
        beautyPrice = 1
        culturePrice = 1
        eduPrice = 1
        carPrice = 1
        etcPrice = 1
        expendsAll = sumExpends()
    
    rank = [
        catagory("식비", eatPrice),
        catagory("주거/통신", lifePrice),
        catagory("의복/미용", beautyPrice),
        catagory("건강/문화", culturePrice),
        catagory("교육/육아", eduPrice),
        catagory("교통/차량", carPrice),
        catagory("기타", etcPrice)
    ]
    
    rank = sorted(rank, key=lambda x: x.sum, reverse=True)
    
    for i in range (0,7):
        print(rank[i].name, rank[i].sum)
        
    if expendsAll == 0:
        for graph in [firstGraph, secondGraph, thirdGraph, fourthGraph, fifthGraph]:
            graph.config(width=1, text="( 0% )")
    else:
        count=0
        for graph in [firstGraph, secondGraph, thirdGraph, fourthGraph, fifthGraph]:
            if rank[count].sum == 0:
                graph.config(width=1)
            else:
                sumPercent = rank[count].sum/expendsAll
                graph.config(width=sumPercent*202, text = "( "+str(int(sumPercent*100))+"% )")
            count = count+1
    
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