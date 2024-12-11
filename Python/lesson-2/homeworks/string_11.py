try:
   int(input())
   print('Only digits')
except ValueError:
   print('Not only digits')