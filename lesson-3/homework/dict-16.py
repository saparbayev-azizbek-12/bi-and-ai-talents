d = {2: 4, 'fruit':'apple', 'tree': 'apple', 'fruits': {'grapes': 'grape'}}
print(any(isinstance(value, dict) for value in d.values()))