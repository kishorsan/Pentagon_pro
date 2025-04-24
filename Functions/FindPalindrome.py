def palindrome(string):
    return string[::-1]

def main():
    aStr = input("Enter an Input: ")
    nStr = aStr.lower()
    if nStr == palindrome(nStr):
        print("Is a palindrome!!")
    else:
        print("Is not a palindrome!!")
    pass

main()

