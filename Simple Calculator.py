first = input("Enter first number: ")
second = input("Enter second number: ")
answer = input("What do you want to do? add, subtract, multiply, or divide? ")


if answer == "add":
    print (int(first) + int(second))
elif answer == "subtract":
    print (int(first) - int(second))
elif answer == "multiply":
    print (int(first) * int(second))
elif answer == "divide":
    print (int(first) / int(second))
else:
    print ("I'm not sure what you mean")

