def is_palindrome(phrase):
    if phrase == phrase[::-1]:
        print(True)
    else:
        print(False)
    return 0

if __name__ == "__main__":
    phrase_input = input("Enter a phrase\n")
    is_palindrome(phrase_input)
