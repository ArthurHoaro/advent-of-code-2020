import os
import re
from pathlib import Path

regex = re.compile('(\d+)\-(\d+) (\w): (\w+)')
parseLine = lambda line: regex.findall(line)[0]

errors = 0
total = 0
currentPath = os.path.dirname(os.path.realpath(__file__))
with Path(f'{currentPath}/input').open() as resource:
	for line in resource:
	    firstIndex, secondIndex, letter, password = parseLine(line)
	    count = password.count(letter)
	    total += 1
	    # Only one between two means XOR
	    errors += 1 if (password[int(firstIndex) - 1] == letter) == (password[int(secondIndex) - 1] == letter) else 0

print('Processed ', total)
print('Valid ', total - errors)
print('Errored ', errors)
