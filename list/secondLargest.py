def main():
    lst = createList()
    print(lst)
    out = findSecondMax(lst)
    print(out)

def createList():
    l1 = []
    while True:
        try:
            num = int(input("Enter a number: "))
            l1.append(num)
        except:
            return l1

def findSecondMax(lst):
    Fmax = Smax = -2**31
    FmaxI = SmaxI = -1
    for i in range(len(lst)):
        if Fmax < lst[i]:
            Smax, SmaxI = Fmax, FmaxI
            Fmax, FmaxI = lst[i], i
        elif Fmax != lst[i] and Smax < lst[i]:
            Smax, SmaxI = lst[i], i

    return (Smax, SmaxI, Fmax, FmaxI)


if __name__ == '__main__':
    main()
    