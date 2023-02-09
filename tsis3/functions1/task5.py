def perm(cur):

    if len(s) < len(cur):
        return "-"

    if len(s) == len(cur):
        return cur

    for i in range(0, len(s), 1):
        if used[i] == 0:
            used[i] = 1
            ans.append(perm(cur + s[i]))
            used[i] = 0

s = str(input())
used = []
ans = []

for i in range(0, len(s), 1):
    used.append(0)

perm("")

for i in range(0, len(ans), 1):
    if ans[i] == None:
        continue
    print(ans[i])