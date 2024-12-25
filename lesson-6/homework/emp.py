MARKS = """.,*:;?"""

def clear_marks(text: str):
    cleared_text = ""
    for i in range(len(text)):
        if text[i] not in MARKS:
            if text[i] == '\n':
                cleared_text += ' '
            else:
                cleared_text += text[i]
    return cleared_text

text = """qwrnnirgn, . ,
gtgt,.?
gtgthty
yhbvfrt
vfbf
vfbf
vfbf
vfbf
vfbf
vfbf
vfbf"""

print(clear_marks(text))