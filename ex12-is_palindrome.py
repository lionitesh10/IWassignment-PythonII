def is_palindrome(word):
    rev_word = word[::-1]
    if word == rev_word:
        return "Palindrome "
    else:
        return "Not Palindrome "


my_word = input("Enter word : ")
print(is_palindrome(my_word))
