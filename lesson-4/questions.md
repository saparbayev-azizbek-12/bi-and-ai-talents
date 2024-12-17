```markdown
# Python Questions and Answers

## Difference Between `continue` and `break` Statements

### `break` Statement:
- Terminates the loop entirely.
- Control exits the loop immediately and proceeds to the next statement after the loop.

**Example:**
```python
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2
```

### `continue` Statement:
- Skips the current iteration of the loop.
- The loop continues with the next iteration without executing the remaining code in the current iteration.

**Example:**
```python
for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0, 1, 2, 4
```

---

## Difference Between `for` Loop and `while` Loop

### `for` Loop:
- Used when the number of iterations is known beforehand.
- Iterates over a sequence like a list, range, or string.

**Example:**
```python
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

### `while` Loop:
- Used when the number of iterations is not known beforehand and depends on a condition.
- Continues until the condition becomes false.

**Example:**
```python
x = 0
while x < 5:
    print(x)
    x += 1  # Output: 0, 1, 2, 3, 4
```

---

## Implementing a Nested `for` Loop System

Nested `for` loops are loops inside another loop. They are useful for working with matrices, tables, or combinations of data.

**Example:**
```python
# Nested for loop to print a multiplication table
rows = 3
cols = 3

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()  # Move to the next row after inner loop ends
```

**Output:**
```
1 x 1 = 1	1 x 2 = 2	1 x 3 = 3	
2 x 1 = 2	2 x 2 = 4	2 x 3 = 6	
3 x 1 = 3	3 x 2 = 6	3 x 3 = 9	
```