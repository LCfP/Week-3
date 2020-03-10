numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

count_uneven = 0
for number in numbers:
    if number % 2 != 0:
        count_uneven += 1

print("There were", count_uneven, "uneven numbers in the list")
