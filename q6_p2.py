nums = range(1, 11)
even = list(filter(lambda x: x % 2 == 0, nums))
square = list(map(lambda x : x**2, even))
print(square)