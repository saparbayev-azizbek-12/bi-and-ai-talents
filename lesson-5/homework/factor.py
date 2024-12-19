def factor(num, divider):
    return bool(num % divider == 0)

num = int(input('Enter a positive integer: '))
a = {1,num}
for i in range(2,int(num**0.5)+1):
    if factor(num, i):
        a.add(i)
        a.add(num//i)
while(a):
    print(f"{a.pop()} is a factor of {num}")