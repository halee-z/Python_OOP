 # Class and Object

 # creating a classs
class Student:
      def __init__(self, name, age):
          self.name = name
          self.age = age


      def display(self):
         print(f"name: {self.name}, age: {self.age}")


# creating an object             
s1 = Student( "nawal", 11)
s1.display()



# Encapsulation
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"Balance: {self.__balance}")

acc = Account(1000)
acc.deposit(500)
acc.show_balance()




# Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # from Animal
d.bark()   # from Dog



# Polymorphism
class Bird:
    def sound(self):
        print("Some bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")

class Parrot(Bird):
    def sound(self):
        print("Squawk")

# Polymorphism in action
for bird in [Sparrow(), Parrot()]:
    bird.sound()

