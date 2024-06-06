pizza = ["pepperoni-pizza","pineapple-pizza","cheese_burst-pizza","margherita-pizza"]
for pom in pizza:
    print(pom)
print("Pizza is love, Pizza is life.\nI love eating pineapple pizza like a deranged animal.\nStill waiting for someone to invent watermelon pizza.\nI LOVE PIZZA RRRRAAAAAA!!")

pets = ["dogs","cats","Harse neighhhhh"]

for a in pets:
    print(a.title())
    if a == pets[0]:
        print("Dogs are excellent companion but they whimsssy and they make up for it by being loyal")
    elif a == pets[1]:
        print("Cats are very wunky in nature, might eat you as a joke ")
    else:
        print("Harse are cute and have been a great companion for us human, neighhhhh ")

print("all the above mentioned animals are great as pets specially harse since you can live with a harse in an apartment. Harse mentioned neighhh neighhh")

for b in range(1,21):
    print(b)

#for c in range(1,1000000):
#    print(c)
#kys

odd_numba =list(range(1,21,2))
for d in odd_numba:
    print(d)

threes = []
for e in range(1,11):
    three = e*3
    threes.append(three)
    print(threes)

cuboid =[]
for f in range(1,11):
    cube = f**3
    cuboid.append(cube)
    print(cuboid)

# List comprehension
cubboid = [value**3 for value in range(1,11)]
print(cubboid)

slicing_a_list = ["maango","aappil","kela","sitaphal","ananas"]
print(slicing_a_list[0:2])
print(slicing_a_list[:4])
print(slicing_a_list[1:])
print(f"The first three items in the list are {slicing_a_list[:3]}")
print(f"The middle three items in the list are {slicing_a_list[1:4]}")
print(f"The last three items in the list are {slicing_a_list[2:]}")
