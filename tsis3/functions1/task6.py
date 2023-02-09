def solve(s):
    cur = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            print(cur[::-1], end=" ")
            cur = ""
        else:
            cur = cur + s[i]
    print(cur[::-1])

s = str(input())
solve(s)