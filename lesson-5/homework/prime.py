def is_prime(n):
    if n < 2:
        return False
    else:
        ans = True
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                ans = False
        return ans
    
num = int(input('Enter number: '))
print(is_prime(num))