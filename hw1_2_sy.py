"""
File Name: hw1_2_sy.py
Author: Sormeh Yazdi
Date: Sep 16, 2020
Updated: Sep 18, 2020
Python version: 3
Purpose: Provided csv data table from hw1_sy.py file, and config_hw1.py params file,
         connects to sql database and copies the csv table into a database table
"""
import psycopg2 as pg2
from config_hw1 import db_params

def connect_db(db_params):
  conn = pg2.connect(
    host=db_params['host'],
    port=db_params['port'],
    dbname=db_params['database'],
    user=db_params['user'],
    password=db_params['password']
  )
  return conn

def main():
  conn = connect_db(db_params)

  with conn.cursor() as curs:
      print(conn)
      print(curs)
      curs.execute("CREATE TABLE IF NOT EXISTS public.sy_FLdemography (lan_B06007_002E integer, lan_B06007_003E integer, lan_B06007_004E integer, lan_B06007_005E integer, lan_B06007_006E integer, inc_B06010_002E integer, inc_B06010_003E integer, inc_B06010_004E integer, inc_B06010_005E integer, inc_B06010_006E integer, inc_B06010_007E integer, inc_B06010_008E integer, inc_B06010_009E integer, inc_B06010_010E integer, inc_B06010_011E integer, educ_B06009_002E integer, educ_B06009_003E integer, educ_B06009_004E integer, educ_B06009_005E integer, educ_B06009_006E integer, home_B06008_007E integer, state VARCHAR(20), county VARCHAR(20), tract VARCHAR(20));")
      curs.execute("DELETE FROM sy_FLdemography")
      print(curs)
      f = open('data_census_scrape.csv')
     # curs.copy_from(f, 'sytesttable',columns=('lan1', 'lan2', 'lan3', 'lan4', 'lan5', 'inc1', 'inc2', 'inc3', 'inc4', 'inc5', 'inc6', 'inc7', 'inc8', 'inc9', 'inc10','educ1', 'educ2', 'educ3', 'educ4', 'educ5', 'home1', 'state', 'county', 'tract'), sep=",")
      copy_stat = "COPY sy_FLdemography FROM stdin DELIMITER \',\' CSV header;"
      curs.copy_expert(copy_stat, f)
      print(curs)

  conn.commit()
  conn.close()


## Execute the main function
if __name__== "__main__":
    main()

