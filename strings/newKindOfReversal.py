'''
WAP to reverse the position of words without reversing the 
individual words
	I/P:
		s1 = "   hello     world"
	O/P:
		world hello
'''

def main():
    aStr = input("Enter a stirng: ")
    aStr += ' '
    result = reverse_logic(aStr, i=0, N=len(aStr), out='', nstr='')
    print(result)

def reverse_logic(s, i, N, out, nstr):
    if i >= N:
        return out
    if s[i] != ' ':
        nstr += s[i]
    elif nstr != '':
        if out == '':
            out = nstr
            nstr = ''
        else:
            out = nstr + ' ' + out
            nstr = ''
    return reverse_logic(s, i+1, N, out, nstr)

if __name__ == '__main__':
    main()