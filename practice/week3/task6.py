class Person:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        self.money = 0
    def sum_money(self):
        self.money = self.fives*5 + self.tens*10 + self.twenties*20
        return self.money 
    
def most_money(money_list):
    max = 0
    person = None
    for name in money_list:
      if name.sum_money() > max:
          max = name.sum_money()
          person = name
    return person.name

john = Person("John", 2, 2, 0)
alice = Person("Alice", 1, 3, 0)
mike = Person("Mike", 0, 0, 2)
x = most_money([john, alice, mike])
y = most_money([john, alice])
print(x, y)
