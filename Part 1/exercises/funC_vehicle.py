# # Functions

# def display_msg():
#     print("Today we gonna be learnin' Functions in Python\n")

# display_msg()

# def favourite_book(title):
#     print(f"Your favourite books is {title}\n")

# get_title = input("What is your favorite book?")
# favourite_book(get_title)

# def username(first_name, last_name):
#     print(f"Your First name is {first_name.title()},& Your last name is {last_name.title()}\n")

# get_fname = input("What is your first name??\n")
# get_lname = input("What is your last name??\n")
# username(get_fname,get_lname)

# # Make a T-shirt

# def make_tshirt(size,printmsg):
#     size
#     if size == "XL" :
#         print(f"The size of your selected shirt is {size},\n The message to be printed on your t-shirt is :\nI Love Python")
#     else:
#          print(f"The size of your selected shirt is {size},\n The message to be printed on your t-shirt is :\n{printmsg}")

# get_size = input("Choose a t-shirt size between S,M,L,XL and XXL\n")
# get_pmsg = input("The message you want to be printed on the T-shirt\n")
# make_tshirt(get_size.upper(),get_pmsg)

# pair0f = {}
# def city_country(city,country):
#     if city == "quit" : print("Closed")
#     else:
#         print(f"{city},{country}")
#         pair0f = {"city" : city ,"country":country}
#         print(pair0f)
    
# print(pair0f)

# active = True

# while active:
#     get_city = input("Enter your favourite city\n")
#     if get_city == "quit" :
#         active = False
#     get_country = input("Enter the country where the city is situated in\n")
#     city_country(get_city,get_country)

# # album = {}
# # def make_album(album_title,artist, no_of_songs = None):
# #     if get_album == "quit" : 
# #         print("closed")
# #     album = {"artist_name": artist, "album":album_title , "no of songs": no_of_songs}
# #     print(album)

# # active2 = True
# # while active2:
# #     get_album = input("Name your favorite album\n")
# #     if get_album == "quit" :
# #         active2 = False
# #     get_artist = input("Name of the artist\n")
# #     get_no_of_songs = input("If you remember could you mention number of songs present in that album\n")
# #     make_album(get_album,get_artist, get_no_of_songs)

# # print(album)
# album = {}

# def make_album(album_title, artist, no_of_songs=None):
#     global album  # Declare album as global to modify the global dictionary
#     if album_title == "quit":
#         print("closed")
#     else:
#         album[album_title] = {"artist_name": artist, "album": album_title, "no of songs": no_of_songs}
#         print(album[album_title])

# active2 = True
# while active2:
#     get_album = input("Name your favorite album\n")
#     if get_album == "quit":
#         active2 = False
#     else:
#         get_artist = input("Name of the artist\n")
#         get_no_of_songs = input("If you remember, could you mention the number of songs present in that album\n")
#         make_album(get_album, get_artist, get_no_of_songs)

# print(album)

# 8.9 Messages
messages = ["Hello!","Hey, Wassup!!","What's going on Mate?","I'm fine, Thank you","When are you visting Tajikistan?","On 9th of May","Shit what you cookin?","Food :)","OKi","Gonna Hop outta Bus a feed it to Hundreds"]

def suspicious_msg_detect(get_msg):
    b = 0
    for i in get_msg :
        
        b+=1
        if b % 2 == 0:
            print(f"Person B: '{i}'\n")
        else : print(f"Person A: '{i}'\n")

suspicious_msg_detect(messages)

# sent_messages = []
# def suspicious_msg_detect(get_msg):
#     b = 0
#     for i in get_msg :
        
#         b+=1
#         if b % 2 == 0:
#             print(f"Person A: '{i}'\n")
#         else : print(f"Person B: '{i}'\n")
#         current = messages.pop(0)
#         sent_messages.append(current)

# suspicious_msg_detect(messages)
# print(sent_messages)  
def make_sammich(*get_list):
    print(get_list)
    print("Here's the list of selected ingredients\n")

make_sammich("sand","creme","bitch","witch","cake","france")

def user_profilet(first_name,last_name,**about_you) :
    about_you['first'] = first_name
    about_you['last'] = last_name
    return about_you
user = user_profilet("john","kerrington",Location = "USA",Age = 24)
print(user)

def make_car(model,company,**feature):
    feature["Model"] = model
    feature["Company"] = company
    return feature

car = make_car("Ferrari 970","Ferrari",color = "red",condition = "new",edition = "vintage")
print(car)