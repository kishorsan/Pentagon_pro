def foreven(number):
    if number%2!=0:
        return True
    
n=4
i=1
while n>0:
    if foreven(i):
        print(i)
        n=n-1
    i=i+1   
    
