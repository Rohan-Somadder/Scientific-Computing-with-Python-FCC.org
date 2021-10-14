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
        result += self.name.center(30, '*') + '\n'
        for item in self.ledger:
            a, m = item['amount'], item['description']
            line = ''
            if len(m) <= 23:
                line += m
                if len(str(a)) <= 7:
                    line += ' ' * \
                        (30-(len(m)+len('{0:.2f}'.format(a)))
                         ) + '{0:.2f}'.format(a)
                else:
                    line += ' '*(30-(len(m)+7)) + '{0:.2f}'.format(a)[:7]
            else:
                line += m[:23]
                if len(str(a)) <= 7:
                    line += ' '*(7-len('{0:.2f}'.format(a))
                                 ) + '{0:.2f}'.format(a)
                else:
                    line += '{0:.2f}'.format(a)[:7]
            line.rstrip()
            line += '\n'
            result += line
        result += 'Total: '+str(self.total)
        return result

    def deposit(self, amount, message=''):
        self.ledger.append({"amount": amount, "description": message})
        self.total += amount

    def withdraw(self, amount, message=''):
        if not self.check_funds(amount):
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
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.total < amount:
            return False
        else:
            return True


def create_spend_chart(categories):
    w = 3*len(categories)
    result = ''
    result += 'Percentage spent by category\n'
    prices = {}
    total = 0.0

    for item in categories:
        price = 0.0
        for entry in item.ledger:
            if entry['amount'] < 0:
                price -= entry['amount']
        prices[f'{item.name}'] = price
        total += price

    for name, cost in prices.items():
        prices[name] = int((cost/total*100)//10*10)

    for i in range(0, 101, 10)[::-1]:
        line = ''
        line += str(i).rjust(3, ' ') + '| '
        for name, perc in prices.items():
            if perc >= i:
                line += 'o  '
            else:
                line += '   '

        line += '\n'
        result += line
    result += '    ' + '-'*(w+1) + '\n'

    num = max([len(item.name) for item in categories])

    for i in range(num):
        line = '     '
        for item in categories:
            line += (item.name[i] if i < len(item.name) else ' ')
            line += '  '
        result += line
        if i < num-1:
            result += '\n'
    return result
