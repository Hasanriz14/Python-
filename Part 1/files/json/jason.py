

num_ls = [1,3,5,7,9,11,13,17,19,23,29]
get_path = Path('num_ls.json')
dump = json.dumps(num_ls)
get_path.write_text(dump)

