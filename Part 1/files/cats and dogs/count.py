from pathlib import Path
read_billy = Path('look,billy.txt')
rs = read_billy.read_text()
rs = rs.lower().count('billy')
print(rs)