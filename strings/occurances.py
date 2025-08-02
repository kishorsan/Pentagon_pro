#WAP to display the count of occurences of values in a given list

def main():
    # string = input("Enter a string: ")
    lst = createList()
    result = usingADict(lst)
    print(result)
    pass

def createList(): #creating a list for taking in integers
    lst = []
    while True:
        try:
            lst.append(int(input("Enter a num: ")))
        except:
            return lst

def usingDicts(string):  #for strings
    d1 = {}
    for i in range(len(string)):
        if string[i] in d1:
            d1[string[i]] += 1
        else:
            d1[string[i]] = 1
    nstr = '' 
    for i, j in d1.items():
        nstr += i + chr(j+48)
    return nstr


def usingADict(lst): # for list of intergers
    d1 = {}
    for i in lst:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    lst = []
    for key, val in d1.items():
        # if val == 1:
        #     lst.append(key)    For when we need keys with one repetetion
        # if val not in lst: # for when we want to remove all duplicate elements
        #     lst.append(key)
        if val > 1:
            lst.append(key)
    return lst
    
if __name__ == '__main__':
    main()
