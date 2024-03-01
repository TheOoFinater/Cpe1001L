import sys
import string

word_definitions = {
    "MOV": "Move to a specified location",
    "ADD": "Addition operation",
    "R0": "Register 0",
    "R1": "Register 1",
    "R2": "Register 2",
    "R3": "Register 3",
    "R4": "Register 4",
}

file_name = sys.argv[1]

file1 = open(file_name, 'r')
lines = file1.readlines()

count = 0   
for line in lines:
    count += 1
    line = line.strip()
    print("Line {}: {}".format(count, line))
    
    words = line.split()

    cleaned_words = []
    for word in words:
        # Check if the word is a whole number
        if word.isdigit():
            # If it's a whole number, define it as itself
            cleaned_words.append(word)
        else:
            cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
            cleaned_words.append(cleaned_word)

    print("Parsed words with definitions:")
    for cleaned_word in cleaned_words:
        # Check if the word has a definition
        if cleaned_word in word_definitions:
            print(cleaned_word, "-", word_definitions[cleaned_word])
        else:
            # If the word is a whole number, define it as itself
            if cleaned_word.isdigit():
                print(cleaned_word, "-", cleaned_word)
            else:
                print(cleaned_word)
