# Завдання 1: Клас BankAccount
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful! New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
        else:
            print("Insufficient funds.")


# Завдання 2: Клас Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


# Завдання 3: Клас Employee
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary} грн"


# Завдання 4: Клас Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# Завдання 5: Клас Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price} грн, Quantity: {self.quantity}")


# Приклад використання всіх класів:

# Завдання 1
account = BankAccount("UA123456", 1000)
account.deposit(500)
account.withdraw(200)

# Завдання 2
car = Car("Toyota", "Corolla", 2020)
print(car.get_info())

# Завдання 3
employee = Employee("Іван", "Менеджер", 15000)
print(employee.get_salary_info())

# Завдання 4
rectangle = Rectangle(5, 10)
print(f"Area: {rectangle.calculate_area()}, Perimeter: {rectangle.calculate_perimeter()}")

# Завдання 5
product = Product("Laptop", 15000, 3)
product.display_info()
print(f"Total price: {product.calculate_total_price()} грн")
