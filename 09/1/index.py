import os
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))

with Path(f'{currentPath}/input').open() as file:
  data = list(filter(lambda x: x.strip(), file.read().split('\n')))

def hasPairs(numberList, value):
  for a in numberList:
    if (value - a) in numberList:
      return True
  return False

xmasFifo = []

for number in [int(number) for number in data]:
  if len(xmasFifo) == 25:
    if hasPairs(xmasFifo, number) == False:
      print(number)
      break
    xmasFifo.pop(0)
  xmasFifo.append(number)
