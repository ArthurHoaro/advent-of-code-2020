import os
import re
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))
maxId = 0

def loadBinaryString(input, zeroSymbol, oneSymbol):
  return int(input.replace(zeroSymbol, '0').replace(oneSymbol, '1'), 2)

with Path(f'{currentPath}/input').open() as file:
  for line in map(lambda x: x.strip(), file):
    row, col = [loadBinaryString(line[:7], 'F', 'B'), loadBinaryString(line[7:], 'L', 'R')]
    id = row * 8 + col
    maxId = id if id > maxId else maxId
        
print('Max seat ID:', maxId)