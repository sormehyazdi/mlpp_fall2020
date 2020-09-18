"""
File Name: hw1_run_sy.py
Author: Sormeh Yazdi
Date: Sep 18, 2020
Python version: 3
Purpose: Run all files together in one script. Calls hw1_sy.py and hw1_2_sy.py
"""

import hw1_sy as get_data
import hw1_2_sy as to_db


print("We will be collecting demographic data from ACS for all counties and tracts in a given state.")
print("If the user does not provide any input, the default state is Florida.")
print("What state are you interested in? Please provide FIPS State Code.")
state = input('FIPS State Code = ').strip()

if state == '':
	state = '12'
	print("Collecting data for Florida by default...")

print("Now collecting data from ACS...")
get_data.acs_data_scrape(state)
print("Complete.")
print("Now uploading data to turnout5_database public schema...")
to_db.main()
print("Complete! Check out your data!")