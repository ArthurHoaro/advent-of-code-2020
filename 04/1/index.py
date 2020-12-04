import os
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))

data = {}
requiredFields = [
  'byr',
  'iyr',
  'eyr',
  'hgt',
  'hcl',
  'ecl',
  'pid',
  # 'cid',
]
validPassports = 0
isValidPassport = lambda data: len(list(field for field in requiredFields if field not in data)) == 0

# Not perfect... it is required to have 2 blank line at the end of file
with Path(f'{currentPath}/input').open() as file:
    for line in map(lambda x: x.strip(), file):
      if not line:
        if isValidPassport(data):
          validPassports += 1
        data = {}
      else:
        extracted = {key: value for key, value in (pairs.split(':') for pairs in line.split(' '))}
        data = {**data, **extracted}
        
print('Valid passports:', validPassports)