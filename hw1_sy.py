"""
File Name: hw1_sy.py
Author: Sormeh Yazdi
Date: Sep 16, 2020
Updated: Sep 18, 2020
Python version: 3
Purpose: Scrape data from the ACS in order to get informative data for turnout project
Required: API KEY = b607bc16543764eef9ef259ea0f6a1519f1144ad
"""

import requests
import ohio.ext.pandas

def make_request(request_str):
	data_req = requests.get(request_str)
	data_json = data_req.json()


	fname = 'data_census_scrape.csv'
	fwrite = open(fname, 'wt', encoding = 'utf-8')

	## list of lists
	for data in data_json:
		line = ','.join(data)
		line += '\n'
		fwrite.write(line)


	fwrite.close()

def acs_data_scrape(fips_state):
	apikey = "b607bc16543764eef9ef259ea0f6a1519f1144ad"
	language_list = "B06007_002E,B06007_003E,B06007_004E,B06007_005E,B06007_006E"
	income_list = "B06010_002E,B06010_003E,B06010_004E,B06010_005E,B06010_006E,B06010_007E,B06010_008E,B06010_009E,B06010_010E,B06010_011E"
	residence = "B06008_007E"
	educ_list = "B06009_002E,B06009_003E,B06009_004E,B06009_005E,B06009_006E"
	#fips_state = '12'

	request_str = "https://api.census.gov/data/2016/acs/acs5?get="+language_list+","+income_list+","+educ_list+","+residence+"&for=tract:*&in=state:"+fips_state+"&in=county:*&key="+apikey

	make_request(request_str)

## Execute the main function
if __name__== "__main__":
    acs_data_scrape('12')