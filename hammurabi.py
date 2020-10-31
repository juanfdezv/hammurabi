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
        self.player_bought_acres = False
    
    def acres_to_buy(self):
        acres_bought = int(input("How many acres do you wish to buy?"))
        bushels_spent = acres_bought * self.land_price
        
        while bushels_spent > self.bushels_in_store:
            print("Think again")
            acres_bought = int(input("How many acres do you wish to buy?"))
            bushels_spent = acres_bought * self.land_price
        
        if acres_bought == 0:
            self.player_bought_acres = False
        else:
            self.player_bought_acres = True
        
        self.acres += acres_bought
        self.bushels_in_store -= bushels_spent

    def acres_to_sell(self):
        acres_sold = int(input("How many acres do you wish to sell?"))
        
        while acres_sold > self.acres:
            print("Think again")
            acres_sold = int(input("How many acres do you wish to sell?"))
        
        self.acres -= acres_sold
        self.bushels_in_store += acres_sold * self.land_price

    def bushels_to_feed(self):
        bushels_fed = int(input("How many bushels do you wish to feed your people?"))

        while bushels_fed > self.bushels_in_store:
            print("Think again")
            acres_sold = int(input("How many bushels do you wish to feed your people?"))
        
        self.bushels_in_store -= bushels_fed
        self.starved_people = self.population - int(bushels_fed / 20)
        self.population -= self.starved_people

    def acres_to_plant(self):
        acres_planted = int(input("How many acres do you wish to plant with seed?"))
        while acres_planted > self.acres:
            print("Think again")
            acres_planted = int(input("How many acres do you wish to plant with seed?"))
        self.bushels_in_store += acres_planted * self.bushels_per_acre



def hammurabi():
    city = City()
    print_introduction()
    for year in range(1, 3):
        print("\nHamurabi: I beg to report to you,")
        print("In year", year, ",", city.starved_people, "people starved")
        print("Population is now", city.population)
        print("The city now owns", city.acres, "acres")
        print("You harvested", city.bushels_per_acre, "bushels per acre")
        print("Rats ate", city.rat_food, "bushels")
        print("You now have", city.bushels_in_store, "bushels in store")
        print("\nLand is trading at", city.land_price, "bushels per acre")
        city.acres_to_buy()
        if city.player_bought_acres == False:
            city.acres_to_sell()
        city.bushels_to_feed()
        city.acres_to_plant()
        if(city.starved_people > city.population * 0.5):
            end_game(city.starved_people)
            break


def print_introduction():
    lines = ["Hamurabi", "Try your hand at governing ancient Sumeria", "for ten-year term of office"]
    for line in lines:
        print(line.center(shutil.get_terminal_size().columns))

def end_game(starved):
    print("\nYou starved", starved, "people in one year!!!")
    print("Due to this extreme mismanagement you have not only been impeached and thrown out of office \nbut you have also been declared national fink!!!")
    print("So long for now.")
    

hammurabi()
