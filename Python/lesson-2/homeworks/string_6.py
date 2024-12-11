str1 = input()
str2 = input()

if str1 in str2:
    print(f"{str1} is substring of {str2}")
elif str2 in str1:
    print(f"{str2} is substring of {str1}")
else:
    print("None")