class CreditCard:
    def __init__(self,customer,bank,account,limit):
        self._customer=input("Enter customer name")
        self._bank=input("Enter bank name")
        self._account=int(input("Enter account no."))
        self._limit=int(input("Enter limit"))
        self._balance=int(input("None"))
    def get_customer(self):
        return self_customer
    def get_bank(self):
        return self_bank
    def get_account(self):
        return self_account
    def get_limit(self):
        return self_limit
    def get_balance(self):
        return self_balance
    def charge(self,price):
        if price+self_balance>self_limit:
            return False
        else:
            self_balance+=price
            return True
    def make_payment(self,amount):
        self_balance-=amount
# a=CreditCard()
# a.CreditCard()
# a.display()