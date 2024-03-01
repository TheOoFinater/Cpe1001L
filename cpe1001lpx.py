import sys
import string

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
        cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
        cleaned_words.append(cleaned_word)
    
