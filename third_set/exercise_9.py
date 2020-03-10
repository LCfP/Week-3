n = 73

for divisor in range(2, n):
    if n % divisor == 0:    # divisor is a divisor for n
        print("False")
        break
else:   # note that the else "belongs" to the for, not the if!
    print("True")
