def greet():
    name = input("Enter Your name :")
    greeting = input("Enter Greeting Text :")
    if not greeting :
        greeting = "Hello"
    print(f"{greeting},{name}")

greet()