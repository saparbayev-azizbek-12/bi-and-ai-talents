import os
from collections import Counter

FILENAME = 'sample.txt'
MARKS = ".,*:;\n"

def read_or_create_file(filename):
    if not os.path.exists(filename):
        print('No file found!')
        text = input('Please enter text to create: ')
        with open(filename, 'w') as file:
            file.write(text)
        return text
    else:
        with open(filename, 'r') as file:
            return file.read()

def clear_marks(text):
    cleared_text = ""
    for char in text:
        if char in MARKS:
            cleared_text += ' '
        else:
            cleared_text += char
    return cleared_text

def count_words(text):
    words = text.split()
    return Counter(words)

def main():
    file_text = read_or_create_file(FILENAME)
    text = clear_marks(file_text.lower())
    words = count_words(text)
    total_words = sum(words.values())

    print('Total words:', total_words)
    print('Top 5 most common words:')
    for word, count in words.most_common(5):
        print(f"{word} - {count} times")

if __name__ == '__main__':
    main()