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
	    minNb, maxNb, letter, password = parseLine(line)
	    count = password.count(letter)
	    total += 1
	    errors += 1 if not int(minNb) <= count <= int(maxNb) else 0

print('Processed ', total)
print('Valid ', total - errors)
print('Errored ', errors)
