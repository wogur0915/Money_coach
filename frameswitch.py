from function import *
import data

# Load Image Files
def load_image():
    global plan0
    
    global type0, type1, type2, type3, type4, type5, type6, type7
    
    plan0 = PhotoImage(file='src/plan0.png')
    
    type0 = PhotoImage(file='src/type0.png')
    type1 = PhotoImage(file='src/type1.png')
    type2 = PhotoImage(file='src/type2.png')
    type3 = PhotoImage(file='src/type3.png')
    type4 = PhotoImage(file='src/type4.png')
    type5 = PhotoImage(file='src/type5.png')
    type6 = PhotoImage(file='src/type6.png')
    type7 = PhotoImage(file='src/type7.png')

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
        expendsPrice = sumExpends()
    else:
        eatPrice = monthEatTotal()
        lifePrice = monthLifeTotal()
        beautyPrice = monthBeautyTotal()
        culturePrice = monthCultureTotal()
        eduPrice = monthEduTotal()
        carPrice = monthCarTotal()
        etcPrice = monthExpEtcTotal()
        expendsPrice = monthExpends()
    
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
        
    if expendsPrice == 0:
        for graph in [firstGraph, secondGraph, thirdGraph, fourthGraph, fifthGraph]:
            graph.config(width=1, text="( 0% )")
    else:
        count=0
        for graph in [firstGraph, secondGraph, thirdGraph, fourthGraph, fifthGraph]:
            if rank[count].sum == 0:
                graph.config(width=1, text="( 0% )")
            else:
                sumPercent = rank[count].sum/expendsPrice
                if int(sumPercent*202) >= 1:
                    graph.config(width=sumPercent*202, text = "( "+str(int(sumPercent*100))+"% )")
                else:
                    graph.config(width=1, text="( 0% )")
            count = count+1
    
    count=0
    for name in [firstCatagory, secondCatagory, thirdCatagory, fourthCatagory, fifthCatagory]:
        name.config(text=rank[count].name)
        count = count+1
    count=0
    for sum in [firstSum, secondSum, thirdSum, fourthSum, fifthSum]:
        sum.config(text=str(rank[count].sum)+" 원")
        count = count+1
    
    if expendsPrice == 0:
        typeLogo.config(image=type0)
    elif rank[0].name == "식비":
        typeLogo.config(image=type1)
    elif rank[0].name == "주거/통신":
        typeLogo.config(image=type2)
    elif rank[0].name == "의복/미용":
        typeLogo.config(image=type3)
    elif rank[0].name == "건강/문화":
        typeLogo.config(image=type4)
    elif rank[0].name == "교육/육아":
        typeLogo.config(image=type5)
    elif rank[0].name == "교통/차량":
        typeLogo.config(image=type6)
    elif rank[0].name == "기타":
        typeLogo.config(image=type7)
    else:
        print("Type Logo Error")
    frame.tkraise()
    
# Assets Frame Switching
def show_assets_frame(frame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice, flag):
    data.flagAM = flag
    incomesAll = sumIncomes()
    expendsAll = sumExpends()
    incomesMonth = monthIncomes()
    expendsMonth = monthExpends()
    moneyAll = incomesAll-expendsAll
    moneyMonth = incomesMonth-expendsMonth
    
    if expendsAll == 0:
        percentAll = 1
    else:
        percentAll = incomesAll/expendsAll
        
    if expendsMonth == 0:
        percentMonth = 1
    else:
        percentMonth = incomesMonth/expendsMonth
    
    if data.flagAM:
        assetsPlusPrice.config(text=(str(incomesAll)+" 원"))
        assetsMinusPrice.config(text=(str(expendsAll)+" 원"))
        assetsSumPrice.config(text=(str(moneyAll)+" 원"))
        if incomesAll == 0 and expendsAll == 0:
            data.commentsLogoNum = 0
        elif percentAll >= 1.3:
            data.commentsLogoNum = 1
        elif percentAll >= 0.7:
            data.commentsLogoNum = 2
        else:
            data.commentsLogoNum = 3
    else:
        assetsPlusPrice.config(text=(str(incomesMonth)+" 원"))
        assetsMinusPrice.config(text=(str(expendsMonth)+" 원"))
        assetsSumPrice.config(text=(str(moneyMonth)+" 원"))
        if incomesMonth == 0 and expendsMonth == 0:
            data.commentsLogoNum = 0
        elif percentMonth >= 1.3:
            data.commentsLogoNum = 1
        elif percentMonth >= 0.7:
            data.commentsLogoNum = 2
        else:
            data.commentsLogoNum = 3
        
    if data.commentsLogoNum == 0:
        commentsLogo.config(image=plan0)
    elif data.commentsLogoNum == 1:
        commentsLogo.config(image=plan0, text="1")
    elif data.commentsLogoNum == 2:
        commentsLogo.config(image=plan0, text="2")
    elif data.commentsLogoNum == 3:
        commentsLogo.config(image=plan0, text="3")
    else:
        print("Comments Logo Error")
    frame.tkraise()