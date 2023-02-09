def Ctemp(temp):
    return (5/9)*(temp-32)

temp = float(input("Temperatura: "))
print("Centigrade temperature: {}".format(Ctemp(temp)))