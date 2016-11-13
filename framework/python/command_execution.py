#!/usr/bin/python

# This script helps show how to execute commands and process the output of the command.

import subprocess

def myrun(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    for line in p.stdout:
	line = str(line).rstrip()
    	stdout.append(line)
        
    return stdout

cmd = "cat command_execution.py"
output = myrun(cmd)
line_num = 0
for line in output:
	#print line
	print "PRINT %s : %s" % (line_num, line)
	line_num = line_num + 1
