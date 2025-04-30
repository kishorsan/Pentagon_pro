def createList(): # creating an integer array dynamically 
    lst = []
    while True:
        try:
            lst.append(int(input()))
        except:
            return lst # returnig after the exception is raised

