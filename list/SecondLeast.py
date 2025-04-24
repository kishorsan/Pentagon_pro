def main():
    lst = createList()
    out = secondMin(lst)
    print(out)


def createList():
    l1 = []
    while True:
        try:
            l1.append(int(input("Enter a num: ")))
        except:
            return l1
        
def secondMin(lst):
    Fmin = Smin = (2**31)-1
    FminI = SminI = -1
    for i in range(len(lst)):
        if Fmin > lst[i]:
            Smin, SminI = Fmin, FminI
            Fmin, FminI = lst[i], i
        elif Fmin != lst[i] and Smin > lst[i]:
            Smin, SminI = lst[i], i
    return (f"First Minimum : {Fmin}", f"First min Index: {FminI}", f"Second min : {Smin}", f"Second min Index: {SminI}")


if __name__ == '__main__':
    main()