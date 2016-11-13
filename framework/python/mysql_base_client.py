#!/usr/bin/python

import sys
import getopt
import subprocess

mysql_host = ''
mysql_user = ''
mysql_pass = ''
mysql_defaults = ''
mysql_args = '-B -N'

print

# Functions

def usage():
    print
    print "Usage : "
    print "-h --host        Description : MySQL host to connect to."
    print "-u --user        Description : MySQL account username."
    print "-p --password    Description : MySQL account password."
    print "-d --defaults    Description : Defaults file that contains MySQL crednetials.  Use either username and password or defaults.  Do not use both."
    print "-H --help        Description : Show script usage."
    print
    print "Example : "
    print "%s " % sys.argv[0]
    print "%s -h server -u root -p password" % sys.argv[0]
    print "%s -h server -d defaults/file/path" % sys.argv[0]
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
    myopts, args = getopt.getopt(sys.argv[1:],"h:u:p:d:H:",['host=','user=','password=','defaults=','help'])
except getopt.GetoptError as e:
    print (str(e))
    usage()
    sys.exit(2)

for o, a in myopts:
    if o in ("-h", "--host"):
        mysql_host = a
        mysql_args = "%s -h %s" % (mysql_args, mysql_host)
    elif o in ("-u", "--user"):
        if mysql_defaults == '':
            mysql_user = a
            mysql_args = "%s -u %s" % (mysql_args, mysql_user)
        else:
            print "Please use user and pass OR defaults.  Please do not use both"
            usage()
            sys.exit()
    elif o in ("-p", "--password"):
        mysql_pass = a
        mysql_args = "%s -p %s" % (mysql_args, mysql_pass)
    elif o in ("-d", "--defaults"):
        if mysql_user == '' and mysql_pass == '':
            mysql_defaults = a
            mysql_args = "--defaults-file=%s %s" % (mysql_defaults, mysql_args)
        else:
            print "Please use user and pass OR defaults.  Please do not use both"
            usage()
            sys.exit()
    elif o in ("-H", "--help"):
        print "Displaying usage"
        usage()
        sys.exit()
    else:
        assert False, "unhandled option"

# Building MySQL connection arguments
print "Using MySQL Client Parameters %s" % mysql_args

print "Checking MySQL Connectivity"

cmd = "mysql %s -e 'SHOW DATABASES'" % mysql_args
output = myrun(cmd)
mysql_connect = False
for line in output:
    if line == 'mysql':
        mysql_connect = True

if mysql_connect:
    print "MySQL connected successfully"
else:
    print "MySQL connection failed!"
    sys.exit()

# Continue the rest of the script
