#!/usr/bin/python

import sys
import getopt
import lib
import os
import subprocess

# Global Variables
host = 'localhost'
mysql_user = ''
mysql_pass = ''
mysql_args = ''
action = 'scan'
interval = 1
duration = 60
data_file = host + '.tar.gz'
debug = False

# Functions

def usage():
    print
    print "MySQL Analyzer"
    print
    print "Usage : "
    print "-h --host=           Description : Host to analyze.  Default = localhost"
    print "-u --user=           Description : MySQL user to connect to the database server"
    print "-p --pass=           Description : MySQL password to connect to the database server"
    print "-a --action=         Description : Specify the action to be taken.  Scan, Collect, or Analyze.  Default = Scan"
    print "                         Scan : One time data collection/scan of the server."
    print "                         Collect : Collect data at an interval for a schedule duration.  Places data into a compressed hostname.tar.gz file"
    print "                         Analyze : Analyze data that has been collected with the Collect action."
    print "-i --interval=       Description : Interval used by the collect action to collection data in minute intervals.  Default = 1."
    print "-d --duration=       Description : Total duration that data is to be collected in minutes.  Default = 60."
    print "-f --file=           Description : Specifies the file you wish to place the collected data, or the file you wish to analyze.  tar.gz is required at the end of the file name.  Default = <hostname>.tar.gz"
    print "-D --debug           Description : Enable Debug logging"
    print
    print "Example : "
    print "%s -h remote_host -u user -p pass" % sys.argv[0]
    print "%s -u user -p pass -a collect -i 5 -d 600 -f datacollection.tar.gz" % sys.argv[0]
    print "%s --host=remote_host --user=username --pass=password --action=analyze --file=datacollection.tar.gz" % sys.argv[0]
    print

# Process command line arguments
try:
    myopts, args = getopt.getopt(sys.argv[1:],"h:u:p:a:i:d:f:D",['host=','user=','pass=','action=','interval=','duration=','file=','debug'])
except getopt.GetoptError as e:
    print (str(e))
    usage()
    sys.exit(2)

for o, a in myopts:
    if o in ("-h", "--host"):
        host = a
        mysql_args = "-h %s" % host
    elif o in ("-u", "--user"):
        mysql_user = a
    elif o in ("-p", "--pass"):
        mysql_pass = a
    elif o in ("-a", "--action"):
        if a.lower() in ['scan','collect','analyze']: 
            action = a.lower()
        else:
            print "Please select a valid action, Scan, Collect, or Analyze!!"
            usage()
            sys.exit(2)
    elif o in ("-i", "--interval"):
        try:
            interval = int(a)
        except ValueError:
            print "Interval option '%s' should be a number" % a
            usage()
            sys.exit(2)
    elif o in ("-d", "--duration"):
        try:
            duration = int(a)
        except ValueError:
            print "Duration option '%s' should be a number" % a
            usage()
            sys.exit(2)
    elif o in ("-f", "--file"):
        data_file = a
    elif o in ("-D", "--debug"):
        debug = True    
    else:
        assert False, "unhandled option"

# Checking for required options and functionality
if action == 'analyze':
    if os.path.exists(data_file):
        print "Found file to analyze."
        if 'tar.gz' not in data_file:
            print "The file %s does not contain tar.gz!!" % data_file
            usage()
            sys.exit()
    else:
        print "File does not exist to analyze: %s" % data_file
        usage()
        sys.exit()

# Building MySQL connection arguments
if mysql_user != '' or mysql_pass != '':
    if os.path.exists('~/.my.analyzer.cnf'):
        os.system('rm -rf ~/.my.analyzer.cnf')
        os.system('echo "[client]" > ~/.my.analyzer.cnf')
        if mysql_user != '':
            os.system('echo "user=%s" > ~/.my.analyzer.cnf' % mysql_user)
        if mysql_pass != '':
            os.system('echo "password=\'%s\'" > ~/.my.analyzer.cnf' % mysql_pass)
        os.system('chmod 600 ~/.my.analyzer.cnf')
    mysql_args = "--defaults-file=~/.my.analyzer.cnf %s" % mysql_args

# Checking connectivity

print "Checking MySQL Connectivity"

cmd = "mysql %s -e 'SHOW DATABASES'" % mysql_args
response = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = [x.strip() for x in response.stdout.readlines()]

if debug: 
    print "Databases discovered : ", output

mysql_connect = False
if 'mysql' in output:
    print "MySQL connected successfully"
else:
    print "MySQL connection failed!"
    usage()
    sys.exit()


