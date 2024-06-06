from random import randint

def generate_list():
    random_list = []
    while len(random_list) < 20:
        random_list.append(randint(1, 20))
    return random_list

# Generate a random list
original_list = generate_list()
print("Original list:", original_list)

# Remove duplicates
unique_list = list(set(original_list))
print("List without duplicates:", unique_list)