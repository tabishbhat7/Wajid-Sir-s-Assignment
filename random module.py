import random
def generate_random_number(n):
    numbers = random.randint(0,n)
    if n < 0 :
        print("Value Error")
    return numbers

n = int(input("Enter the upper limit of integers :"))
random_numbers = generate_random_number(n)
print(random_numbers)