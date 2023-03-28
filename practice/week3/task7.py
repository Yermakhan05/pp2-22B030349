def ispolindrome(word):
    j = len(word)
    for i in range(0, int(len(word)/2), 1):
        j -= 1
        if word[i] != word[j]:
            return False
    return True

word = input()
print(ispolindrome(word))