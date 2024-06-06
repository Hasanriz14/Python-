# dictionaries in python are a key-value pair
alien_0 = {}

alien_0 = {"color":"green","height": 4.5}
print(alien_0["color"])
print(alien_0["height"])
print(alien_0)

#adding a key-value pair
alien_0 ["position_x"] = 43.2
alien_0 ["position_y"]= 12.7

print(alien_0)

# deleting a pair in dictionaries
del alien_0["height"]
print(alien_0)

# modifying a pair in dictionaries
alien_0["color"] = "red"
print(alien_0["color"])

peoper ={"first-name":"Alex","last-name":"fernando","\nage":"23","city":"newyorkington"}
print(peoper)

favorita_numba = {"semolina":"33","awici":"77","bianca":"3","dennis":"91","Rodrigo":"11"}
print(favorita_numba)

glossary = {}

glossary["localhost"]="host a website locally if you store all the executables or files required by a website to operate"

glossary["def"] = "def is used as initializer for functions in python dont know why they gotta problemo with fn "

glossary["indents"] ="indents are used as a way to solidify if the statement below a loop,if statement,etc is a part of it or not, failure to indent leads to errors"

glossary["capitalize"] = "capitalize should be deleted from this godforsaken language"

glossary["random"] = "random is cool, I like that guy he just chill like that"

# for i in glossary:
#     pointy = glossary.get(i)
#     print(f"{i}: {pointy}\n")

for i,j in glossary.items():
    print(f"{i}\n")
    print(f"{j}\n")

# Nesting dictionaries in list

car0 = {"sd":"sds","awes":"sdrew"} 
car1 = {"sgr":"slm","awbfg":"bnd"} 
car2 = {"qw":"ssa","wews":"mowk"} 

cars = [car0,car1,car2]
print(cars)

#6.7 People

people = {"first_name":"Alex","last_name":"Vortex","age":"67","city":"Columbia","qualities":"Severe dementia"}
for a,b in people.items():
    print(b)

people1 = {"first_name":"Badri","last_name":"ShiningShore","age":"21","city":"Greenland","qualities":"can be unlocked after 55"}

people2 = {"first_name":"Frank","last_name":"Singh","age":"35","city":"Vatican","qualities":"3.4ft"}

community = [people,people1,people2,peoper]

for  i in community:
    print(f"{i}\n")
#6.8 pets

pet0 = {"name":"Lucy","type":"Dog","breed":"pomerian","mixed":"no","gender":"fmale","care-taker":"Xybna"}
pet1 = {"name":"Ben","type":"Cat","breed":"tabby","mixed":"no","gender":"male","care-taker":"Ben"}
pet2 = {"name":"Walter","type":"Dog","breed":"pug","mixed":"yes","gender":"male","care-taker":"Vince"}

pets = [pet0,pet1,pet2]

for  i in pets:
    print(f"{i}\n")

#6.11 cities

city0 = {"city":"Mumbai","country":"India","Population": 21_673_000,"fact":"Financial Capital of India"}
city1 = {"city":"Bangkok","country":"Thailand","Population": 11_070_000,"fact":"The world knows the Thai capital as Bangkok, but locals refer to their city as Krungthep or 'City of Angels'. The full, 169-characters long name has been listed in the Guinness Book of World Records for the longest name of a place."}
city2 = {"city":"Florida","country":"USA RAAAA","Population": 22_000_000,"fact":"Hardest state to survive in god's green earth"}
city =[city0,city1,city2]
for  i in city:
    print(f"{i}\n")
