# numbers = [1, 3, 5, 7, 9]
# numbers = [1, 3, 5, 7, 9, 2]
numbers = [1, 2, 3, 5, 7, 9]

sum_up_to_even = 0
for number in numbers:
    if number % 2 == 0:
        break
    else:
        sum_up_to_even += number

print("Sum of the elements up to but not including the first even number is:", sum_up_to_even)
