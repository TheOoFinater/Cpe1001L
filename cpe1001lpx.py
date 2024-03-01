import sys
from nltk.tokenize import word_tokenize

file_name = sys.argv[1]

file1 = open(file_name, 'r')
lines = file1.readlines()

count = 0   
for line in lines:
    count += 1
    line = line.strip()
    print("Line {}: {}".format(count, line.strip()))
s = file1
tokens = word_tokenize(s)
print(tokens)