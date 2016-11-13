#!/usr/bin/python

import argparse
import MySQLdb

parser = argparse.ArgumentParser(description='This is a parameter example that prints intervals', add_help=False)

# Not Required
parser.add_argument('-u', '--user')
parser.add_argument('-p', '--password')
parser.add_argument('-h', '--host')

try:
    results = parser.parse_args()
    print 'Input file:', results.iI
    print 'Output file:', results.O
except IOError, msg:
    parser.error(str(msg))

config = {
  'user': 'scott',
  'password': 'tiger',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True,
}

try:
    cnx = mysql.connector.connect(**config) 
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

