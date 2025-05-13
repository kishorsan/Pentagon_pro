# WAP to check weather the given string is a pangram or not

# A given string is said to be PANGRAM if and only if it consists of all the 26 alphabetic letters in it, ignoring the cases

def main():
    s = input("Enter a string: ")
    # inputs = ['ABCDEFGHIJKLMNOPQRSTuvwxyzzzz polsoj w w', 'The sku is blue and yellow and dark', 'qwertyuiopASDFGHJKL;.,nbvcooop0  po']
    # for i in inputs:
    result = pangram(s)
    print(result)

def filter_given(s):
    nstr = ''
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            nstr += chr(ord(s[i])+32)
        elif 'a' <= s[i] <= 'z':
            nstr += s[i]
    return nstr

def return_string(lst):
    nstr = ''
    for i in range(len(lst)):
        if lst[i] == 0:
            nstr += chr(i+97)
    return nstr

def pangram(s):
    s = filter_given(s)
    # if len(s) < 26:
    #     return False
    ascii = [0]*26
    count = 0
    for i in range(len(s)):
        index = ord(s[i]) - 97
        ascii[index] += 1
        if ascii[index] == 1:
            count += 1
    # print(f"All function: {all(ascii)}\nAny function {any(ascii)}")
    # if 0 in ascii:
    #     return False
    if count == 26:
        return True
    return return_string(ascii)
    



if __name__ == '__main__':
    main()