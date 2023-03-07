def upper_lower_letters(text):
    num_upper = 0
    num_lower = 0

    for letter in text:
        if letter.isupper():
            num_upper += 1
        elif letter.islower():
            num_lower += 1

    return num_upper, num_lower

text = input()
num_upper, num_lower = upper_lower_letters(text)
print("Number of uppercase letters:", num_upper)
print("Number of lowercase letters:", num_lower)