from pathlib import Path
import json
def get_numba():
    get_path = Path('store_number.json')
    if  get_path.exists():
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
        get_path = Path('store_number.json')
        read_num = get_path.read_text()
        print_num = json.loads(read_num)
        print(print_num)
    else:
        print('file not found\n')
get_numba()