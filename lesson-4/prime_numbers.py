n = int(input('n = '))

is_prime = True
primes = []

for i in range(2,n+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        primes.append(i)
    is_prime = True
print(primes)