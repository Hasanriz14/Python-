from pathlib import Path
set_path = Path('guest.txt')
balls = ''
say_my_name = []
for i in range(1,10):
    getUser = input("WElcome to Carribean Plaza\nPlease enter your name:\n")
    say_my_name.append(balls)
    balls += getUser + '\n'
set_path.write_text(balls)
print(say_my_name)
