#!/usr/bin/python

# I have found that argparse is not always installed by default.  This module may have to be installed seperately from Python

import argparse

parser = argparse.ArgumentParser(description='This is a parameter example that prints intervals', add_help=False)

#Required

parser.add_argument('-i', '--interval', type=int, help='Interval in seconds', required=True)
parser.add_argument('-u', '--user', required=True, help="Keep Required Together")

# Not Required
parser.add_argument('-e', '--enum', choices=['rock', 'paper', 'scissors'])
parser.add_argument('-p', '--password')
parser.add_argument('-T', '--store_true', action='store_true')
parser.add_argument('-F', '--store_false', action='store_false')
parser.add_argument('-D', '--store_default', action='store_const', const=42, help='Stores Value : 42')
parser.add_argument('-l', '--length', default='10', type=int)

# In File Out File

parser.add_argument('-I', metavar='in-file', type=argparse.FileType('rt'))
parser.add_argument('-O', metavar='out-file', type=argparse.FileType('wt'))

try:
    results = parser.parse_args()
    print 'Input file:', results.I
    print 'Output file:', results.O
except IOError, msg:
    parser.error(str(msg))

parser.print_help()

print
print "These are the results from the arguments"
print results
print

print "Setting one of the parameters to a variable and printing"
username = results.user
print username
