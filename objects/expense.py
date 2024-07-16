from datetime import date

class Expense:
    def __init__(self,amount,tDate,seller_name,description=""):
        self.amount = amount
        self.tDate = tDate
        self.seller_name = seller_name
        self.description = description


#setters (no need for getters since the values are public and this is a personal program)

    def set_amount(self,namount):
        self.amount = namount


    def set_tDate(self,ntDate):
        self.tDate = ntDate

    def set_seller_name(self,nseller_name):
        self.seller_name = nseller_name

    def set_description(self,ndescription):
        self.description = ndescription
    
    def display(self):
        print(self.seller_name)
        print(self.amount)
        print(self.tDate)
        print(self.description)

        '''

    def bark(self):
        return f"{self.name} says woof!"

    '''