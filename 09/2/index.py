import os
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))

with Path(f'{currentPath}/input').open() as file:
  data = list(map(int, filter(lambda x: x.strip(), file.read().split('\n'))))

def hasPairs(numberList, value):
  for a in numberList:
    if (value - a) in numberList:
      return True
  return False

def getWeakness(numberList, start, faltyValue):
  subset = []
  for number in numberList[start::]:
    subset.append(number)
    if sum(subset) == faltyValue:
      return min(subset) + max(subset)
    elif sum(subset) > faltyValue:
      return None

fifoLength = 25
xmasFifo = []
faltyValue = None
weakness = None

for number in data:
  if len(xmasFifo) == fifoLength:
    if hasPairs(xmasFifo, number) == False:
      faltyValue = number
      break
    xmasFifo.pop(0)
  xmasFifo.append(number)

for index in range(0, len(data) - 1):
  if (weakness := getWeakness(data, index, faltyValue)) is not None:
    break

print('Invalid:', faltyValue)
print('Weakness:', weakness)
