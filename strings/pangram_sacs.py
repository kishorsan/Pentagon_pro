'''
Today I had a question in Goldman Sachs today, its simialr to 1832. Check if the Sentence Is Pangram.

the questio is to check if the given sentence is a pangram and return a string of all the missing characters as a String.

if the input string is empty we have to return all the characters of the alphabet. But there was global variable ALPHABET with all the characters in lowercase.

Example1 : The quic brown for jumps over the lazy dog - return "kx"
Example2 : "" - return "abcdefghijklmnopqrstuvwxyz"
Example3 : The quick brown fox jumps over the lazy dog - return ""
'''

def main():
    s1 = input("Enter a string: ")
    result = pangram_missing(s1)
    print(result)

def filter_func(s):
    nstr = ''
    for i in s:
        if 'A' <= i <= 'Z':
            nstr += chr(ord(i)+32)
        elif 'a' <= i <= 'z':
            nstr += i
    return nstr

def pangram_missing(s1):
    ascii_ = [0]*26
    s1 = filter_func(s1)
    for i in range(len(s1)):
        ascii_[ord(s1[i])-97] += 1
    nstr = ''
    for i in range(len(ascii_)):
        if ascii_[i] == 0:
            nstr += chr(i + 97)
    return nstr

if __name__ == '__main__':
    main()