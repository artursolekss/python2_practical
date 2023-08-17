def square(number):
    return number * number


numbers = list(range(1,99999999))
numbers_sqr = list() 
for num in numbers:
    numbers_sqr.append(square(num))


print(numbers_sqr)