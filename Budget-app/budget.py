class Category:
    ledger: list[dict]
    total: float
    name: str

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0.0

    def __str__(self):
        result = ''
        result += '*'*((30-len(self.name))//2+(1 if len(self.name) % 2 == 0 else 0)) + \
            self.name + '*'*((30-len(self.name))//2)
        for a, m in zip(self.ledger):
            line = ''
            if len(m) <= 23:
                line += m
                if len(str(a)) <= 7:
                    line += ' '*(30-len(m)+len(str(a))) + str(m)
                else:
                    line += ' '*(30-len(m)+7) + str(a)[:7]
            else:
                line += m[:23]
                if len(str(a)) <= 7:
                    line += ' '*(7-len(str(a))) + str(m)
                else:
                    line += str(a)[:7]
            line += '\n'
            result += line
        result += 'Total: '+str(self.total)
        return result

    def deposit(self, amount, message=''):
        self.ledger.append({"amount": amount, "description": message})
        self.total += amount

    def withdraw(self, amount, message=''):
        if self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": (-1*amount), "description": message})
            self.total = self.total - amount
            return True

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from{self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.total < amount:
            return False
        else:
            return True


def create_spend_chart(categories):
    w = 3*len(categories) + 1
    result = ''
    result += 'Percentage spent by category\n'
    prices = {}
    total = 0.0
    for item in categories:
        price = 0.0
        for entry in item.ledger:
            if entry['amount']<0:
                price -= entry['amount']
        prices[f'{item.name}'] = price
        total += price 
