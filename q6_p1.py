def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# If the input number, x, returns back after the formula is run, x + 1 is prime
prime = lambda x: factorial(x) % (x + 1) == x
prime_list = []
for z in range(1, 100):
    if prime(z):
        prime_list.append(z + 1)
    else:
        continue

print(prime_list)
