from pathlib import Path

get_path = Path('pi_digits.txt')
contents = get_path.read_text()
pi_string = ''
for l in contents.splitlines():
    pi_string += l
print(pi_string)
print(len(pi_string))

message = "I hate books"
message = message.replace('hate', 'love')
print(message)

# Pinocchio li'N'es

    # Lying about his origin: "I was not made, but was born."

liNes = "I was not made, but was born.\n"

get_pin = Path('pinocchio.txt')
get_pin = get_pin.write_text(liNes)
print(liNes)
