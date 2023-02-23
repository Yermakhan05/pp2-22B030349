import re

def insert_spaces(string):
    return re.sub('(?!^)(?=[A-Z])', ' ', string)

f = open('tsis5/row.txt', encoding='utf-8')
s = str(f.read())
ans = insert_spaces(s)

print(ans)