code = int(input("choose your operation \n 1-hello world\n 2-data entry/exit\n 3-calculator\n 4-conditional structure\n 5-grades\n 6-discount calculator\n 7-odd or even?\n"))

if code == 1:
    print("Hello World")

if code == 2:
    age = int(input("type your age: "))
    print(f"You are {age} years old")

if code == 3:
    yofada = str = "Y"
    while yofada == "y" or yofada == "Y":
        num1 = float(input("type the first number: "))
        num2 = float(input("type the second number: "))

        yomama = str = "Y"
        while yomama == "y" or yomama == "Y":
            oper = int(input("choose your operation \n 1-sum\n 2-subtraction\n 3-division\n 4-multipliciacion\n"))
            if oper == 1:
                print("the sum is:", num1 + num2)
            elif oper == 2:
                print("the subtraction is:", num1 - num2)
            elif oper == 3:
                print("the division is:", num1 / num2)
            elif oper == 4:
                print("the multiplication is:", num1 * num2)
            elif oper > 4:
                print("type a valid operation")
            yomama = str = input("do you want to do another operation? (Y/N)\n")

        yofada = str = input("do you want to change the numbers? (Y/N)\n")

    print("OK, Bye")

if code == 4:
    age = int(input("type your age: "))
    if age >= 18:
        print("You're an adult")
    else:
        print("You're a minor")

if code == 5:
    grade1 = float(input("type the first grade: "))
    grade2 = float(input("type the second grade: "))
    avrg = float = (grade1+grade2)/2
    print(f"the average of the grades is {avrg}")

if code == 6:
    prodprice = float(input("type the product price: "))
    discvalue = int(input("type the product discount: "))
    disc1 = float = (prodprice/100)*discvalue
    discountTotal = prodprice - disc1
    print(f"The final price of the product is {discountTotal}")

if code == 7:
    number = int(input("Type the number to be verified: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

if code >= 8:
    print("Type a valid code number")