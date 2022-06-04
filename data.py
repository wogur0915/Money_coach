# Global List Value For History DB
dates = []
money = []
types = []
otherDetails = []
expOrInc = []

# treeview columns
columns = 0

# Sort flag
dateFlag = 1
iOrEFlag = 1
moneyFlag = 1
tagFlag = 1
otherFlag = 1

# Check All/Month
flagAM = True

# For Design Test
historySum = 0
historyPlus = 1
historyMinus = 2

class catagory(object):
    def __init__(self, name, sum):
        self.name = name
        self.sum = sum

# Global Value For Assets Page Logo
commentsLogoNum = 0

# Setting data
link = "https://github.com/KorBasilion/OSS-Basic-Project"
history = "+ 버튼을 사용해 내역을 추가할 수 있습니다.\n삭제하고 싶은 내역을 선택한 후, - 버튼을 누르거나 더블 클릭하시면 삭제하실 수 있습니다.\n입력한 내역을 저장하실 때에는 상단의 저장 버튼을 누른 후, 저장 위치를 선택하시면 저장이 가능합니다.\n 기존 데이터를 불러오실 때는 상단의 불러오기를 통해 데이터 파일을 선택하면 데이터를 불러오실 수 있습니다"
statistics = "입력하신 소비 내역 중에서 가장 많은 금액을 사용한 상위 5개의 카테고리를 확인하실 수 있습니다.\n소비 성향은 가장 많은 소비 내역을 기준으로 소비 성향을 도출해주도록 되어있습니다."
assets =  "입력하신 내역 데이터를 분석해 현재 남은 자산과 소비, 지출 총액을 보여드립니다.\n분석된 데이터를 토대로 소비에 대한 플래닝을 제시해드립니다."
