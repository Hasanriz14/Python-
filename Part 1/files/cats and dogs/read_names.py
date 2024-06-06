from pathlib import Path

read_path = Path('cat.txt') # make it plural
try:
    read_path = read_path.read_text()
    print(read_path)
except:
    FileNotFoundError
    print("The file was not found\n")
read_path2 = Path('dog.txt') # make it plural
try:
    read_path2 = read_path2.read_text()
    print(read_path2)
except:
    FileNotFoundError
    print("The file was not found\n")

read_path = Path('cat.txt') # make it plural
try:
    read_path = read_path.read_text()
    print(read_path)
except:
    FileNotFoundError
    pass
read_path2 = Path('dog.txt') # make it plural
try:
    read_path2 = read_path2.read_text()
    print(read_path2)
except:
    FileNotFoundError
    pass
