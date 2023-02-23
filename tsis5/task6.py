import re

f = open('tsis5/row.txt', encoding='utf-8')
s = str(f.read())

x = re.sub(" ", ',', s)

print(x)