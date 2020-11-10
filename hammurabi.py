import shutil
import random


class City:
    def __init__(self):
        self.starved_people = 0
        self.population = 100
        self.acres = 1000
        self.bushels_per_acre = 3
        self.rat_food = 0
        self.bushels_in_store = 2800
        self.land_price = random.randint(15, 26)
        self.player_bought_acres = False
        self.immigrants = 0
    
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
            bushels_fed = int(input("How many bushels do you wish to feed your people?"))
        
        self.bushels_in_store -= bushels_fed

        people_fed = int(bushels_fed / 20)
        if self.population > people_fed:
            self.starved_people = self.population - people_fed
            self.population -= self.starved_people
        else:
            self.starved_people = 0
            self.immigrants = people_fed - self.population
            self.population += self.immigrants


    def acres_to_plant(self):
        acres_planted = int(input("How many acres do you wish to plant with seed?"))
        while acres_planted > self.acres:
            print("Think again")
            acres_planted = int(input("How many acres do you wish to plant with seed?"))
        self.bushels_in_store += acres_planted * self.bushels_per_acre

    def generate_land_price(self):
        self.land_price = random.randint(15, 26)

    # generar un numero entre 0 y 10
    # si ese numero es mayor o igual a 6, no pasa nada
    # si es menor a 6, generar un numero entre 10 y 40
    # restar el porcentaje de bushels_in_store => self.bushels_in_store = numero * self.bushels_in_store / 100

    def generate_rat_food(self):
        random_number = random.randint(0, 10)
        if (random_number < 6):
            self.rat_food = int(random.randint(10, 40) * self.bushels_in_store / 100)
        else:
            self.rat_food = 0
    
    def consume_rat_food(self):
        self.bushels_in_store -= self.rat_food



def hammurabi():
    city = City()
    print_introduction()
    for year in range(1, 3):
        print("\nHamurabi: I beg to report to you,")
        print("In year", year, ",", city.starved_people, "people starved")
        if year > 1:
            if city.immigrants > 0:
                print(city.immigrants, "came to city")
            else:
                print("No immigrants came to the city")
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
        city.generate_land_price()
        city.generate_rat_food()
        city.consume_rat_food()


def print_introduction():
    lines = ["Hamurabi", "Try your hand at governing ancient Sumeria", "for ten-year term of office"]
    for line in lines:
        print(line.center(shutil.get_terminal_size().columns))

def end_game(starved_people):
    print("\nYou starved", starved_people, "people in one year!!!")
    print("Due to this extreme mismanagement you have not only been impeached and thrown out of office \nbut you have also been declared national fink!!!")
    print("So long for now.")
    

hammurabi()
