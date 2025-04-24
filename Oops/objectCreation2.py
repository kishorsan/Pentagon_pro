class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def highestMarks(self, aStudent):
        if (self.marks > aStudent.marks):
            print(f"{self.name} has the max marks")
            return self
        else:
            print(f"{aStudent.name} has the max marks")
            return aStudent

StudentList = []
s1 = Student("Kishor", 50)
StudentList.append(s1)
s2 = Student("Raj", 54)
StudentList.append(s2)
s3 = Student("Karan", 604)
StudentList.append(s3)
s4 = Student("Nagarjuna", 100)
StudentList.append(s4)
first = StudentList[0]
for i in range(1,len(StudentList)):
    first = first.highestMarks(StudentList[i])

print(first.name)
