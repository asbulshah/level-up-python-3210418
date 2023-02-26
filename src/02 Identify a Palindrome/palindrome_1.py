import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+',phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

if __name__ == '__main__':
    phrase_input = input("Enter a phrase\n")
    print(is_palindrome(phrase_input))