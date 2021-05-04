class Budget:
    amount = 0

    def __init__(self, category):
        self.category = category

    def deposit(self, amount):
        print('You have deposited %d into %s Category' % (amount, self.category) )
        self.amount += amount

    def withdraw(self, amount):
        if(self.amount >= amount):
            print('You have withdrawn %d from %s Category' % (amount, self.category) )
            self.amount -= amount
        else:
            print('Insufficient funds in %s Category' % (self.category) )

    def balance(self):
        print('You have %d left in %s' % (self.amount, self.category) )

    def transfer(self, object, amount):
        if(self.amount >= amount):
            print('You have Transferred %d from %s to %s Category' % (amount, self.category, object.category) )
            object.amount += amount # transferred to
            self.amount -= amount # current object transferred from


food = Budget('food')
clothing = Budget('clothing')
entertainment = Budget('entertainment')

food.deposit(10000)
food.balance()
food.transfer(clothing, 3000)
food.balance()
clothing.balance()