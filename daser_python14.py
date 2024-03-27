# class Student:
#     def __init__(self, name, surname, grade, school_number):
#         self.name = name
#         self.surname = surname
#         self.grade = grade
#         self.school_number = school_number

# students = [
#     Student("John", "Doe", 85, "S001"),
#     Student("Jane", "Smith", 78, "S002"),
#     Student("Alice", "Johnson", 92, "S003"),
#     Student("Bob", "Brown", 80, "S004"),
#     Student("Emily", "Williams", 88, "S005"),
#     Student("Michael", "Jones", 75, "S006"),
#     Student("Emma", "Davis", 95, "S007"),
#     Student("William", "Wilson", 82, "S008"),
#     Student("Olivia", "Taylor", 90, "S009"),
#     Student("James", "Martinez", 70, "S010")
# ]

# sorted_students = sorted(students, key=lambda x: x.grade)

# for student in sorted_students:
#     print(f"{student.name} {student.surname}: Grade {student.grade}, School Number: {student.school_number}")


# class Parents:
#     def __init__(self,name,age,childrens):
#         self.name = name
#         self.age = age
#         self.childrens = childrens
#     def info1(self):
#         return f'Her name {self.name}, she is {self.age} she have {self.childrens} childrens:'

# Parents1 = Parents('Anna', 24, 2)
# Parents1.name = 'Anna'
# Parents1.age = '24'
# Parents1.childrens = '2'
# print(Parents1.info1())

# class Childrens(Parents):
#     def __init__(self, name, age, quailt, hungry):
#         self.name = name
#         self.age = age
#         self.quailt = quailt
#         self.hungry = hungry
#     def info2(self):
#         return f'My name is {self.name} i am {self.age} yers old, i {self.quailt} and i {self.hungry}:'

# Childrens1 = Childrens('Tiko', 7 , 'quailt', 'hungry')
# Childrens1.name = 'Tiko'
# Childrens1.age = '7'
# Childrens1.quailt = 'quailt'
# Childrens1.hungry = 'hungry'
# print(Childrens1.info2())