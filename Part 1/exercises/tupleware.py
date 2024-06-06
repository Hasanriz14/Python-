#tuples
#immutable
dimensions = (21,34,54,67)
for i in dimensions:
    print(i)

buffet = ("aloo tikki","chhaas","mutter-paneer","jeera rice","raita")
print("Today's list of food includes:")
for a in buffet:
    print(f"{a}")

#intentional error
# buffet[0] = "chaap"
# print(f"buffet[0]")

# writing over a tuple
buffet = ("chicken65","mutton-biryani","chhaas","haryali-chicken","fish-fry")
print("Today's list of food includes: ")
for b in buffet:
    print(f"{b}")