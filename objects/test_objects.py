from expense import Expense

'''
class Expense:
    def __init__(self,amount,tDate,seller_name,description=""):
        self.amount = amount
        self.tDate = tDate
        self.seller_name = seller_name
        self.description = description
'''
#testing expense

sw = Expense(80,(12,23,1997),"sherwin_williams","paint supplies")

sw.display()