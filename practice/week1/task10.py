word = input()

letters_count = {}
for letter in word:
    if letter.isupper():
            letter = letter.lower()
    if letter in letters_count:
        letters_count[letter] += 1
    else:
        letters_count[letter] = 1


for letter in letters_count:
    print(letter, letters_count[letter])
