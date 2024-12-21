def calculator(num1,num2,operator):
    if operator == '+':
        result = num1 + num2
        return result
    elif operator == '-':
        result = num1 - num2
        return result
    elif operator == '*':
        result = num1 * num2
        return result
    elif operator == '/':
        result = num1 / num2
        return result
    else :
        print("incorrect operator")

num1 = int(input("Enter any number :"))
num2 = int(input("Enter any number :"))
operator = input("Select the operator '+','-','*','/':")

print(calculator(num1,num2,operator))