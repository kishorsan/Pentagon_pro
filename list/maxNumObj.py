class MaxMin:
    def __init__(self):
        self.max = -2**31
        self.maxIndex = -1
        self.min = min = (2**31)-1
        self.minIndex = -1
        
    def createList(self):
        l1 = []
        while True:
            try:
                num = int(input("Enter a number : "))
                l1.append(num)
            except:
                return l1

    def maxNum(self, l1, max, index=-1):
        for i in range(len(l1)):
            if max < l1[i]:
                max, index = l1[i], i
        return (max, index, 1)

    def minNum(self, l1, min, index=-1):
        for i in range(len(l1)):
            if min > l1[i]:
                min, index = l1[i], i
        return (min, index, 0)

    def maxNumre(self, l1, max, index=-1, i=0):
        if i >= len(l1):
            return (max, index, 1)
        if max < l1[i]:
            max, index = l1[i], i
        return self.maxNumre(l1, max, index, i+1)

    def minNumre(self, l1, min, index=-1, i=0):
        if i >= len(l1):
            return (min, index, 0)
        if min > l1[i]:
            min, index = l1[i], i
        return self.minNumre(l1, min, index, i+1)

    def printR(self, out):
        if out[1] == -1:
            print("No ", "max" if out[2] else "min", "element as it is an empty list")
        else:
            print(f"Max" if out[2] else "Min", f"element is {out[0]} and is at index {out[1]}")
        
    
m1 = MaxMin()
lst = m1.createList()

out = m1.maxNum(lst, m1.max)
m1.printR(out)

out1 = m1.maxNumre(lst, m1.max)
m1.printR(out1)

result = m1.minNum(lst, m1.min)
m1.printR(result)

result1 = m1.minNumre(lst, m1.min)
m1.printR(result1)