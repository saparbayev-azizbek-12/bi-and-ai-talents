txt = input()
length = len(txt)
txt = list(txt)
vowels = 'AaEeUuIiOo'
used_chars = []
n = 2
while(n<=length-2):
    if txt[n] not in vowels and txt[n] not in used_chars:
        used_chars.append(txt[n])
        txt.insert(n+1,'_')
        n += 4
    else:
        n += 1
print(''.join(txt))