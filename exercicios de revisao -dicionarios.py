from winreg import KEY_SET_VALUE

code = int(input("choose your exercise (1-11)\n"))
if code == 1:
    data = {"nome": "fulano", "idade": 20, "cidade":"xique-xique/bahia"}
    name = ("%(nome)s")
    age = ("%(idade)s")
    city = ("%(cidade)s")
    dataprint = str(input("Whitch data do you wish to print? \n name\n age\n city\n"))
    dataprint=dataprint.upper()
    if dataprint == "NAME":
        print(name % data)
    elif dataprint ==  "AGE":
        print(age % data)
    elif dataprint == "CITY":
        print(city % data)
    else:
        print("type a valid data")

elif code == 2:
    product = {"smartphone": 2000, "tablet": 3000, "TV": 4000}
    print(product)
    key = input("Type the key that you wish to update: ")
    value = input("Type the new value: ")

    if key in product:
        product[key] = value
    else:
        print("Key not found")

    print(product)

elif code == 3:
    data = { }
    key = input("Type the name(key): ")
    value = input("Type age(value): ")
    data[key] = value
    print(data)

elif code == 4:
    dados = dict()

    for i in range(3):
        key = input(f"Type the key {i + 1}: ")
        value = input(f"type the value for {key}: ")
        dados[key] = value

    print(dados)

elif code == 5:
    data = {"nome": "fulano", "idade": 20, "cidade":"xique-xique/bahia"}
    print(data)
    delet = str(input("do you wish to delete the entire dictionary? Y/N \n"))
    delet = delet.upper()
    if delet == "Y" :
        data.clear()
        print("dictionary deleted successfully")
    else:
        print("OK")

elif code == 6:
    data = {"nome": "fulano", "idade": 20, "cidade":"xique-xique/bahia"}
    data2 = data.copy()
    data2["nome"] = "joazinho"
    print(data)
    print(data2)

elif code == 7:
    list = input("Type the names separated by commas: ")

    names = [name.strip() for name in list.split(",")]

    dictionary = dict.fromkeys(names, 0)

    print(dictionary)

elif code == 8:
    data = {"Pedro": 90, "Maria": 80, "Joao":60}
    name = str(input("Whitch student's grade do you wish to see?\n"))
    grade = (data.get(name))
    if grade == None:
        print("this student does not exist")
    else:
        print(grade)

elif code == 9:
    products = {"rice": 25.90, "beans": 8.50, "pasta": 6.20, "milk": 4.80 }

    print("Keys (products):", products.keys())

    print("Values (prices):", products.values())

    print("Items (product & price):", products.items())

elif code == 10:
    products = {"rice": 25.90, "beans": 8.50, "pasta": 6.20, "milk": 4.80}
    print(products)
    remov = str(input("choose a item (key) to be removed\n"))
    products.pop(remov)
    print(products)
    print("remove a random item:")
    products.popitem()
    print(products)

elif code == 11:
    running = True
    users = {"Pedro": 30, "Maria": 21, "Joao": 13}
    while running == True:
        operation = int(input("Choose a operation to perform:\n"
                              "1- display all users\n"
                              "2- search a user\n"
                              "3- insert a new user\n"
                              "4- update a user's age\n"
                              "5- remove a specific user\n"
                              "6- remove last added user\n"
                              "7- create a copy and edit a single value\n"
                              "8- create a new dictionary with a default age for every user\n"
                              "9- update the existing dictionary(with a newly created one)\n"
                              "10- clean all data form a dictionary\n"
                              "11- create a new dictionary (with information given by the user)\n"
                              "12- exit\n"))
        if operation == 1:
            dispOpt = str(input("what do you wish to display? (Keys, Values,Both)\n"))
            dispOpt = dispOpt.upper()
            if dispOpt == "KEYS":
                print("Keys (names):", users.keys())
            elif dispOpt == "VALUES":
                print("Values (ages):", users.values())
            elif dispOpt == "BOTH":
                print("Users (names and ages):", users.items())
            else:
                print("type a valid operation")
        elif operation == 2:
            name = str(input("Whitch user do you wish to see?\n"))
            us = (users.get(name))
            if us == None:
                print("this user does not exist")
            else:
                print(f"{name}:", us)
        elif operation == 3:
            key = input("Type the name(key): ")
            value = input("Type age(value): ")
            users[key] = value
            print(users)
            print("\n")

        elif operation == 4:
            key = input("Type the user that you wish to update: ")
            value = input("Type the new age: ")

            if key in users:
                users[key] = value
                print(users)
                print("\n")
            else:
                print("user not found")

        elif operation == 5:
            remov = str(input("choose a user to be removed: "))
            users.pop(remov)
            print(users)
            print("\n")

        elif operation == 6:
            users.popitem()
            print(users)
            print("\n")

        elif operation == 7:
            print(users)
            users2 = users.copy()
            name = str(input("whitch value do you wish to change in the copied dictionary?\n "))
            nemname = int(input("type in the new value: "))
            users2[name] = nemname
            print(users)
            print(users2)

        elif operation == 8:
            list = input("Type the names in the new dictionary, separated by commas: ")
            defage = int(input("type the default age: "))

            names = [name.strip() for name in list.split(",")]

            newnames = dict.fromkeys(names, defage)

            print(newnames)

        elif operation == 9:
            usersupd = dict()
            dicsize = int(input("what is the size of your update for the dictionary?\n"))
            for i in range(dicsize):
                key = input(f"Type the key {i + 1}: ")
                value = input(f"type the value for {key}: ")
                usersupd[key] = value
            print (users)
            print(usersupd)
            users.update(usersupd)
            print(users)

        elif operation == 10:
            confirmation = int(input("are you sure that you want to delete all registered users?\n 1- Yes\n 2- No\n"))
            if confirmation == 1:
                users.clear()
                print(users)
            else:
                print("operation canceled")

        elif operation == 11:
            newdict = dict()
            dicsize = int(input("what is the size of your dictionary?"))
            for i in range(dicsize):
                key = input(f"Type the key {i + 1}: ")
                value = input(f"type the value for {key}: ")
                newdict[key] = value

            print(newdict)

        elif operation == 12:
            running = False

else:
    print("Type a valid exercise")