# pizza toppings
# prompt = "Welcome to Brocc Pizzeria"
# prompt += "\nWhat would you like to order"
# prompt += "\nYou can list the toppings after selecting the pizza and type 'quit' to exit the menu and to place the order"
# print("//////////////")
# print("====MENU======")
# print("//////////////")
# n= 0
# pizza_menu = {"Cheese pizza":25,"Pepperoni pizza":12,"Margherita pizza":22,"Chicken Cheese pizza":15,"Veggie loaded pizza":8,"Sicillian pizza":20}
# for i,j in pizza_menu.items() :
#     n +=1
#     print(f"{n}.{i}:= {j}$\n")

# prompt2 = "Which pizza would you like, use index number i.e 1,2,3 respectively\n"
# message = int(input(prompt2)) <-- remove # to make it work
# if message == 1 :
#     print("You have selected Cheese pizza and that would be 25$")
# elif message == 2 :
#     print("You have selected Pepperoni pizza and that would be 12$")
# elif message == 3 :
#     print("You have selected Margherita pizza and that would be 22$")
# elif message == 4 :
#     print("You have selected Chicken Cheese pizza and that would be 15$")
# elif message == 5 :
#     print("You have selected Veggie loaded pizza and that would be 8$")
# elif message == 6 :
#     print("You have selected Sicillian pizza and that would be 20$")

# prompt3 = "What toppings would you like? Toppings are free\n"
# toplist = []
# active = True
# while active :
#    toppings = input(prompt3) <-- remove # to make it work
    
#     if toppings == "quit" :
#         active = False
#         print(f"{toplist} these are your toppings of choice")
#     else :
#          print(toppings)
#          toplist.append(toppings)
        
# MOVIE TICKETS
userprompt = "Welcome to MovieMania Grand Cinema\n"
userprompt+= "Please enter your name:\n"
getinput = input(userprompt)
print(f"{getinput}!! Please to meet you\n")
userprompt2 = "Enter your age\n"
get_age = int(input(userprompt2))
if get_age <= 5 :
    print("The ticket is free, enjoy the show")
elif get_age >= 6 <= 15 :
    print("The ticket would cost 2.99$, enjoy the show")
elif get_age > 15 :
    print("The ticket would cost 5$, enjoy the show") 

# Filling a Dictionary using user input

polling_active = True
responses = {}

while polling_active :
    name = input("What is your name\n")
    response = input("Enter one favourite food item\n")

    responses [name]= response 

    pas = input("Would you like the next person to take on the quiz Yes/No ? \n")
    if pas == "No" :
       polling_active = False

print("Polling activity is Complete\nHere are the results:\n>>>>>>>>>>>>>>>>>>>>>\n<<<<<<<<<<<<<<<<\n")

for name,response in responses.items() : 
    print(f"{name},You're favourite food item is {response}")

# Deli
sandwich_orders =["pastrami sandwich","Grilled cheese sandwich","egg sandwich","ham sandwich","pastrami sandwich","grilled cheese sandwich","egg sandwich","pastrami sandwich"]
sandwich_orders1 = []
for i in sandwich_orders:
    lem = i.capitalize()
    sandwich_orders1.append(lem)
print(sandwich_orders1)
sandwich_orders_fin = []
while sandwich_orders1 : 
    get_order = sandwich_orders1.pop()
    print(f"This order is now completed => {get_order}")
    sandwich_orders_fin.append(get_order)
print(">>>>>>>>>>>>>>><<<<<<<<<<<<")
print(f"The list of completed orders{sandwich_orders_fin}")

# Next Day and no pastrami left 
sandwich_orders2 =["pastrami sandwich","Grilled cheese sandwich","egg sandwich","ham sandwich","pastrami sandwich","grilled cheese sandwich","egg sandwich","pastrami sandwich"]
sandwich_orders3 = []
for i in sandwich_orders2:
    lem = i.capitalize()
    sandwich_orders3.append(lem)
print("No Pastrami Sandwich Today since it's out of stock")
print(sandwich_orders1)
sandwich_orders_fin1 = []
while "Pastrami sandwich" in sandwich_orders3:
    sandwich_orders3.remove("Pastrami sandwich")
print(sandwich_orders3)