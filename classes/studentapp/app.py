from re import S
from student import student

student1 = student('Ahmet', 32, 'a@gmail.com', '123Ahmet')
student2 = student('Melisa', 28, 'a@gmail.com', '123Ahmet')
print(student1.on_honor_roll())
print(student2.on_honor_roll())
