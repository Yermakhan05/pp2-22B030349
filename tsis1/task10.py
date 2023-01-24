myorder = """I have a {carname}, 
it is a {model}.
{carname} cost {0} dollors."""
prise = input()
print(myorder.format(prise, carname = "Ford", model = "Mustang"))
