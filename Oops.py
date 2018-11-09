"""
Python OOPs Concepts

Is Python Object Oriented?
Yes. Python is an object oriented programming language. You can write programs in Python either in functional way or
in object oriented way.

What is OOP?
There are mainly two types of programming, which are procedure oriented and object oriented.
Object oriented programming (OOP) is a programming paradigm based on the concept of objects and data.
In object oriented programming, every entity is treated as an object.

Classes in Python
A class can be defined as an object's blueprint, description or definition.
We can use the same class as a blueprint for creating multiple different objects.
Classes are created using the keyword 'Class' and an intended block which contains class methods.

The __init__  method
Class definitions should start with the __init__ method (stands for initialization method) .
This method is called when an object of the class is created.  __init__ method is the constructor of the class.
All methods must have 'self ' as their first parameter. 'self' refers to the instance calling the method.
Instances of a class have attributes, which are pieces of data associated with them. """


# example:

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


kittu = Student('Kittu', 85)
kitty = Student('kitty', 91)

print(kitty.name)
print(kitty.grade)
print(kittu.name)
print(kittu.grade)


"""
Methods in Python
Classes can have other methods defined to add functionality to them. 
All methods should have 'self' as their first parameter.
"""


# example :

class Student:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print("Hello.. I'm " + self.name)

kitty = Student("Python")
kitty.sayHello()

"""
Class variable vs Instance variable
We can access a variable defined in  a class by using the class name (class variable) or 
by using the object name (instance variable).
"""


# example :

class Blog:
    url = 'www.python.ccm'

    def __init__(self, name):
        self.name = name


tutorial = Blog("Basics of Python")
print(tutorial.name)
print(Blog.url)

# In this example, 'url' is a class variable and 'name' is an instance variable.

"""
Inheritance in Python
The mechanism of deriving a new class from an old one is called inheritance. 
The old class is called super class and the new one is called sub class. 
The sub class can use all the stuff that is inside  a super class.

syntax:  Class Sub_class (Super_class):
                  ......class definition....
"""


# example:

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def meow(self):
        print("Meow..")


liza = Cat("Liza", "Orange")
print(liza.color)
print(liza.name)
liza.meow()

# Inheritance can also be indirect. one class can inherit from another,and that class can inherit from a third class.
"""
Super()
The function super() is a useful inheritance related function that refers to the parent class. 
It can be used to find the method with a certain name in an object's super class.
Syntax :    super().method_name
"""

"""
Polymorphism in Python
Polymorphism is the property by which objects belonging to different classes are able to respond to the same message, 
but in different ways. 
Polymorphism can be carried out through inheritance, with sub classes making use of super class methods or overrides 
them, so that the same method works differently based on the object that we are working with.
"""


# example :
class Fruit:
    def __init__(self, name):
        self.name = name

    def love(self):
        pass  # pass means do nothing


class Mango(Fruit):
    def love(self):
        print("Lakshmi loves mangoes")


class Apple(Fruit):
    def love(self):
        print("Narine loves apples")


slice = Mango("Alphonso")
slice.love()
appy = Apple("Kashmiri")
appy.love()

"""
It is important to note that both 'Abstraction' and 'Encapsulation' 
(These are two main concepts in OOP) do not have much role in Python, unlike other object oriented languages (eg: Java).
Advantages of OOPs in Python
Object oriented programming has many advantages over other programming paradigms. Some of them are:

Objects created can easily be reused.
Once a program reaches a certain size, OOP based programs are actually easier to code than other types of programs.
An object oriented program is lot easier to modify and maintain existing codes.
and many more.....


OOP is a great programming paradigm. But it is not the single thing that can solve all problems. 
There are some cases where OOP is the best suited way and there are other cases where procedural way is the best. 
Every Python developer should be comfortable working with Python in an object oriented fashion because it can absolutely 
be the right tool to solve certain kinds of problems.

But how do you know when to use OOP instead of the procedural way?.
Well, this skill will  be picked up by a developer over time as long as he/she writes code. 
When a developer gains experience, he/she will feel more comfortable in picking these tools depending on circumstances.
"""
