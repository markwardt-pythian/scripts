#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='This is a parameter example that prints intervals', add_help=False)
parser.add_argument('-i', '--interval', type=int, help='interval to print', required=True)
parser.add_argument('-u', '--user', required=True, help="Keep Required Together")
parser.add_argument('-e', '--enum', choices=['rock', 'paper', 'scissors'])
parser.add_argument('-p', '--password')
parser.add_argument('-T', '--store_true', action='store_true')
parser.add_argument('-F', '--store_false', action='store_false')
parser.add_argument('-D', '--store_default', action='store_const', const=42, help='Default Value : 42')
parser.add_argument('-l', '--length', default='10', type=int)

args = parser.parse_args()
parser.print_help()
