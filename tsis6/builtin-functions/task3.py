def palindrome_or_not(text):
    reversed_text = text[::-1]
    return reversed_text == text


text = input()
if palindrome_or_not(text):
    print("Text is a palindrome")
else:
    print("Text is not palindrome")
      