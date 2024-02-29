import sys

file_name = sys.argv[1]

file1 = open(file_name, 'r')
Lines = file1.readlines()

count = 0   
for line in Lines:
    count += 1
    print("Line {}: {}".format(count, line.strip()))

print(file_name)