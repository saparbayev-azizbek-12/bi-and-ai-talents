txt = input()
char = input()
for i in range(len(txt)):
    print(txt[i] if txt[i] != char else "", end="")