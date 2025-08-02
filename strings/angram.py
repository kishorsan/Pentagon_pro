def main():
    s1 = input("Enter a string: ")
    s2 = input("Enter another string: ")
    result = anagram(s1, s2)
    anagram_dict(s1, s2)
    print("It is an anagram" if result else "It is not an anagram")


def filter_func(s):
    nstr = ''
    for i in s:
        if 'A' <= i <= 'Z':
            nstr += i
        elif 'a' <= i <= 'z':
            nstr += chr(ord(i)-32)
    return nstr

def anagram(s1, s2):
    ascii_T1 = [0]*26
    s1 = filter_func(s1)
    s2 = filter_func(s2)
    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        ascii_T1[ord(s1[i])-65] += 1
        ascii_T1[ord(s2[i])-65] -= 1

    for i in range(len(ascii_T1)):
        if ascii_T1[i]:
            return False
    return True

def anagram_dict(s1, s2):
    d1 = {}
    s1 = filter_func(s1)
    s2 = filter_func(s2)
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        d1[s1[i]] = d1.get(s1[i], 0) + 1
        d1[s2[i]] = d1.get(s2[i], 0) - 1

    for values in d1.values():
        if values != 0:
            return False
        
    print(d1)
    pass

if __name__ == '__main__':
    main()