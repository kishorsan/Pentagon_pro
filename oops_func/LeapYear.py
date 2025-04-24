def main():
    year = int(input("Enter a year: "))
    leap = Leap(year)
    if leap.Leapyear() and leap.CenturyYear():
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")

    if leap.aLeapYearCompiled():
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")
    pass

class Leap:
    def __init__(self, num):
        self.num = num

    def Leapyear(self):
        return self.num%4 == 0

    def CenturyYear(self):
        tempYear = self.num//100
        return tempYear%4 == 0
    
    def aLeapYearCompiled(self):
        return self.num%400 == 0 if self.num%100 == 0 else self.num%4 == 0

main()