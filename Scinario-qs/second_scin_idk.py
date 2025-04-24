# Car
isAvailable = False
class Car:
    def __init__(self, carModel, rentalPrice):
        self.carModel = carModel
        self.rentalPrice = rentalPrice
        # self.__isAvailable = False

    # @property
    # def isAvailable(self):
    #     return self.__isAvailable

    def rentCar(self):
        # if self.__isAvailable:
        global isAvailable
        if isAvailable:
            if self.rentalPrice >= 700:
                print(f"The car name is {self.carModel}")
                print(f"The car has been rented for {self.rentalPrice}")
                # print("The Car has been rented")
                # self.__isAvailable = False
                isAvailable = False
            else:
                print("Minimum rental price is 700rs")
        else:
            print("Sorry the car is not available!")

    def returnCar(self):
        global isAvailable
        print("The Car has been returned!")
        # self.__isAvailable = True
        isAvailable = True

# Default
# isAvailable = False 
c1 = Car("Toyota", 700)
while True:
    op = input("Do you want to rent the car or Return the car?\n")
    if (op == "r" or op == "Rent" or op == "rent"):
        # if c1.isAvailable:
        if isAvailable:
            carModel = input("Enter the Car you wish to rent: ")
            carRent =  int(input("Enter the Rent (min = 700rs): "))
            c1 = Car(carModel, carRent)
        c1.rentCar()
    elif (op == "R" or op == "Return" or op == "return"):
        c1.returnCar()
    else:
        break
        
