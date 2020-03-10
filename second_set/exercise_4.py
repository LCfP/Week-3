numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# (a)
for number in numbers:
    print(number)

# (b)
for number in numbers:
    print(number, number * number)

# (c)
total = 0
for number in numbers:
    total += number

print(total)

# (d)
product = 1             # note that the base number of multiplication is 1
for number in numbers:
    product *= number

print(product)
