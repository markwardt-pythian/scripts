#!/usr/bin/python

import argparse
import sys
import subprocess

# Global Variables
mysql_user = ''
mysql_pass = ''
mysql_host = 'localhost'
mysql_args = ''

# Functions

def myrun(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    for line in p.stdout:
	line = str(line).rstrip()
    	stdout.append(line)
        
    return stdout

# Parsing command line arguments

parser = argparse.ArgumentParser(description='Base MySQL Script using the OS installed MySQL client and command line execution', add_help=False)
parser.add_argument('-h', '--host')
parser.add_argument('-u', '--user')
parser.add_argument('-p', '--password')
parser.add_argument('-d', '--defaults', help='Defaults File')

try:
    results = parser.parse_args()
except IOError, msg:
    parser.error(str(msg))
    parser.print_help()

# Configuring MySQL command line parameters
if results.user is not None and results.defaults is not None:
    parser.error("Please use either User or Defaults, and not both")
    sys.exit()

if results.host is not None:
    mysql_host = results.host
    mysql_args = " -h %s" % (mysql_host)
	
if results.user is not None:
    mysql_user = results.user
    mysql_args = " -u %s" % (mysql_user)

if results.password is not None:
    if results.user is None:
	parser.error("Please set a username if you are setting a password")
	sys.exit()
    mysql_pass = results.password
    mysql_args = " -p %s" % (mysql_pass)

print "Checking MySQL Connectivity"

cmd = "mysql %s -e 'SHOW DATABASES'" % (mysql_args)
output = myrun(cmd)
line_num = 0
for line in output:
        #print line
        print "PRINT %s : %s" % (line_num, line)
        line_num = line_num + 1
