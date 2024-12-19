def enrollment_stats(a: list, index: int) -> int:
    summa = 0
    for i in a:
        summa += i[index]
    return summa
    

def mean(a: list, index: int) -> int:
    return f"{(sum([i[index] for i in a])/len(a)):.2f}"

def median(a: list, index: int) -> int:
    a = sorted(a, key=lambda x: x[index])
    return a[len(a)//2][index]


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

print('*'*50)
print('Total student:',enrollment_stats(universities, 1))
print('Total tuition: $',enrollment_stats(universities, 2))
print()
print('Student mean:',mean(universities, 1))
print('Student median:',median(universities, 1))
print()
print('Tuition mean: $',mean(universities, 2))
print('Tuition median: $',median(universities, 2))