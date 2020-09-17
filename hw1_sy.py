#key: b607bc16543764eef9ef259ea0f6a1519f1144ad
## This key appears to be borken
# https://api.census.gov/data/2018/acs/acs5?get=NAME,group(B01001)&for=us:1
#scaaaabun



import requests
import csvkit
import ohio.ext.pandas

#use bs4 to do the requests, cleaner than curling
# all the census blocks in 1 state and 10 variables in that census block

#plan, grab data for Florida = FIPS = 12

# then do bs4 request or plain old requests, or Ohio thing for requesting data with the big url. 

county_list = ['001', '003', '005', '007', '009', '011', '013', '015', '017', '019', '021',
				'023', '027', '029', '031', '033', '035', '037', '039', '041', '043', '045', 
				'047', '049', '051', '053', '055', '057', '059', '061', '063', '065', '067',
				'069', '071', '073', '075', '077', '079', '081', '083', '085', '086', '087',
				'089', '091', '093', '095', '097', '099', '101', '103', '105', '107', '109',
				'111', '113', '115', '117', '119', '121', '123', '125', '127', '129', '131', '133']


## curl command:
## curl --get "https://api.census.gov/data/2018/acs/acs5?get=B00001_001E,B06007_002E,B06007_003E,B06007_004E,B06007_005E,B06007_006E&for=block%20group:2&in=state:12%20county:025%20tract:957602&key=b607bc16543764eef9ef259ea0f6a1519f1144ad" 
## for people who speak english and other languages

# https://api.census.gov/data/2018/acs/acs5?get=B00001_001E,B06007_002E,B06007_003E,B06007_004E,B06007_005E,B06007_006E&for=block%20group:*&in=state:12&in=county:027&in=tract:*&key=b607bc16543764eef9ef259ea0f6a1519f1144ad" 
## for people who speak english and other languages

## This one seemed to work:
#curl --get 

apikey = "b607bc16543764eef9ef259ea0f6a1519f1144ad"
language_list = "B06007_002E,B06007_003E,B06007_004E,B06007_005E,B06007_006E"
income_list = "B06010_002E,B06010_003E,B06010_004E,B06010_005E,B06010_006E,B06010_007E,B06010_008E,B06010_009E,B06010_010E,B06010_011E"
residence = "B06008_007E"
educ_list = "B06009_002E,B06009_003E,B06009_004E,B06009_005E,B06009_006E"

request_str = "https://api.census.gov/data/2016/acs/acs5?get="+language_list+","+income_list+","+educ_list+","+residence+"&for=tract:*&in=state:12&in=county:*&key="+apikey

data_req = requests.get(request_str)
data_json = data_req.json()

#r = requests.get("https://api.census.gov/data/2016/acs/acs5?get=B00001_001E,B06010_002E,B06010_003E,B06010_004E,B06010_005E&for=tract:*&in=state:01&in=county:*&key=b607bc16543764eef9ef259ea0f6a1519f1144ad", auth=('user', 'pass'))
#r1 = requests.get("https://api.census.gov/data/2016/acs/acs5?get="+language_list+"&for=tract:*&in=state:12&in=county:*&key="+apikey, auth=('user', 'pass'))

#r2 = requests.get("https://api.census.gov/data/2016/acs/acs5?get="+income_list+"&for=tract:*&in=state:12&in=county:*&key="+apikey, auth=('user', 'pass'))

#r3 = requests.get("https://api.census.gov/data/2016/acs/acs5?get="+educ_list+"&for=tract:*&in=state:12&in=county:*&key="+apikey, auth=('user', 'pass'))

#r4 = requests.get("https://api.census.gov/data/2016/acs/acs5?get="+residence+"&for=tract:*&in=state:12&in=county:*&key="+apikey, auth=('user', 'pass'))

fname = 'data_census_scrape.csv'
fwrite = open(fname, 'wt', encoding = 'utf-8')

## list of lists
for bob in data_json:
	line = ','.join(bob)
	line += '\n'
	fwrite.write(line)


fwrite.close()
