# Learning Tool from Verna Orsatti:  Exercise on how to use import csv, collections, defaultdict
#   Also using: for, not in, list, sorted, append, items, print, join

# Exercise Goal is to print each State with cities listed after - one State followed by list of cities.
#   Sort by State
#   ADD user friendly dialog
#   Run code in Terminal!  It works!

#Here's what is supplied:
# Unsorted list of a selection of States/city combinations as Tuples
state_city_list = [('TX','Georgetown'), ('CO','Denver'),('CO','Denver'), ('TX','Houston'), ('NY','Albany'), ('AK','Valdez'),('AK','Homer'),('AK','Fairbanks'),('NY', 'Syracuse'), ('NY', 'Buffalo'), 
    ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta'),('MN','St. PAUL'),('CO','Greeley'),('CO','Pueblo')]

# Take a look at the original list in Terminal:
print() # Blank line
print("state_city_list = ")
print(state_city_list)
print()

# Get some csv tools for creating a default dictionary:
import csv
from collections import defaultdict

# First let's sort the list and display it under the original list
sorted_city_list = sorted(state_city_list)
print("sorted_city_list =")
print(sorted_city_list)
print()

# Let's tool this list into a dictionary:
    # Keys will be the State codes
    # Values will be lists of cities per State code

# Create a defaultdict (dictionary)
#   Calling 'list' in the defaultdict will define the dictionary as a key with a list association
cities_by_state = defaultdict(list)

#Build dictionary with keys/values from pre-defined list of tuples
for state, city in sorted_city_list:
    if city not in cities_by_state[state]: # check values for state - only add non-existant cities per State
        cities_by_state[state].append(city)

# Take a look at the dictionary with keys and values in terminal:
print() # Blank line
print("The new list, cities_by_state is this as a result of defaultdict(list):")
print(cities_by_state) 
    #  Will print like this: (Notice that Denver only shows once)
    #    defaultdict(<class 'list'>, {'AK': ['Fairbanks', 'Homer', 'Valdez'], 'CA': ['Palo Alto', 'Sacramento'], 'CO': ['Denver', 'Greeley', 'Pueblo'], 'GA': ['Atlanta'], 'MN': ['St. PAUL'], 'NY': ['Albany', 'Buffalo', 'Rochester', 'Syracuse'], 'TX': ['Dallas', 'Georgetown', 'Houston']})
print() # Blank line

# Print formatted data from our dictionary
print("Here are the formatted results:")
for state, cities in cities_by_state.items():
    # IMPORTANT: Using 'items' keeps elements in the state whole, 
    # otherwise WITHOUT IT, the state wll be broken up into 2 characters 
    # in the following print statement, and you won't pick up the cities !!!
    
    print(state,"cities are:",'/'.join(sorted(cities)))
        # '/'.join(cities) will remove the the formatting
        # and use a 'slash' or whatever you use to separate the cities.
        # A sort was added to the cities in cities_by_state per state

# Output will look like this - just what we wanted!

# Here are the formatted results:
# AK cities are: Fairbanks/Homer/Valdez
# CA cities are: Palo Alto/Sacramento
# CO cities are: Denver/Greeley/Pueblo
# GA cities are: Atlanta
# MN cities are: St. PAUL
# NY cities are: Albany/Buffalo/Rochester/Syracuse
# TX cities are: Dallas/Georgetown/Houston

print() # Blank line
print("YAY - I hope this helped you!")    

# Co-Create with a helpful mindset - Verna Orsatti
