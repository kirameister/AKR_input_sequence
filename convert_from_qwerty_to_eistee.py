import sys
import re

for line in sys.stdin:
    # first convert all the original keys in subject into upper case 
    line = re.sub('e', 'E', line)
    line = re.sub('t', 'T', line)
    line = re.sub('i', 'I', line)
    line = re.sub('o', 'O', line)

    line = re.sub('d', 'D', line)
    line = re.sub('k', 'K', line)
    line = re.sub('l', 'L', line)
    line = re.sub(';', ':', line)

    # convert upper cases into new chars
    line = re.sub('E', 'd', line)
    line = re.sub('T', ';', line)
    line = re.sub('I', 'k', line)
    line = re.sub('O', 'l', line)
    line = re.sub('D', 't', line)
    line = re.sub('K', 'e', line)
    line = re.sub('L', 'i', line)
    line = re.sub(':', 'o', line)

    print(line, end='')
