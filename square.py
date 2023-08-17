import time
import random

def square(number):
    return number * number


random.seed(10)
numbers = random.sample(range(1,9999999999),1000000000)
numbers_sqr = list() 

start_time = time.time()
for num in numbers:
    numbers_sqr.append(square(num))

result = time.time() - start_time

print(result)

