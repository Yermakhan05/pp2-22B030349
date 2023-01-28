quiz = [
    ("1.Which? ", {"1444", "1555", "1666"}),
    ("2.When? ", {"Then", "Than"}),
    ("3.Who? ", {"Tokaev", "Nazarbaev"})
]
quetion = 0
correct = 0
while quetion != len(quiz):
    answer = input(quiz[quetion][0])
    if answer in quiz[quetion][1]:
        correct += 1
    quetion += 1

prosent = float((correct/quetion)*100)
if prosent >= 70:
    print("Congrats, you won with {}% correctness".format(prosent))
else:
    print("You lost! You got only {}% correctness".format(prosent))
