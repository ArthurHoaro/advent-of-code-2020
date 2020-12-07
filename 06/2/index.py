import os
import re
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))
total = 0
data = None

def processLine(line, data):
  line = set(line)
  if data is None:
    return line
  return [letter for letter in data if letter in line]

with Path(f'{currentPath}/input').open() as file:
  for line in map(lambda x: x.strip(), file):
    if not line:
      total += len(data)
      data = None
    else:
      data = processLine(line, data)

print(total)
