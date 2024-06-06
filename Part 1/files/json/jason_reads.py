from pathlib import Path
import json

get_path = Path('num_ls.json')
writer = get_path.read_text()
numbers = json.loads(writer)
print(numbers)

