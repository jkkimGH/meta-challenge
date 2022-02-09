# 1. Simple log inspector that counts 404 errors
import sys
import re

# with open(sys.argv[1], 'r') as logFile:
with open('errorLog', 'r') as logFile:
    counter = 0

    for line in logFile:
        if re.search('[0-9]{6} 404', line):
            counter += 1

print("400s:", counter)

# 2. Time range 5XX counter

# with open(sys.argv[1], 'r') as logFile:
with open('errorLog', 'r') as logFile:
    counter = 0

    for line in logFile:
        if re.search('06[0-9]{4} 5[0-9]{2}', line):
            counter += 1

print("500s between 060000 and 070000:", counter)
