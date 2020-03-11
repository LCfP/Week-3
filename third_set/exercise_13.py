n = 2432012

count_even_digits = 0
n = abs(n)
while True:
    smallest_digit = n % 10
    if smallest_digit % 2 == 0:
        count_even_digits += 1

    n = n // 10
    if n == 0:
        break

print(count_even_digits)
