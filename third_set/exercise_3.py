numbers = [12, -10, 32, -3, 66, 17, -42, 99, 20]

sum_negative = 0
for number in numbers:
    if number < 0:
        sum_negative += number

print("Sum of the negative numbers", sum_negative)