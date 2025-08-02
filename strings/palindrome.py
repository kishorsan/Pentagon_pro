def main():
    s1 = input("Enter a string: ")
    result = palindrome(s1)
    print(result)


def filter_func(s1):
    nstr = ''
    for i in range(len(s1)):
        if 'A' <= s1[i] <= 'Z':
            nstr += chr( ord(s1[i]) + 32 )
        elif 'a' <= s1[i] <= 'z' or '0' <= s1[i] <= '9':
            nstr += s1[i]
    return nstr

def palindrome(s1):
    s1 = filter_func(s1)
    i = 0
    j = len(s1) - 1
    while i <= j:
        if s1[i] != s1[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    main()