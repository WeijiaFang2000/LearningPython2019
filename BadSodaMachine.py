# Author: Weijia Fang
# Title: BadSodaMachine.py
# Completion Date: Sep 2019


class BadSodaMachine:
    #Initialization
    def __init__(self, product, price):
        self.number = 0 #how many soda in the machine
        self.balance = 0 #how much money in the machine
        self.product = product #name of the product
        self.price = price #the unit price of a product

    def purchase(self,num=1):
        if self.number == 0: #When the amount of soda is 0
            return 'Product out of stock'
        if self.number < num: #When the amount of soda less than the amount the customer want
            return 'Current soda stock: ' + str(self.number)
        if self.balance < self.price*num: #When there is not enough money in the machine
            return 'Please deposit $' + str(num*self.price - self.balance)
        if self.balance > self.price*num: #When the amont of money in the machine is greater than the value of products
            change = self.balance - self.price*num
            self.balance = 0 #There should be no money left in the machine after purchase
            self.number = self.number - num #How many soda left in the machine after purchase
            return self.product + ' dispensed, take your $' + str(change) #Give change to the customer
        if self.balance == self.price*num: #When the money in the machine is equal to the value of products
            self.balance = 0 #There should be no money left in the machine after purchase
            self.number = self.number - num #How many soda left in the machine after purchase
            return self.product + ' dispensed'

    def deposit(self, amount):
        if self.number == 0: #When there is no soda in the machine
            return 'Sorry, out of stock. Take your $' + str(amount) + ' back' #Give back the money
        self.balance = self.balance + amount #Add the money in the machine and money the customer put into the machine together
        return 'Balance: $' + str(self.balance)

    def restock(self, amount):
        self.number = self.number + amount 
        return 'Current soda stock: ' + str(self.number)
    