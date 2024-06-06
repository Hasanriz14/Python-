from pathlib import Path
import json

get_path = Path('store_nuber.txt')
get_input = input('your favourite number ?\nInput down below:\n')
try:
    writer = json.dumps(int(get_input))
except:
    ValueError
    print('Not an Integer\n')


try:
    get_path.write_text(writer)
except:
    FileNotFoundError
    print("file not found\nFollowing are the causes:\n1. The file name is erronous\n 2. The file is located in a separate folder\n3. You dumb as hell")