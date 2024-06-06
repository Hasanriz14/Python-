from pathlib import Path
import json

get_path = Path('store_number.txt')
read_num = get_path.read_text()
print_num = json.loads(read_num)
print(print_num)
