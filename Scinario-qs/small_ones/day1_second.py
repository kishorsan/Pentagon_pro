# Get Every Second Character
# def getFirst(aStr):
#     n = len(aStr)
#     newstr = ""
#     for i in range(n):
#         if i%2 == 0:
#             newstr += aStr[i]
#     return newstr

def getSecond(aStr):
    return aStr[::2]

if __name__ == '__main__':
    stri = input("Enter a string: ")
    second = getSecond(stri)
    print(second)
    # first = getFirst(stri)
    # print(first)