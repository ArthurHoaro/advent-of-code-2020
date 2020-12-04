import os
import re
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))

def checkHeight(value):
  try:
    if value.endswith('cm'):
      return 150 <= int(value[:-2]) <= 193
    elif value.endswith('in'):
      return 59 <= int(value[:-2]) <= 76
  except: pass
  return False
hairRegex = re.compile(r'#[a-f0-9]{6}')
pidRegex = re.compile(r'\d{9}')

data = {}
requiredFields = {
  'byr': lambda x: 1920 <= int(x) <= 2002,
  'iyr': lambda x: 2010 <= int(x) <= 2020,
  'eyr': lambda x: 2020 <= int(x) <= 2030,
  'hgt': lambda x: checkHeight(x),
  'hcl': lambda x: bool(hairRegex.fullmatch(x)),
  'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
  'pid': lambda x: bool(pidRegex.fullmatch(x)),
  # 'cid',
}
validPassports = 0

def isValidPassport(data):
  for field, validator in requiredFields.items():
    if field not in data or not validator(data[field]):
      return False
  return True

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