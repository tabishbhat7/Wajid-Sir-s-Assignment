import math
def pythagorus(x,y):
    hypt = math.sqrt(base**2 + perp**2)
    return hypt


base = float(input("Enter Base of a Triangle :"))
perp = float(input("Enter perpendicular of a Triangle :"))
result = pythagorus(base,perp)
print(result)


import random
limit = int(input("Enter the upper Limit :"))
guess = int(input(f"Guess the number from '0' to {limit} :"))
number = random.randint(0,limit)
if guess == number:
    print(f"Congrats!Number Guessed is Correct ,{number} = {guess}")
else :
    print(f"Number Guessed {guess} is not equal to the number generated {number}")