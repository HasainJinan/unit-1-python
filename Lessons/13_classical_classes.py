"""
Task 0: Class We-do

Create a class for a video game character, that tracks its health.
    -Create a method for damage

Then create a subclass called "Player" that has more health.
    -Create a method for healing
"""

#Initial character class.
class Character:
    health = 30

    #Initialize name and damage.
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    #Universal damage method.
    def dmg(self, dmg):
        self.health = self.health - dmg

#Player subclass.
class Player(Character):
    health = 100

    def healing(self):
        if self.health + 15 > 100:
            self.health = 100
        else:
            self.health = self.health + 15
        
#Enemy 1.
enemy1 = Character("Gnawer", 10)
#Player 1.
player1 = Player("MC", 10)

#Battlefield.
enemy1.dmg(player1.damage)
print("Enemy Health: " + str(enemy1.health))
player1.dmg(enemy1.damage)
player1.dmg(enemy1.damage)
print("Health: " + str(player1.health))
player1.healing()
print("Health: " + str(player1.health))
player1.healing()
print("Health: " + str(player1.health))

#Whitespace.
print()
print()
print()

"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

#Creates a class called person.
class Person:
    #Initializing/personalizing name and age to each object.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #Introductory sentence.
    def intro(self):
        print("Hello, my name is " + self.name + ". I am " + str(self.age) + " years old.")

#Executing introduction.
me = Person("Hasain", 16)
me.intro()

#Whitespace.
print()
print()
print()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

#Initial class, Animal.
class Animal:
    #Initial speak option.
    def speak(self):
        pass

#Subclass one, Dog.
class Dog(Animal):
    #Upgraded speak option.
    def speak(self):
        print("Woof Woof.")

#Subclass two, Cat.
class Cat(Animal):
    #Upgraded speak option.
    def speak(self):
        print("Meow Meow.")

#Creating objects.
dog = Dog()
cat = Cat()

#Speaking.
dog.speak()
cat.speak()

#Whitespace.
print()
print()
print()

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

#Initial class, BankAccount.
class BankAccount:
    #Initial attributes.
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    #Deposit method.
    def deposit(self, dep):
        self.balance = self.balance + dep

    #Withdraw method.
    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw

#Bank account 1.
account_1 = BankAccount(0, "John")
account_1.deposit(40)
print("Balance after deposit: " + str(account_1.balance))
account_1.withdraw(25)
print("Balance after withdrawal: " + str(account_1.balance))

#Whitespace.
print()
print()
print()

#Bank account 2.
account_2 = BankAccount(20000, "Jane")
account_2.deposit(30000)
print("Balance after deposit: " + str(account_2.balance))
account_2.withdraw(15500)
print("Balance after withdrawal: " + str(account_2.balance))