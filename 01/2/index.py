import os
from pathlib import Path

# Extract cleaned input file into an array
currentPath = os.path.dirname(os.path.realpath(__file__))
years = Path(f'{currentPath}/input').read_text().split('\n')
years = list(map(int, filter(None, years)))
expectedYear = 2020

yearsIndex = {key: year for year, key in enumerate(years)}

def findPairMatching(years, yearsIndex, expected):
    for year in years:
        diff = expected - year
        if (diff in yearsIndex):
            print(f'{year} x {diff} = {year * diff}')
            return year * diff
    return None

# For day one we keep the same logic as with 2 results, and increase to O(n^2)
# but it will quickly won't work very well if we increase the number of matching entries
for year in years:
    res = findPairMatching(years, yearsIndex, expectedYear - year)
    if (res is not None):
        print(f'{year} * {res} = {year * res}')
        exit()