def enrollment_stats(a: list) -> list:
    student, tuition = 0, 0
    for i in a:
        for j in i:
            student += j[1]
            tuition += j[2]
    return [student, tuition]

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

