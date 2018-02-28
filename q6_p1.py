primes = range(2, 101)
for i in range(2, 8):
    primes = list(filter(lambda x: x == i or x % i, primes))

print(primes)
