#!/usr/bin/python

import sys
import getopt

alpha = 'default_alpha_value'
beta = '1'
charlie = ''
print

# Functions

def usage():
    print
    print "Usage : "
    print "-a --alpha      Description : Provide the alpha value.  Default = default_alpha_value"
    print "-b --beta       Description : Provide the beta value.  Integer.  Default = 1"
    print "-c --charlie    Description : Provide the charlie value.  Required"
    print
    print "Example : "
    print "%s -a alpha_value -b beta_value -c charlie_value" % sys.argv[0]
    print "%s --alpha=alpha_value --beta=beta_value --charlie=charlie_value" % sys.argv[0]
    print

# Process command line arguments
try:
    myopts, args = getopt.getopt(sys.argv[1:],"a:b:c:",['alpha=','beta=','charlie='])
except getopt.GetoptError as e:
    print (str(e))
    usage()
    sys.exit(2)

for o, a in myopts:
    if o in ("-a", "--alpha"):
        alpha = a
    elif o in ("-b", "--beta"):
        try:
            beta = int(a)
        except ValueError:
            print "Beta should be an integer"
            print a
            print beta
            usage()
            sys.exit()
    elif o in ("-c", "--charlie"):
        charlie = a
    else:
        assert False, "unhandled option"

# Checking for required options
if charlie == '':
    print "option -c --charlie is required"
    usage()
    sys.exit()

# Display input and output file name passed as the args
print "Alpha = %s and Beta = %s and Charlie = %s" % (alpha,beta,charlie)
