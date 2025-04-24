## Find if the given number is Even or Odd

def main():
    n = int(input("Enter the number: "))
    eo1 = EvenOdd()
    isEven = eo1.EvenOrOdd(n)
    print(f"{n}", "is Even" if isEven else "is Odd")
    isPrime = eo1.prime(n)
    print(f"{n}", "is Prime" if isPrime else "is not Prime")


class EvenOdd:
    def EvenOrOdd(self, num):
        return num%2 == 0

        # if num%2 == 0:
        #     print(f"{num} is Even")
        # else:
        #     print(f"{num} is Odd")

    def prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                return False
        return True


if __name__ == '__main__':
    main()