class Category:

# To instantiate objects
    def __init__(self, category):
        self.category = category
        self.record = []
        self.amount = 0.0

# Depositing funds to each of the categories
    def deposit (self, amount, description=""):
        self.record.append({"amount": amount, "description": description})
        self.amount += float(amount)

# Checking Funds
    def check_funds (self,amount):
        if self.amount< amount:
            return False
        else:
            return True

# Withdrawing funds from each category
    def withdraw (self, amount, description=""):
        if self.check_funds(amount) == True:
            self.amount -= float(amount)
            self.record.append({"amount":-amount, "description": description})
            return True
        else:
            return False

# Computing category balances
    def get_balance(self):
        return self.amount

# Transferring balance amounts between categories
    def transfer(self,amount,category):
        if self.check_funds(amount) == True:
            self.amount -= amount
            self.record.append({"amount":-amount, "description":"Transfer to "+ category.category})
            category.record.append({"amount": amount, "description":"Transfer from "+ self.category})
            return True
        else:
            return False

#Testing Deposit and Withdrawal
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(50.00, "Ebulo")
print(food.get_balance())

clothing = Category("Clothing")
food.transfer(300, clothing)
print(food.get_balance())