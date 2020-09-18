#hw1_2_sy.py

import psycopg2 as pg2
from config_hw1 import db_params, ssh_params
from sshtunnel import SSHTunnelForwarder


# read parameters from a secrets file, don't hard-code them!
"""
def get_secrets(filename):
	with open(filename) as f:
		return f.read()
"""
"""
tunnel = SSHTunnelForwarder(
	ssh_params['ssh_host'],
	ssh_username=ssh_params['ssh_username'],
	ssh_password=ssh_params['ssh_password'],
	remote_bind_address=ssh_params['remote_bind_address'],
	local_bind_address=ssh_params['local_bind_address']
	)
tunnel.start()
"""

conn = pg2.connect(
  host=db_params['host'],
  port=db_params['port'],
  dbname=db_params['database'],
  user=db_params['user'],
  password=db_params['password']
)
cur = conn.cursor()
cur.execute("SELECT * FROM your_table LIMIT 100;")
for record in cur:
  process_record(record)

# Close communication with the database
cur.close()
conn.close()
# Stop the tunnel
tunnel.stop()