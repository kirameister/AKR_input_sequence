import sys
import re

for line in sys.stdin:
    # first convert all the original keys in subject into upper case 
    line = re.sub('Ctrl e', 'Ctrl E', line)
    line = re.sub('Ctrl t', 'Ctrl T', line)
    line = re.sub('Ctrl i', 'Ctrl I', line)
    line = re.sub('Ctrl o', 'Ctrl O', line)

    line = re.sub('Ctrl d', 'Ctrl D', line)
    line = re.sub('Ctrl k', 'Ctrl K', line)
    line = re.sub('Ctrl l', 'Ctrl L', line)
    line = re.sub('Ctrl ;', 'Ctrl :', line)

    # convert upper cases into new chars
    line = re.sub('Ctrl E', 'Ctrl d', line)
    line = re.sub('Ctrl T', 'Ctrl ;', line)
    line = re.sub('Ctrl I', 'Ctrl k', line)
    line = re.sub('Ctrl O', 'Ctrl l', line)
    line = re.sub('Ctrl D', 'Ctrl t', line)
    line = re.sub('Ctrl K', 'Ctrl e', line)
    line = re.sub('Ctrl L', 'Ctrl i', line)
    line = re.sub('Ctrl :', 'Ctrl o', line)

    print(line, end='')
