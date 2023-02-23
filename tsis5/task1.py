import re

f = open('tsis5/row.txt', encoding='utf-8')
s = str(f.read())

x = re.search("ab*$", s)

if x:
    print("it's a match")
else:
    print("no match found")