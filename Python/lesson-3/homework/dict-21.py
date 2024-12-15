d = {2: 4, 3:2, 1: 1}
print(dict(sorted(d.items(), key=lambda item: item[1])))