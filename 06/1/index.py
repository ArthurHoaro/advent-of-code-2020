import os
import re
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))
total = 0
data = ''

with Path(f'{currentPath}/input').open() as file:
  for line in map(lambda x: x.strip(), file):
    if not line:
      total += len(set(data))
      data = ''
    else:
      data += line.replace(' ', '')

print(total)
