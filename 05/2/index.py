import os
import re
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))
ids = []

def loadBinaryString(input, zeroSymbol, oneSymbol):
  return int(input.replace(zeroSymbol, '0').replace(oneSymbol, '1'), 2)

with Path(f'{currentPath}/input').open() as file:
  for line in map(lambda x: x.strip(), file):
    row, col = [loadBinaryString(line[:7], 'F', 'B'), loadBinaryString(line[7:], 'L', 'R')]
    ids.append(row * 8 + col)
        
ids.sort()
for id in range(0, ids[len(ids) - 1]):
  if id not in ids and id - 1 in ids and id + 1 in ids:
    print('Missing ID:', id)
    exit()
    