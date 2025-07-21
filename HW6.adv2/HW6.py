#🏧BANK ACCOUNT SYSTEM

class BanckAccount:
    bank_name="First national bank"


    def __init__(self,account_holder,initial_balance:float):
        self.account_holder=account_holder
        self.initial_balance=initial_balance
        self.transactions=[]

    def deposit(self,amount:float) -> None:
        if amount>0:
            self.initial_balance+=amount
            self.transactions.append(amount)
            print(f"deposited:{amount},new_balance:{self.initial_balance}")
        else:
            print('the amount is not valid')
    
    def withdraw(self,amount:float) -> None:
        if amount<=self.initial_balance:
            self.initial_balance-=amount
            self.transactions.append(-amount)
            print(f"withdraw:{amount} , new_balance:{self.initial_balance}")
        else:
            print('you do not have enough money in your bank account')

    def __str__(self):
        return f"Account Holder: {self.account_holder} - Balance:{self.initial_balance}"
    
    @classmethod
    def change_bank_name(cls,newname) -> None:
        cls.newname=newname
        print(f"from now on the bank name is {cls.newname}")
    
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            print('the amount is valid ')
        else:
            print(False)

    def show_transactions(self) ->None:
        print(f"transactions for {self.account_holder}")
        for transactions in self.transactions:
            print(f"{transactions}")
        


class SavingsAccount(BanckAccount):
    
    def __init__(self,account_holder,initial_balance,interest_rate:float=0.01):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
        

    def add_interest(self) -> None:
        interest=self.initial_balance*self.interest_rate
        self.initial_balance+=interest
        print(f"NEW BALANCE: {self.initial_balance}")
    
    def __str__(self) ->str:
        print(f"Account Holder :{self.account_holder}-new balance:{self.initial_balance}-interest rate:{self.interest_rate}")

    





person1=BanckAccount('Alice',0)
person2=BanckAccount('BOB',0)

person1.deposit(5000)
person1.deposit(1000)
person1.withdraw(2000)
print(person1.__str__())
person1.show_transactions()

BanckAccount.change_bank_name('Blue Bank')
BanckAccount.validate_amount(1000)

person1_saving=SavingsAccount(person1.account_holder,person1.initial_balance)
person1_saving.add_interest()
print(person1_saving.__str__())