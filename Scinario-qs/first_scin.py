# Product
class Product:
    def __init__(self, productId, productName, price):
        self.productId = productId
        self.productName = productName
        self.price = price
    
    def applyDiscount(self, percentage):
        return ( self.price * ( 100 - percentage ) / 100 )
    
    def __str__(self):
        L1 = [self.productId, self.productName, self.price]

        return f"ProductId: {L1[0]} \nProductName: {L1[1]} \nOriginal Price: {L1[2]}" 


product = []
discounted = []
discount = 10

while True:
    pid = int(input("Enter prod id: "))
    if pid == 000:
        break
    pName = input("Enter product name: ")
    price = int(input("Enter product price: "))
    p1 = Product(pid, pName, price)

    product.append(p1)

    disc = p1.applyDiscount(discount)
    discounted.append(disc)
    print(disc)
    
print()
for i in range(len(product)):
    print(product[i])
    print(f"Discount is {discounted[i]}\n")





    