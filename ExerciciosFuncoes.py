code = int(input("Choose your exercise (1-30)\n"))

if code == 1:
    def add(a, b):
        return a + b
    print(add(3, 4))

elif code == 2:
    def multiply(a, b):
        return a * b
    print(multiply(3, 4))

elif code == 3:
    def message(name):
        print(f"Hello, {name}!")
    message("Anna")

elif code == 4:
    def bigger(a, b):
        return a if a > b else b
    print(bigger(10, 7))

elif code == 5:
    def divide(a, b):
        return a // b, a % b
    print(divide(10, 3))

elif code == 6:
    def even_or_odd(n):
        return n % 2 == 0
    print(even_or_odd(7))

elif code == 7:
    print("It will print: Olá, none")

elif code == 8:
    def introduce(name, age, city):
        print(f"Name: {name}, Age: {age}, City: {city}")
    introduce("Anna", 20, "Curitiba")

elif code == 9:
    def introduce(name, age, city):
        print(f"Name: {name}, Age: {age}, City: {city}")
    introduce("Carlos", 25, "São Paulo")
    introduce(name="Maria", age=30, city="Rio")

elif code == 10:
    def introduce(name, age, city):
        print(f"Name: {name}, Age: {age}, City: {city}")
    introduce("Anna", "Curitiba", 20)
    print("The values will be inverted due to wrong input order")

elif code == 11:
    def greeting(name, period="day"):
        print(f"Good {period}, {name}!")
    greeting("John")

elif code == 12:
    def greeting(name, period="day"):
        print(f"Good {period}, {name}!")
    greeting("Maria", "afternoon")

elif code == 13:
    print("Error: parameters with default values must come after required ones.")

elif code == 14:
    def add_all(*numbers):
        return sum(numbers)
    print(add_all(1, 2, 3, 4))

elif code == 15:
    def show_data(**data):
        for key, value in data.items():
            print(f"{key}: {value}")
    show_data(name="Anna", age=20)

elif code == 16:
    print("*args collects positional values, **kwargs collects key=value pairs.")

elif code == 17:
    x = 10
    def test():
        x = 5
        print(x)
    test()
    print(x)

elif code == 18:
    counter = 0
    def increment():
        global counter
        counter += 1
        return counter
    print(increment())

elif code == 19:
    def triple(x):
        return x * 3
    f = triple
    print(f(4))

elif code == 20:
    def triple(x):
        return x * 3
    def execute(func, value):
        return func(value)
    print(execute(triple, 5))

elif code == 21:
    square = lambda x: x**2
    print(square(6))

elif code == 22:
    numbers = [1, 2, 3, 4, 5]
    print(list(map(lambda x: x*2, numbers)))

elif code == 23:
    numbers = [1, 2, 3, 4, 5]
    print(list(filter(lambda x: x % 2 == 0, numbers)))

elif code == 24:
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)
    print(factorial(5))

elif code == 25:
    def countdown(n):
        if n < 0:
            return
        print(n)
        countdown(n-1)
    countdown(5)

elif code == 26:
    print("Error: recursion has no stopping condition, causing infinite loop.")

elif code == 27:
    def average(lst):
        return sum(lst)/len(lst)
    print(average([10, 20, 30]))

elif code == 28:
    def average(lst):
        return sum(lst)/len(lst)
    help(average)

elif code == 29:
    def calculator(a, b, operation):
        if operation == "add":
            return a+b
        elif operation == "subtract":
            return a-b
        elif operation == "multiply":
            return a*b
        elif operation == "divide":
            return a/b
    print(calculator(10, 5, "multiply"))

elif code == 30:
    def process_data(*args, **kwargs):
        print("Args:", args)
        print("Kwargs:", kwargs)
    process_data(1, 2, 3, name="Anna", age=20)

else:
    print("Type a valid exercise")
