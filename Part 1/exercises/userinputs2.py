prompt = "Hey what si up ma guys it's red from amognus"
prompt += "\nI wanna play a game !"
prompt += "\nYou can't leave the game until you type 'quit' in the shhhattt\n"

message =""

while message != "quit" :
    message = input(prompt)
    message.lower()
    print(message)
    print("[=][=][=][=][=][=][=][=][=][=]")


prompt2 = "El mario und Luigi ist Kong Maansion,Save El Princessto"
active = True
while active :
    message = input(prompt2)
    if message == "quit" :
        active = False
    else : print(message)
store = []
current_number = 4
while current_number  < 80 :
    current_number += 1
    if current_number % 2 == 0 :
        continue
    elif current_number % 3 == 0 :
        continue
    elif current_number % 5 == 0:
        continue
    store.append(current_number)

print(f"1\n2\n3\n5\n {store}")
