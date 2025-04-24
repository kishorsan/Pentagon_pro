def charArr():
    l1 = []
    while True:
        ch = input("Enter a character: ")
        if ch=='':
            return l1
        l1.append(ch)
print(charArr())