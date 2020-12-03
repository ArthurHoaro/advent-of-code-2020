import os
from pathlib import Path

moveDown = 1
moveRight = 3
rightIndex = res = 0

filter = lambda index, moveDown: index % (moveDown) == 0 and index >= moveDown
fitlerLines = lambda file, moveDown: (line.strip() for index, line in enumerate(file, 0) if filter(index, moveDown))

currentPath = os.path.dirname(os.path.realpath(__file__))
with Path(f'{currentPath}/input').open() as file:
  for line in fitlerLines(file, moveDown):
    rightIndex += moveRight

    print('line:', line)
    print('right:', rightIndex, '(', line[rightIndex % len(line)], ')')

    res += 1 if line[rightIndex % len(line)] == '#' else 0

print('Final result (classic loop):', res)

# Barely readable oneliner just for fun
with Path(f'{currentPath}/input').open() as file:
	res = sum(1 if line[rightIndex * moveRight % len(line)] == '#' else 0 for rightIndex, line in enumerate(fitlerLines(file, moveDown), 1))

print('Final result (one liner):', res)
