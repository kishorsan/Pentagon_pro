def isLeapyear(year):
    return (((year % 100 != 0) and (year % 4 == 0)) or (year %400 == 0))
    
def main():
    year = int(input("Enter a year: "))
    if isLeapyear(year):
        print("Leap Year!!")
    else:
        print("Is not a Leap Year")
    
main()

