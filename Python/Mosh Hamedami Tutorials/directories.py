from os import mkdir
from pathlib import Path

path = Path("Python")
total = 0
for file in path.glob('*.*'):
    total += 1
print(f'total: {total} files in directory {path}')
