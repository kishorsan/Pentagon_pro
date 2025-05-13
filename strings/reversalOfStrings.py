# WAP to reverse a complete string
def main():
    s = input("Enter a string: ")
    result1 = reverse_Increment(s, i=0, N=len(s), out='')
    print(result1)
    result2 = reverse_Decrement(s, i=0, N=len(s)-1, out='')
    print(result2)
    s += ' '
    result3 = reverse_In_Place(s, i=0, N=len(s), nstr='', out='')
    print(result3)
    pass

def reverse_Increment(s, i, N, out):
    if i >= N:
        return out
    out = s[i] + out
    return reverse_Increment(s, i+1, N, out)

def reverse_Decrement(s, i, N, out):
    if i > N:
        return out
    out += s[N]
    return reverse_Decrement(s, i, N-1, out)

def reverse_In_Place(s, i, N, nstr, out):
    if i >= N:
        return out
    if s[i] != ' ':
        nstr = s[i] + nstr
    elif nstr != '':
        if out != '':
            out += ' '+  nstr
            nstr = ''
        else:
            out = nstr
            nstr = ''
    return reverse_In_Place(s, i+1, N, nstr, out)

if __name__ == '__main__':
    main()