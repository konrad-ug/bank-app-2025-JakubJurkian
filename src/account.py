class BaseAccount:
    def __init__(self, balance=0, express_fee=0):
        self.balance = balance
        self.express_fee = express_fee
        self.historia = []

    def incoming_transfer(self, amount):
        self.balance += amount
        self.historia.append(amount)

    def outgoing_transfer(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.historia.append(-amount)
            return True
        else:
            return False

    def outgoing_transfer_express(self, amount):
        if self.balance >= amount:
            self.balance -= amount+self.express_fee
            self.historia.append(-amount)
            self.historia.append(-self.express_fee)
            return True
        else:
            return False
