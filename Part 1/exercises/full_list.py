# Names

frens = ["Timmy","Eric","Jacob","Alan","Raj","Arslan"]

for x in frens:
    print(x)

#greetings 
    print(f"Guten tag!! {x}, How's your day?")


# car brands
print("============================")
mucho_gracias = ["Honda","Mercedes","BMW","Ferrari","Nissan","General Motors","Maruti Suzuki","Toyota","Hyundai","Tata","KIA"]

for y in mucho_gracias:
    print(f"i would like to buy a car from {y} ")

# Guest List

guests = ["Stephen Hawking","Hawking's wheelchair","Rothschild","My bitchlessness"]

for a in guests:
    print(f"{a}, you're invited to the grand party to celebrate 26 Nov")

print("Rothschild couldn't attend this grand party!!")
guests.pop(-2)
print(guests)
print("\n\nReplacing guest!!\n===============")
print("Newyorkton is our replacement guest :>")

guests.insert(2,"Newyorkton")
print(guests)

print("New List =>")
for b in guests:
    print(f"{b}, you're invited on 26 Nov to attend a grand party hosted by yours truly")

print("New guests incoming!! ;>")

guests.insert(0,"schrodinger")
guests.insert(3,"Mica Jackson")
guests.append("residents of Wordington")

print(guests)
print("\n\n Another List >(")
for c in guests:
    print(f"{c}, you're invited on 26 Nov to attend a grand party hosted by yours truly\n")


print("IMPORTANT UPDATE!!!")
print("The table has not arrived yet meaning only two people are invited to the grand party ")
print("The invited list will be updated shortly >(")
print(f"{guests[0]},sadly you're dropped\n")
guests.pop(0)
print(f"{guests[-2]},happy you're dropped\n")
guests.pop(-2)
print(f"{guests[-1]},sadly you're dropped\n")
guests.pop(-1)
print(f"{guests[3]},sadly you're dropped\n")
guests.pop(3)
print(guests)

print("THANKS FOR JOINING ")
guests.pop(0)
guests.pop(0)
guests.pop(0)
print(guests)
