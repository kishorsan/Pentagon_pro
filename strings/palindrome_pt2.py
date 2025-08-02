def main():
    s1 = input("Enter a string: ")
    result = palindrome(s1)
    print(result)

def filter_func(s1):
    s1 += ' '
    nstr = ''
    lst = []
    for i in range(len(s1)):
        if 'A' <= s1[i] <= 'Z':
            nstr += chr(ord(s1[i])+32)
        elif 'a' <= s1[i] <= 'z' or '0' <= s1[i] <= '9':
            nstr += s1[i]
        else:
            lst.append(nstr)
            nstr = ''
    return lst

def palindrome(s1):
    out = filter_func(s1)
    print(out)

if __name__ == '__main__':
    main()



