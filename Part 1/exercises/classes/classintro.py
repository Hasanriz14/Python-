class Restaurant :
    def __init__(self,restaurant_name,cuisine,number_served = 0):
        self.restaurant = restaurant_name
        self.cuisine = cuisine
        self.served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant} caters {self.cuisine} cuisine\n")

    def open_restaurant(self):
        print(f"{self.restaurant} restaurant open from 12pm\n")
        
    def set_serves(self,serves) :
        self.set_serves = serves
        print(f"{self.restaurant} has served {serves} as per yesterday\n")
    def incremental(self,increase) :
        self.set_serves += increase
        print(f"total serves as per today {self.set_serves}\n")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<")
    
resto = Restaurant("Maharaja","Indian")
print(f"There's this new restaurant called {resto.restaurant}\n")
print(f"They cater {resto.cuisine} cuisine\n")
resto.describe_restaurant()
resto.open_restaurant()
resto.set_serves(1000)
resto.incremental(12)

resto1 = Restaurant("La Crosta", "Italian")
resto1.describe_restaurant()
resto1.open_restaurant()
resto1.set_serves(240)
resto1.incremental(75)

resto2 = Restaurant("Hengbok Restaurant","Korean")
resto2.describe_restaurant()
resto2.open_restaurant()
resto2.set_serves(103)
resto2.incremental(34)

# Inheritance
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine,number_served = 0):
        super().__init__(restaurant_name,cuisine)
        print(f"{restaurant_name} serves {cuisine}\n")
    def get_flavor(self):
        self.flavour = ["Butter-scotch","Chocolate","Vanilla","Strawberry","Mango","Pistachio","Blueberry"]

        print(f"The list of available flavours today is {self.flavour}")

ice_cream = IceCreamStand("Icecream truck","ice-cream")
ice_cream.get_flavor()

        