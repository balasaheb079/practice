# program1.py - OOP concepts demo

from abc import ABC, abstractmethod
from typing import List


# 1) Basic class & object
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
# comment
    def greet(self):
        return f"Hi, I am {self.name} and I'm {self.age}."
#second comment

# 2) Encapsulation (private attribute + property)
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # "private" by convention (name mangling)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @property
    def balance(self) -> float:
        return self.__balance


# 3) Abstraction + Inheritance + Polymorphism
class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!!"


# 4) Composition (has-a relationship)
class Engine:
    def start(self):
        return "Engine running"


class Car:
    def __init__(self, model: str):
        self.model = model
        self.engine = Engine()  # composition

    def start(self):
        return f"{self.model}: {self.engine.start()}"


# 5) Classmethod and staticmethod
class Pizza:
    def __init__(self, toppings: List[str]):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls(["tomato", "mozzarella", "basil"])

    @staticmethod
    def is_vegetarian(toppings: List[str]) -> bool:
        non_veg = {"pepperoni", "ham", "bacon", "chicken"}
        return not any(t in non_veg for t in toppings)


# 6) Magic methods / operator overloading
class Vector:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Demo runner
def main():
    # Basic object
    p = Person("Alex", 30)
    print(p.greet())

    # Encapsulation
    acct = BankAccount("Alex")
    acct.deposit(100)
    try:
        acct.withdraw(30)
    except ValueError as e:
        print("Error:", e)
    print("Balance:", acct.balance)

    # Inheritance & Polymorphism
    animals: List[Animal] = [Dog("Rex"), Cat("Luna")]
    for a in animals:
        print(f"{a.name} says {a.speak()}")

    # Composition
    car = Car("Toyota")
    print(car.start())

    # Class/static methods
    margh = Pizza.margherita()
    print("Margherita is vegetarian?", Pizza.is_vegetarian(margh.toppings))

    # Magic methods
    v1 = Vector(1, 2)
    v2 = Vector(3, 9)
    print("v1 + v2 =", v1 + v2)

# testing
if __name__ == "__main__":
    main()



# lines below are for testing purposes 
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b

# d
# a
# ssa
# s
# ss

