import shutil

def hammurabi():
    
    starved_people = 0
    population = 100
    acres = 1000
    bushels_per_acre = 3
    rat_food = 200
    bushels_in_store = 2800
    land_price = 26
    
    print_introduction()
    for year in range(1, 11):
        print("Hamurabi: I beg to report to you,")
        print("In year ", year, ", ", starved_people, " people starved")
        print("Population is now ", population)
        print("The city now owns ", acres, " acres")
        print("You harvested ", bushels_per_acre, " bushels per acre")
        print("Rats ate ", rat_food, " bushels")
        print("You now have ", bushels_in_store, " in store")
        print("\nLand is trading at ", land_price, " bushels per acre")

def print_introduction():
    lines = ["Hamurabi", "Try your hand at governing ancient Sumeria", "for ten-year term of office"]
    for line in lines:
        print(line.center(shutil.get_terminal_size().columns))


    

hammurabi()
