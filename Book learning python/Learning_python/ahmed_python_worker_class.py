class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def firstName(self):
        return self.name.split()[0]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


ahmed = Worker('Ahmed Zahid', 100000)
ali = Worker('Ali Zahid', 600000)
print(ahmed.firstName())
print(ali.firstName())

ali.giveRaise(.10)
print(ali.pay)
