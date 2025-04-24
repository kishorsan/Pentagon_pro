l1 = [(100, "ki"), (200, "Ke"), (200, "Ko"), (1000, "ku"), (5000, "Kp")]

# Sorting the list of tuples based on the first element in descending order
l1.sort(key=lambda x: x[0], reverse=True)

print(l1)