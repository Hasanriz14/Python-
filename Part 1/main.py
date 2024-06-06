import random
# random age

x = random.randint(3, 120)
ntraits = ["deaf","blind","schizo","artistic","restarted","lobotomised","mentally abused"]
negative_traits = random.choice(ntraits)
ptraits = ["Courageous", "trustworthy","wunk enjoyer","kind","mario","0/10 yasuo","2018 s1mple","Ketchup"]
positive_traits = random.choice(ptraits)
age = x
print(f" you are {negative_traits} and your age is {age}, but you're also {positive_traits}")

# Strings

goat = "'ada lovelace'"
print(goat.title())
print(goat.upper())
print(goat.lower())

print(f"Hello!,",goat.title()) # f stands for "format"
print(f"\t Python") # \t is tab |<---  --->|
print(f"Languages:\nPython\nC++\nJava\nRust")
print(f"\"Giga NIgga\"")
print(f"\'Giga NIgga\'")
print(f"\\Giga NIgga\\")

favorita_lang = "\'   py ythhh  ooo  nnnn  nnn   \'"
facorr = favorita_lang.strip()
print(facorr)
print(favorita_lang.lstrip())
print(favorita_lang.rstrip())

# some arbitrary methods
long_url = "https://bitchass.com"
headless = long_url.removeprefix("https://")
print(headless)
neckless = long_url.removesuffix(".com")
print(neckless)

# solving syntax errors using proper formatting in print macro
message = 'One of Python\'s strength is in it\'s diverse community '
print(message)

# Lists

bike = ["Bajaj-Pulsar","KTM","Royal-enfield","Hero-motocorp","Harley-davidson"]
print(bike)
print(bike[0])
print(bike[0].title())
print(bike[0].upper())
print(bike[0].swapcase())
print(bike[-1]) 
print(bike[-2]) 
print(bike[-3]) 

bike.append("Kawasaki")
print(bike[-1])

bike.insert(0,"Ather")
bike.insert(1,"Yamaha")
print(bike[0],bike[1])
# permanent sort
bike.sort()
print(bike)
bike.sort(reverse=True)
print(bike)
# temporary sort
print(sorted(bike))
