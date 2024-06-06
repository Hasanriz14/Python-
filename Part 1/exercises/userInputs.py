# Rental Car
prompt1 = "Welcome! to Freeman's Car Rentals\nWhat is your goodname?\n"
getname = input(prompt1)
print(f"Hello! {getname}, Which Car are you looking for,\nhere's a list to help you out\n")
prompt2 = ["Honda","Subaru","Volkswagen","BMW"]
getcarbrand = input(prompt2)

if getcarbrand == "Honda" :
    print("Sure!! Lemme find you a Honda real quick")
elif getcarbrand == "Subaru" :
    print("Sure!! Lemme find you a Subaru real quick")
elif getcarbrand == "Volkswagen" :
    print("Sure!! Lemme find you a Volkswagen real quick")
elif getcarbrand == "BMW" :
    print("Sure!! Lemme find you a BMW real quick")

# Restaurant Seating
prompt3 = "Greetings!!\n How many in the dinner group?"

getinput =int(input(prompt3))

if getinput <= 7:
    print("You can come right away sire!!")
elif getinput >=8  <=14 :
    print("You'll have to wait for the table")
elif getinput >=15 <=35 :
    print("You'd have to pre-book the tables a day prior :>")
else : print("You're actually looking for a cemetry it's the first left after the roundabout")

prompt4 = "Haalo! Input a number ranging between 1 to 10\n"
getnuminput = int(input(prompt4))
if getnuminput := True :
    print("The number is eligible")
    if getnuminput * 10 <= 100 :
        print("The number is a multiple of 10")
    else: print("GTFO")