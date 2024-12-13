txt = input()
vowels = 'AIOUEaeuio'
unli, undosh = 0,0
for i in txt:
    if i in vowels:
        unli += 1
    else:
        undosh += 1
print(f"Number of vowels : {unli}\nNumber of consonants : {undosh}")