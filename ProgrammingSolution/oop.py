#----------------Object Oriented Programming Exercise Solution--------------

# 1. Create a class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


# 2. Add a method to calculate average grade
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)


# 3. method greet()
class Student:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello, my name is", self.name)


# 4. method get_name()
class Student:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name


# 5. Access & modify attributes
s = Student("Mark", 20)
print("Before:", s.name)
s.name = "Sadhu"
print("After:", s.name)


# 6. Constructor for Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# 7. Constructor for Book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


# 8. Constructor for Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


# 9. Polymorphism / Overloading (Python handles by default arguments)
class MathOps:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        return a + b + c

obj = MathOps()
print(obj.add(2, 3))
print(obj.add(2, 3, 4))


# 10. Access Modifiers
class Test:
    def __init__(self):
        self.public = "I am public"
        self.__private = "I am private"

t = Test()
print(t.public)
# print(t.__private)  # Error in strict OOP langs


# 11. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def show(self):
        print("Balance:", self.__balance)


# 12. Getter & Setter
class Account:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        self.__balance = amount


# 13. Static Method
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @staticmethod
    def get_count():
        print("Total objects:", Counter.count)


# 14. Operator Overloading (+)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = v1 + v2
print(v3.x, v3.y)


# 15. Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")


# 16. Abstract Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w


# 17. Simple Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# 18. Multiple Inheritance
class Animal:
    def eat(self):
        print("Animal eating")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

class Cat(Animal):
    def meow(self):
        print("Cat meowing")


# 19. Inheritance with multiple bases
class Teacher:
    def teach(self):
        print("Teaching")

class Coach:
    def coach(self):
        print("Coaching")

class SportsTeacher(Teacher, Coach):
    pass
