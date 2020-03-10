n = 8
threshold = 1e-3
approximation = n / 2

while True:
    better = (approximation + n / approximation) / 2
    if abs(approximation - better) < threshold:
        print(better)
        break
    approximation = better