txt = input()
vowels = 'AEUIOaeuio'
for i in range(len(txt)):
    print(txt[i] if txt[i] not in vowels else "*", end="")