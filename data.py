# Global List Value For History DB
dates = []
money = []
types = []
otherDetails = []
expOrInc = []

# Global Money Values
expSum = 0
incSum = 0
totalMoney = 0

# treeview columns
columns = 0

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

# Global Value For Statistics Page Logo
typeLogoNum = 0

# Global Value For Assets Page Logo
commentsLogoNum = 0