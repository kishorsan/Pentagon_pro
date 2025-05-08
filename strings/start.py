# val = 'a'
# result = chr(ord(val)-32)
# print(result)

def main():
    s1 = "Abcc01 ?Dd"
    print(f"Original string: {s1}")
    resultLTU = lowerCasetoUpper(0, len(s1), s1, '')
    print(f"Lower to upper: {resultLTU}")
    resultUTL = upperCasetoLower(0, len(s1), s1, '')
    print(f"Upper to lower: {resultUTL}")
    resultSwap = SwapCase(0, len(s1), s1, '')
    print(f"Swap case: {resultSwap}")

def lowerCasetoUpper(i, N, s1, out):
    if i >= N:
        return out
    if 'a'<= s1[i] <= 'z':
        out += chr(ord(s1[i])-32)
    else:
        out += s1[i]
    return lowerCasetoUpper(i+1, N, s1, out)

def upperCasetoLower(i, N, s1, out):
    if i >= N:
        return out
    if 'A'<= s1[i] <= 'Z':
        out += chr(ord(s1[i])+32)
    else:
        out += s1[i]
    return upperCasetoLower(i+1, N, s1, out)

def SwapCase(i, N, s1, out):
    if i >= N:
        return out
    if 'A'<= s1[i] <= 'Z':
        out += chr(ord(s1[i])+32)
    elif 'a' <= s1[i] <= 'z':
        out += chr(ord(s1[i])-32)
    else:
        out += s1[i]
    return SwapCase(i+1, N, s1, out)

main()