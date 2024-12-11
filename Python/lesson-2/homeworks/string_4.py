text = input()
if len(text)%2:
    print('Yes' if text[:len(text)//2] == text[len(text)//2+1:][::-1] else 'No')
else:
    print('Yes' if text[:len(text)//2] == text[len(text)//2:][::-1] else 'No')