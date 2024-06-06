from pathlib import Path
get_path = Path('cats.txt')
get_new_path = Path('dogs.txt')
cat_names = ["willow","spots","breezy"]
dog_names = ["pumpkin","patches","quicksilver"]
nxt_line =""
for i in cat_names:
    nxt_line += i + "\n"
    forge = get_path.write_text(nxt_line)
new_line = ""
for i in dog_names:
    new_line += i + "\n"
    forge = get_new_path.write_text(new_line)
