import os
from pathlib import Path

# Extract cleaned input file into an array
currentPath = os.path.dirname(os.path.realpath(__file__))
years = Path(f'{currentPath}/input').read_text().split('\n')
years = list(map(int, filter(None, years)))

yearsIndex = {key: year for year, key in enumerate(years)}

# Look if there is an entry matching 2020 - current to keep O(n) complexity
for year in years:
    diff = 2020 - year
    if (diff in yearsIndex):
        print(f'{year} x {diff} = {year * diff}')
        exit()