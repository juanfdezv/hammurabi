import shutil

class City:
    def __init__(self):
        self.starved_people = 0
        self.population = 100
        self.acres = 1000
        self.bushels_per_acre = 3
        self.rat_food = 200
        self.bushels_in_store = 2800
        self.land_price = 26
        self.acres_bought = 0
    
    

def hammurabi():
    city = City()
    print_introduction()
    for year in range(1, 11):
        print("\nHamurabi: I beg to report to you,")
        print("In year ", year, ", ", city.starved_people, " people starved")
        print("Population is now ", city.population)
        print("The city now owns ", city.acres, " acres")
        print("You harvested ", city.bushels_per_acre, " bushels per acre")
        print("Rats ate ", city.rat_food, " bushels")
        print("You now have ", city.bushels_in_store, " in store")
        print("\nLand is trading at ", city.land_price, " bushels per acre")


def print_introduction():
    lines = ["Hamurabi", "Try your hand at governing ancient Sumeria", "for ten-year term of office"]
    for line in lines:
        print(line.center(shutil.get_terminal_size().columns))

    

hammurabi()
