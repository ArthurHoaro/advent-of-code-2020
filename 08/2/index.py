import os
import operator
import re
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))

with Path(f'{currentPath}/input').open() as file:
  data = list(filter(lambda x: x.strip(), file.read().split('\n')))

operators = {
  '+': operator.add,
  '-': operator.sub,
}

def nop(accumulator, pointer, value):
  return accumulator, pointer + 1

def acc(accumulator, pointer, value):
  return operators[value[:1]](accumulator, int(value[1:])), pointer + 1

def jmp(accumulator, pointer, value):
  return accumulator, operators[value[:1]](pointer, int(value[1:]))


programs = {
  'acc': acc,
  'jmp': jmp,
  'nop': nop,
}

for index, line in enumerate(data):
  replace =  line[:3]
  if replace == 'acc':
    continue

  programCopy = data.copy()
  programCopy[index] = programCopy[index].replace(replace, 'jmp' if replace == 'nop' else 'nop')
  print('Change line:', line, '--->', programCopy[index])

  pointer = 0
  accumulator = 0
  processed = {}

  while pointer not in processed and 0 <= pointer < len(programCopy):
    processed[pointer] = True
    print(programCopy[pointer], '- [', accumulator, ']')
    operation, value = programCopy[pointer].split(' ')

    accumulator, pointer = programs[operation](accumulator, pointer, value)

  if pointer == len(programCopy):
    break

print('Accumulator:', accumulator)
