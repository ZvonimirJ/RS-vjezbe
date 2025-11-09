def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def primes_in_range(start, end):
    result = []
    for x in range(start, end + 1):
        if isPrime(x):
            result.append(x)
    return result

print(isPrime(7))
print(isPrime(10))
print(primes_in_range(1, 10))
