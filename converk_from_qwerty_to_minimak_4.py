
import sys
import re

for line in sys.stdin:
    line = re.sub('d', 'D', line)
    line = re.sub('t', 'T', line)
    line = re.sub('k', 'K', line)
    line = re.sub('e', 'E', line)

    line = re.sub('D', 't', line)
    line = re.sub('T', 'k', line)
    line = re.sub('K', 'e', line)
    line = re.sub('E', 'd', line)

    print(line, end='')
