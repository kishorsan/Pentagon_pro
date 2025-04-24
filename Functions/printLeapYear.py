def main():
    start = int(input("Enter the start range: "))
    startTemp = start
    end = int(input("Enter the end year: "))
    print("Invalid Input" if start > end else "\n### Leap Years ###")
    while start <= end:
        if aLeapYear(start):
            print(start)
            start += 4
        else:
            start += 1
    print("\n### NON Leap Years ###")
    while startTemp <= end:
        if not aLeapYear(startTemp):
            print(startTemp)
        startTemp += 1
    

def aLeapYear(ayear):
    return ayear%400 == 0 if ayear%100 == 0 else ayear%4 == 0


main()