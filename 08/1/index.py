import os
import re
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))

with Path(f'{currentPath}/input').open() as file:
  data = list(filter(lambda x: x.strip(), file.read().split('\n')))

def acc(accumulator, pointer, value):
  if value[:1] == '+':
    return accumulator + int(value[1:]), pointer + 1
  return accumulator - int(value[1:]), pointer + 1

def jmp(accumulator, pointer, value):
  if value[:1] == '+':
    return accumulator, pointer + int(value[1:])
  return accumulator, pointer - int(value[1:])

def nop(accumulator, pointer, value):
  return accumulator, pointer + 1

pointer = 0
accumulator = 0
processed = {}
programs = {
  'acc': acc,
  'jmp': jmp,
  'nop': nop,
}

while pointer not in processed:
  processed[pointer] = True
  print(data[pointer])
  operation, value = data[pointer].split(' ')

  accumulator, pointer = programs[operation](accumulator, pointer, value)


print('Accumulator:', accumulator)
