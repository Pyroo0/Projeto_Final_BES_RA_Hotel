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