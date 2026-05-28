from unicodedata import name

import conversorModul
import textoModul
import operacoesModul
import usuarioModul
import geometriaModul
exer = int(input("Choose the exercise(1-4): "))
if exer == 1:
    oper = int(input("What do you wish to do?\n 1- convert cm to m\n 2- converto C to F\n 3- count letters\n 4- make eveything uppercase\n"))
    if oper == 1:
        conversorModul.conversorm()
    elif oper == 2:
        conversorModul.conversorc()
    elif oper == 3:
        textoModul.countl()
    elif oper == 4:
        textoModul.upperc()
    else:
        print("Type a valid exercise")
elif exer == 2:
    a = int(input("type in the first number: "))
    b = int(input("type in the second number: "))
    print(f"Sum: {operacoesModul.sum(a, b)}")
    print(f"Subtraction: {operacoesModul.sub(a, b)}")
    print(f"Multiplication: {operacoesModul.mult(a, b)}")
    print(f"Division: {operacoesModul.div(a, b)}")

elif exer == 3:
    name = input("Type in your name to check-in: ")
    usuarioModul.register(name)
    usuarioModul.salut(name)

elif exer == 4:
    l = float(input("square side: "))
    print(f"Square area: {geometriaModul.sqrarea(l)}")

    r = float(input("Circle radius: "))
    print(f"Circle area: {geometriaModul.crclarea(r):.4f}")

    b = float(input("Rectangle base: "))
    h = float(input("Rectangle height: "))
    print(f"Rectangle perimeter: {geometriaModul.rectangleperimeter(b, h)}")
