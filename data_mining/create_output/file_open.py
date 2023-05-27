from pathlib import Path

path = Path(r'D:/datamining/media/')

for filename in path.iterdir():
    with filename.open() as f:
        ... # process the file