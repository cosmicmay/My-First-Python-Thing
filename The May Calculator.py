keepGoing = "y"
while keepGoing == "y" or keepGoing == "Y":
    choice = input("Welcome to May calculator, do you want to add, subtract, multiply, or divide? ")

    if choice == "add":
        FirstNumber = int(input("Type first number. "))
        SecondNumber = int(input("Type second number. "))
        if FirstNumber == int("9") and SecondNumber == int("10"):
            print("21")
        else:
            print(FirstNumber + SecondNumber)

    elif choice == "subtract":
        FirstNumber = int(input("Type first number. "))
        SecondNumber = int(input("Type second number. "))
        print(FirstNumber - SecondNumber)

    elif choice == "multiply":
        FirstNumber = int(input("Type first number. "))
        SecondNumber = int(input("Type second number. "))
        print(FirstNumber * SecondNumber)

    elif choice == "divide":
        FirstNumber = int(input("Type first number. "))
        SecondNumber = int(input("Type second number. "))
        print(FirstNumber / SecondNumber)

    elif choice == "poop":
        print("Fuck off")

    else:
        print("This question requires a case sensitive answer, run again to restart. ")

    keepGoing = input("Type y to keep using the calculator. ")