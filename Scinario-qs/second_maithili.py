class Car:
    def  __init__(self,cname,cprice):
        self.cname=cname
        self.cprice=cprice
        self.isavail=False
        print("the car is =",self.cname)
        print("the price is =",self.cprice)

    def rent(self):
        if (self.isavail==True):
            print("car is available for rent")
            carname=input("enter the car name=")
            carprice=int(input("enter the amt="))
            print("the car is rented")
            self.isavail=False  
        else:
            print("sorry the car is not available")
            
    def returnCar(self):
        self.isavail=True
        print("thank you")

n1=input("enter the car name:")
n2=int(input("enter the price:"))
c1=Car(n1,n2)
while(True):
    print("1.RENT")
    print("2.RETURN")
    print("3.EXIT")
    option=int(input("enter the option"))
    if (option==1):
        c1.rent() 
    elif (option==2):
        c1.returnCar()
    elif (option==3):
        break
    else:
        print("Enter valid ip")