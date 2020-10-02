# main.py
# This is your code's starting point
# Follow the guidelines in the homework document
# Don't forget to add data folder for your data
# Replace the following line with real application code
import sys
import pandas as pd 
import string 

from read_state_module import read_state
from read_country_module import read_country
from read_county_module import read_county

# initiate read country class and reads/process file
def country():
    files = "data/us.csv"
    print("Country data was chosen...")
    data = read_country(files)
    data.read_file()
    data.date_reformat()


    data.country_stats()
    print('\n')
    print('Number of US cases:')
    print(data.USA_stats.iloc[0]['cases'])
    print('\n')
    print('Number of US deaths:')
    print(data.USA_stats.iloc[0]['deaths'])
    print('\n')

    print('\n')

# initiate read state class and reads/process file
def state():
    files = "data/us-states.csv"
    data = read_state(files)
    data.read_file()
    data.date_reformat()
    data.per_state_stats()
    print('\nCases per state:\n')
    print(data.state_stats)

# initiate read county class and reads/process file
def counties():
    files = "data/us-counties.csv"
    data_county = read_county(files)
    data_county.read_file()
    data_county.date_reformat()
    county, state = input("Enter County and State separated by space: ").split()
    print("\nNumber of cases and deaths for county", county, "and state", state, ": \n")
    data_county.set_user_selection(county, state)
    data_county.per_state_county()
    print(data_county.county_state)
    while True:
        value = input("Would you like to view another county and state? (y/n) ")
        value = value.lower()
        value = value.replace(" ", "")
        if value not in ['y', 'n']:
            print('Invalid input please try again')
        else:
            if value == 'y' :
                counties()
            break
    
def main():
    file = ""
    error_message = 'Invalid input please try again'
    options = ["county", "state", "country"]
    while True:
        value = input("Please chose county, state, or country data set:")
        value = (value.lower())
        value = value.replace(" ", "")

        if value not in options:
            print(error_message)
        else:
            if value == "country":
                
                country()
                break
            elif value == "state":
                state()

                print("US State data was chosen...")

                break
            counties()
        

            break
    while True:
        value = input("Would you like to view another dataset? (y/n) ")
        value = value.lower()
        value = value.replace(" ", "")
        if value not in ['y', 'n']:
            print(error_message)
        else:
            if value == 'y' :
                main()
            break

                
    


    

main()