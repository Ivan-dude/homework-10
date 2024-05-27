numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
#is_prime = True
for i in range(len(numbers)):
    print(i)
    if i == 1:
        numbers.remove(i)
print(numbers)
numbers_ = numbers
print(numbers_)
for x in range(len(numbers_)):
        for k in range(1, x):
            if x % k != 0 and x != k:
                primes.append(x)
            else:
                not_primes.append(x)
print(primes)
print(not_primes)
