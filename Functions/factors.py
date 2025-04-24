class WorkWithNumbers:
    def __init__(self, value):
        self.num = value

    def main(self): # unreliable and takes too much time
        lst = []
        for i in range(1, self.num+1):
            x = self.num%i
            if x == 0:
                lst.append(i)
        return lst

    def fact(self):
        lst = []
        i = 1
        while i not in lst:
            if self.num%i == 0:
                lst.append(i)
                if self.num//i == i:
                    break
                lst.append(self.num//i)
            i += 1
        return lst

    def fact2(self):
        i = 1
        count = 0
        while i*i <= self.num:
            if self.num%i == 0:
                print(i, end=' ')
                count += 1
                if i == self.num//i:
                    break
                count += 1
                print(self.num//i, end=' ')
            i += 1
        return count
    
    # def isPrime(self, aNum):
    #     if aNum < 1:
    #         return
    #     i = 2
    #     while i * i <= aNum:
    #         if aNum%(i) == 0:
    #             return
    #         i += 1
    #     return True

    # def primeFact(self, aLst):
    #     lst = []
    #     for i in aLst:
    #         if self.isPrime(i):
    #             lst.append(i)
    #     return lst


if __name__ == '__main__':
    n = int(input("Enter a Number: "))
    num1 = WorkWithNumbers(n)

    result = num1.main()
    print(result)

    out = num1.fact()
    print(out)

    prime = num1.fact2()

    if prime == 2:
        print("\nIs a prime")
    else:
        print("\nIs not a prime")

    # ahut = num1.primeFact(final)
    # print(ahut)