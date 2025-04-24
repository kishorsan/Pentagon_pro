def main():
    e1 = Even()
    num = int(input("Enter the numbe: "))
    temp = num
    print("\nUsing For loop")
    for i in range(1,num+1):
        print(e1.EvenFor(i))

    j = 1
    print("\nUsing While loop")
    while temp > 0:        
        if e1.EvenWhile(j):
            print(j)
            temp -= 1
        j += 1

    print("\nUsing Recursion !!")
    e1.EvenReccursion(1,num)

class Even:
    def EvenFor(self,num):
        return num*2

    def EvenWhile(self,num):
        return num%2 == 0

    def EvenReccursion(self,k,num):
        if num:
            if k%2 == 0:
                print(k)
                self.EvenReccursion(k+1,num-1)
            else:
                self.EvenReccursion(k+1,num)
        return


main()