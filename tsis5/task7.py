import re

def camel(s):
    return re.sub('_([a-z])', lambda match: match.group(1).upper(), s)

f = open('tsis5/row.txt', encoding='utf-8')
s = str(f.read())
ans = camel(s)

print(ans)