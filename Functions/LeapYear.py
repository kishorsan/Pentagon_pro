def LeapYear(num):
    return num%4 == 0

def century(num):
    temp = num//100
    return temp%4 == 0

def aLeapYear(num):
    return num%400 == 0 if num%100 == 0 else num%4 == 0

def main():
    year = int(input("Enter your year: "))
    if LeapYear(year) and century(year):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")

    if aLeapYear(year):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")
    

main()
