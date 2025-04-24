def pattern(n, current=1):
    if current <= n:  
        print(current, end=" ")
        pattern(n, current + 1)
    print(current, end=" ")

# Call the function with n=4
pattern(4)
