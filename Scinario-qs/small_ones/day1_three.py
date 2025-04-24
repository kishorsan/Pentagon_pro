# Extract First and Last Three Characters

def extract(aStr):
    if len(aStr) < 6:
        return "Too short"
    else:
        return f"{aStr[:3]}{aStr[-3:]}"
    
if __name__ == '__main__':
    stri = input("Enter a string: ")
    output = extract(stri)
    print(output)