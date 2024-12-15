def get_value(d, keys):
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None  # Key not found or not a dictionary
    return current

d = {2: 4, 'fruit':'apple', 'tree': 'apple', 'fruits': {'grapes': 'grape'}}
path = ['fruits', 'grapes']
value = get_value(d,path)
if value is not None:
    print(f"Value found: {value}")
else:
    print("Path does not exist.")