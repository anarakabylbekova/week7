# Полиморфизм

# Полиморфизм - возможность использовать один и тот же метод для объектов от разных классов, 
# при этом результат может меняться в зависимости от того к какому классу принадлежит объект.

# Полиморфизм - множество форм.

# def add(x, y):
#     return x + y

# print(add(5, 5))
# print(add(str(5), str(5)))


# print(len('python'))
# print(len([1,2,3,4]))
# print(len({'a': 5}))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         return 'MEOWWW'

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def make_sound(self):
#         return 'GAVV'

# cat = Cat('Barsik', 10)
# dog = Dog('Rex', 8)
# print(cat.make_sound())
# print(dog.make_sound())

# list_ = [cat, dog]

# for i in list_:
#     print(i.make_sound())


# from math import pi
# from turtle import circle


# class ShapeMixin:
#     """Класс для описания формы"""  
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self) -> str:
#         return self.name

# class Square(ShapeMixin):
#     def __init__(self, length):
#         super().__init__('Square')
#         self.length = length
    
#     def area(self):
#         return self.length ** 2

# class Circle(ShapeMixin):
#     def __str__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         return self.radius ** 2 * pi

    
# square1 = Square(4)
# square2 = Square(2)

# circle1 = Circle(3)
# circle2 = Circle(5)



# list_ = [square1, square2, circle1, circle2]
# [print(i.area()) for i in list_]




# Абстракция - абстрактный класс (класс, в котором есть абстрактный метод) - определяет общий интерфейс для набора подклассов. 
# Заставляя дочерние классы реализоввывать абстрактные методы.

# from abc import ABC, abstractclassmethod

# class A(ABC):
#     def method1(self):
#         pass

#     @abstractclassmethod
#     def method2(self):
#         pass

# class B(A):
#     def method2(self):
#         pass

# b = B()

# from abc import ABC, abstractclassmethod

# class People(ABC):
#     @abstractclassmethod
#     def breath():
#         pass
#     @abstractclassmethod
#     def eat():
        
#     @abstractclassmethod
#     def move():
#         pass
#     @abstractclassmethod
#     def sleep():
#         pass


# class Person(People):
#     def sleep(self):
#         print('Я умею отдыхать')

#     def breathe(self):
#         print('Я умею дышать')
    
#     def eat(self):
#         print('Я умею есть')

#     def move(self):
#         print('Я умею двигаться')

# obj1 = Person()


# from abc import ABC, abstractclassmethod

# class Animal(ABC):
#     @abstractclassmethod
#     def move():
#         pass

# class Cat(Animal):
#     def move(self):
#         print('I am a cat, I can move')


# class Dog(Animal):
#     def move(self):
#         print('I am a dog, I can run')
    

# cat = Cat()
# dog = Dog()
# cat.move()
# dog.move()


# 3 Fiz
# 5 Buzz
# 3 5 FizBuzz


# list_ = range(1, 100)
# for i in list_:
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizBuzz')
#     elif i % 3 == 0:
#         print('Fiz')
#     elif i % 5 == 0:
#         print('Buzz')
   


