def countl():
    count = str(input("Type the word or phrase to be counted: "))
    leng = len(count.replace(" ", ""))
    print(f"{count} has {leng} characters")

def upperc():
    uppercase = str(input("Type the word or phrase to be uppercased: "))
    upperfinal = uppercase.upper()
    print(f"{uppercase} uppercased is {upperfinal}")