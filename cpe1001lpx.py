import sys

def parse_line(line):
    operands = line.split('+')

file_name = sys.argv[1]

file1 = open(file_name, 'r')
Lines = file1.readlines()

count = 0   
for line in Lines:
    count += 1
    line = line.strip()
    print("Line {}: {}".format(count, line.strip()))
    result = parse_line(line)
    print("   Result: {}".format(result))
    total_sum += result

print("Total sum of valid additions im the file", total_sum)

