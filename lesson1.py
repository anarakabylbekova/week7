# Миксины и множественное наследование

# class Transport:
#     def move(self):
#         return 'Этот транспорт: '

# class Boat(Transport):
#     def move(self):
#         print(f'{super().move()} плывет')

# boat = Boat()    
# boat.move()


# class Call:
#     def call(self):
#         print('call')


# class Mail:
#     def send_letter(self):
#         print('mail')


# class SmartPhone(Call, Mail):
#     pass

# obj1 = SmartPhone()
# obj1.call()
# obj1.send_letter()

# print(SmartPhone.__mro__)


# class Parent1:
    
#     def method(self):
#         print('Parent1')
#     pass

# class Parent2:
#     def method(self):
#         print('Parent2')

# class Child(Parent1, Parent2):
#     def method(self):
#         print('child')
#     pass

    
# child = Child()
# child.method()


# class Grandpa:
#     # a = 1
#     pass

# class Grandma:
#     # a = 2
#     pass

# class Dad(Grandma, Grandpa):
#     # a = 3
#     pass


# class Mom:
#     a = 4

# class Me(Dad, Mom):
#     # a = 5
#     pass

# obj1 = Me()
# print(obj1.a)


# class A:
#     a = 1

# class B:
#     # a = 2
#     pass

# class C(A):
#     a = 3

# class D(B, C):
#     # a = 4
#     pass


# obj1 = D()
# print(obj1.a)



# class A:
#     a = 1

# class B(A):
#     a = 2
    

# class C(A):
#     # a = 3
#     pass

# class D(C, B):
#     pass
    

# obj1 = D()
# print(obj1.a)
# print(D.__mro__)

# Прочитать про Проблемы Ромба (Diamond Problem)


"""МИКСИНЫ"""

# Mixin - это особый вид множественного наследования, 
# где задача миксинов является расширение функционала других классов (расширители классов)

# Работа с Mixin:
# 1) Принято давать имена, заканчивающиеся на mixin (GetterMixin)
# 2) Mixin не предназначен, чтобы от него создавали объекты
# 3) Нужен чтобы расширить функционал другого класса


# class MoveMixin:
#     def move(self):
#         print('Двигаюсь')

# class StopMixin:
#     def stopp(self):
#         print('Остановись')

# class Person(MoveMixin, StopMixin):
#     pass

# class Car(MoveMixin, StopMixin):
#     pass

# class GetYearMixin:
#     def get_year(self, age):
#         return f'Привет вы родились примерно в {2022 - self.age} году'


# class Person(GetYearMixin):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj1 = Person('John', 22)
# print(obj1.get_year(obj1.age))


"""Видеолекции"""

# class Parent:
#     def who_am_i(self):
#         print('I am a parent')

# class Child(Parent):
#     def who_am_i(self):
#         super().who_am_i()
#         print('I am a child')

# child = Child()
# child.who_am_i()


# class Grandpa:
    # def talant(self):
    #     print('I am good at dancing')
#     pass

# class Grandma:
#     def talant(self):
#         print('I am good at singing')

# class Father:
    # last_name = 'White'
    # def talant(self):
    #     print('I can build houses')

# class Mother(Grandpa, Grandma):
#     last_name = 'Brown'

# class Child(Father, Mother):
#     pass

# child = Child()
# print(child.last_name)
# child.talant()
# print(Child.__mro__)


# class A:
#     def __init__(self, param):
#         print(f"Hey, It is A class, I got {param} parameter")

#     def get_a(self):
#         print("Aaaa")
        
# class B:
#     def __init__(self, param):
#         print(f"Hey, It is B class, I got {param} parameter")

#     def get_b(self):
#         print("Bbbb")

# class C(A, B):
    # def __init__(self):
    #     print(f"Hey, It is C class, I don't get any parametres")

#     def get_c(self):
#         print("Cccc")
    

# c = C('Makers')
# c.get_a()
# c.get_b()
# c.get_c()

# Tasks



# class RadioMixin:
#     def play_music(self):
#         title = 'Love again'
#         print(f'Песня называется: {title}')

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(RadioMixin):
#     pass
# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music()
# boat.play_music()
# obj.play_music()




# class Auto:
#   def ride(self):
#     print('Riding on a ground')

# class Boat:
#   def swim(self):
#     print('floating on water')

# class Amphibian(Auto, Boat):
#   pass

# obj = Amphibian()
# obj.ride()
# obj.swim()


# class Clock:
#     def current_time(self):
#         print('17:10:41')

# class Alarm:
#     def on(self):
#         print('Включен')

#     def off(self):
#         print('Выключен')

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         print('Будильник включен')

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()


# class A:
#     def method(self):
#         print('Hello, I am A')

# class B(A):
#     def method(self):
#         super().method()
#         print('Hello, I am B')
    

# class C(A):
#     def method(self):
#         super().method()
#         print('Hello, I am C')
    

# class D(B, C):
#     def method(self):
#         print('Hey, D')
#     pass
    

# d = D()
# d.method()



# Принцип - SOLID

# class Bird:
#     def __init__(self):
#         print('I am a bird')

#     def fly(self):
#         print('I can fly')

# class Hawk(Bird):
#     pass

# class Eagle(Bird):
#     pass

# class Pinguin(Bird):
#     pass
