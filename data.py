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
