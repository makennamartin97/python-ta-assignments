class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    # Add a display_user_balance method to the User class
    def display_balance(self):
        print(f"Balance for {self.name}: {self.balance}$")
    
    # Add a make_withdrawal method to the User class
    def make_withdrawal(self, amount):
        self.balance -= amount

    def make_deposit(self, amount):
        self.balance += amount
    
    def transfer_money(self, otheruser, amount):
        otheruser.make_deposit(amount)
        self.make_withdrawal(amount)



# Create 3 instances of the User class
user1 = User('Makenna')
user2 = User('Michele')
user3 = User('Brian')

# Have the first user make 3 deposits and 1 withdrawal and 
# then display their balance
user1.make_deposit(300)
user1.make_deposit(90)
user1.make_deposit(20)
user1.make_withdrawal(5)
user1.display_balance()

# Have the second user make 2 deposits and 2 withdrawals and 
# then display their balance
user2.make_withdrawal(-1000)
user2.make_deposit(365)
user2.make_deposit(5)
user2.make_withdrawal(-12)
user2.display_balance()

# Have the third user make 1 deposits and 3 withdrawals and 
# then display their balance
user3.make_deposit(20)
user3.make_withdrawal(1)
user3.make_withdrawal(400)
user3.make_withdrawal(26)
user3.display_balance()

# BONUS: Add a transfer_money method; have the first user 
# transfer money to the third user and then print both users' balances
user1.transfer_money(user3, 400)
user1.display_balance()
user3.display_balance()