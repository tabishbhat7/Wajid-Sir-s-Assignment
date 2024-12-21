sum = 0
def sum_even(limit):
    global sum
    for i in range(0,limit):
        if i % 2 == 0:
            sum += i
    return sum
limit = int(input("Enter upper limit :"))
result = sum_even(limit)
print(result)