list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

newList = []
for i in list1:
    if i not in list2:
        newList.append(i)
for i in list2:
    if i not in list1:
        newList.append(i)
print(newList)