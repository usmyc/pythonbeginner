# you can create your datatypes with classes. Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.
# Self is same in JS 'this'.

class student:
    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
    def on_honor_roll(self):
        if self.age >= 30:
            return True
        else:
            return False
