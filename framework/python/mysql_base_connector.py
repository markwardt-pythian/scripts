#!/usr/bin/python

import sys
import getopt
import subprocess
import MySQLdb

# Requires the Pyton MySQL module installed for MySQLdb import

mysql_host = 'localhost'
mysql_user = ''
mysql_pass = ''

print

# Functions

def usage():
    print
    print "Usage : "
    print "-h --host        Description : MySQL host to connect to."
    print "-u --user        Description : MySQL account username."
    print "-p --password    Description : MySQL account password."
    print "-H --help        Description : Show script usage."
    print
    print "Example : "
    print "%s " % sys.argv[0]
    print "%s -h server -u root -p password" % sys.argv[0]
    print

def myrun(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    for line in p.stdout:
        line = str(line).rstrip()
        stdout.append(line)

    return stdout

# Process command line arguments
try:
    myopts, args = getopt.getopt(sys.argv[1:],"h:u:p:H:",['host=','user=','password=','help'])
except getopt.GetoptError as e:
    print (str(e))
    usage()
    sys.exit(2)

for o, a in myopts:
    if o in ("-h", "--host"):
        mysql_host = a
    elif o in ("-u", "--user"):
        mysql_user = a
    elif o in ("-p", "--password"):
        mysql_pass = a
    elif o in ("-H", "--help"):
        print "Displaying usage"
        usage()
        sys.exit()
    else:
        assert False, "unhandled option"

db = MySQLdb.connect(
    host=mysql_host,    # your host, usually localhost
    user=mysql_user,         # your username
    passwd=mysql_pass,  # your password
    db="mysql")        # name of the data base

print "Checking MySQL Connectivity"

cur = db.cursor()
cur.execute("SHOW DATABASES")

for row in cur.fetchall():
    print row[0]
    if row[0] == 'mysql':
        mysql_connect = True

db.close()

if mysql_connect:
    print "MySQL connected successfully"
else:
    print "MySQL connection failed!"
    sys.exit()

# Continue the rest of the script
