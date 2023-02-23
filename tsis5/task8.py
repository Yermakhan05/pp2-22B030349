import re

f = open('tsis5/row.txt', encoding='utf-8')
s = str(f.read())
ans = re.findall('[A-Z][a-z]*', s)

print(ans)