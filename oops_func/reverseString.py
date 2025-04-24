# WAP a program to Reverse a string

def main():
    aStr = input("Enter a String: ")
    r1 = Reverse()
    rStr = r1.reverse(aStr)
    print(f"{aStr} Reversed is: {rStr}")
    fStr = r1.pickFirst(aStr)
    print(f"{aStr} Odd placed elements are: {fStr}")

class Reverse:
    def reverse(self, string):
        return string[::-1]

    def pickFirst(self, string):
        return string[::2]
    
if __name__ == '__main__':
    main()
    