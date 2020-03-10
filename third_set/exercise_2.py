numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

even_sum = 0
for number in numbers:
    if number % 2 == 0:
        even_sum += number

print("The sum of the even numbers is:", even_sum)
