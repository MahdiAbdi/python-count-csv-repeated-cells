import csv
import sys
from collections import Counter
result = []
with open(sys.argv[2], 'w+', encoding='utf-8') as f:
  with open(sys.argv[1], newline='', encoding='utf-8') as g:
    reader = csv.reader(g)
    for row in reader:
      result = result + row
  listResult = Counter(result).most_common()
  for item in listResult:
    f.write(''.join(map(str, item)) + '\n')

print(f'Script ran successfully. imported {sys.argv[1]} and the result has been written in {sys.argv[2]}')