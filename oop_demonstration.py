class Dog:
    def __init__(self, name, age,breed):
        self.name = name
        self.age = age
        self.breed = breed
        print(f"Создана собака по кличке {self.name}!")

    def bark(self):
        return f"{self.name} говорит: Гав-гав!"

    def get_info(self):
        return f"Это {self.breed} по кличке {self.name}, ему {self.age} лет."

rex =Dog("Песя",10, "овчарка")

rex.get_info()

#1 Инкапсуляция, отдельным уроком разобрать __attr

class BankAccount:
    def __init__(self, owner_name, real_balance):
        self.owner_name = owner_name
        self.__balance = real_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Счет пополнен на {amount}. Текущий баланс: {self.__balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Со счета списано {amount}. Текущий баланс: {self.__balance}")
        else:
            print("Недостаточно средств или неверная сумма.")

    def get_balance(self):
        print(f"Баланс счета для {self.owner_name}: {self.__balance}")
        return self.__balance

my_account = BankAccount("Иван Иванов", 1000)

my_account.get_balance()
my_account.deposit(100)
my_account.withdraw(100)

#2 Наследование
#3 И в этом же примере полиморфизм


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Дочерний класс должен реализовать этот метод")

    def eat(self):
        print(f"{self.name} ест.")

class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит: Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу!"

    def purr(self):
        return f"{self.name} мурлычет... Мррр"

dog = Dog("Пес")
cat = Cat("Кот")

dog.eat()
cat.eat()


print(dog.speak())
print(cat.speak())

print(cat.purr())

#Абстракция - рассказать на словах и, возможно, вынести на другой урок