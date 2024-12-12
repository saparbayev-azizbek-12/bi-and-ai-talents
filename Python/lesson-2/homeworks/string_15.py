txt = input()
my_list = txt.split()
ans = ''.join([a[0] for a in my_list])
print(ans)