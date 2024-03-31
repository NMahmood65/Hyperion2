'''
*** USING ENUMERATE AND EXCEPTION HANDLING ***
This program calculates the total cost of holiday based on select destinations.
Need to select a destination from the given list then number of night stay at a hotel 
(name not provided) and number of days car hire (type of car not provided). The program then 
calculates the total cost and prints it out.
'''

import locale
locale.setlocale(locale.LC_ALL, '')

# Get user values for destination, number of nights stay and number of days car hire:
print("The cities we fly to are: Kuala_Lumpur, Singapore, Hong_Kong, Shanghai and Tokyo.")
city_list = ['Kuala_Lumpur', 'Singapore', 'Hong_Kong', 'Shanghai', 'Tokyo']
city_flight = input("Please give the city you want return flight ticket to from the list above: ")

# Check if city given is a valid destination:
if city_flight not in city_list:
    #print()
    print("We do not fly to the city requested.")
    print("Please type in a city from the following list:")
    print("Kuala_Lumpur, Singapore, Hong_Kong, Shanghai, Tokyo")
    print("Please start again.")
    exit()
try:
    num_nights = int(input("Please give the number of nights you wish to stay in the city: "))
except ValueError:
    print("Please type in a whole number for the number of nights stay. No characters are allowed.")
    print("Please start again.")
    exit()
try:
    rental_days = int(input("Please give the number of days you wish to hire a car: "))
    #print()
except ValueError:
    print("Please type in a whole number for the number of days car hire. No characters are allowed.")
    print("Please start again.")
    exit()

# The list has values in the order given.
# Name of city, cost per night for hotel, cost per day for car rental, cost of return flight:
travel_data = [
    ['Kuala_Lumpur', 60, 70, 600], 
    ['Singapore', 95, 100, 800],
    ['Hong_Kong', 100, 120, 650],
    ['Shanghai', 110, 110, 600],
    ['Tokyo', 120, 110, 900]
    ]

# Calculate the cost of hotel stay and return value:
def hotel_cost(nights: int):
    for index, value in enumerate(travel_data):
        if value[0] == city_flight:
            cost_of_hotel = nights * value[1]
            # Convert value to local currency and print:
            cost_of_hotel_ = locale.currency(cost_of_hotel, grouping=True)
            print("The cost of hotel stay for", nights,"nights is", cost_of_hotel_)
            return cost_of_hotel

# Calculate the cost of flight to the given city and return value:
def plane_cost(city: int):
    for index, value in enumerate(travel_data):
        if value[0] == city:
            cost_of_flight = value[3]
            # Convert value to local currency and print:
            cost_of_flight_ = locale.currency(cost_of_flight, grouping=True)
            print("The cost of return flight to", city_flight,"is", cost_of_flight_)
            return cost_of_flight

# Calculate the total cost of car rental for the given days and return value:
def car_rental(days: int):
    for index, value in enumerate(travel_data):
        if value[0] == city_flight:
            cost_of_rental = days * value[2]
            # Convert value to local currency and print:
            cost_of_rental_ = locale.currency(cost_of_rental,grouping=True)
            print("The cost of car rental for", rental_days, "days is", cost_of_rental_)
            return cost_of_rental

# Add up all the costs and return value:
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost_of_holiday = cost_of_rental + cost_of_flight + cost_of_hotel
    # Convert value to local currency and print:
    total_cost_of_holiday = locale.currency(total_cost_of_holiday,grouping=True)
    return total_cost_of_holiday

# Calls to all the functions:
cost_of_flight = plane_cost(city_flight)
cost_of_hotel = hotel_cost(num_nights)
cost_of_rental = car_rental(rental_days)
cost_of_holiday = holiday_cost(cost_of_flight, cost_of_hotel, cost_of_rental)

# Print the total cost of holiday:
print("The total cost of holiday is:", cost_of_holiday)