#!/usr/bin/python3
import sys
cmdline = sys.argv
print("Args: "+ str(cmdline))
print("cmdline[1]: "+ str(cmdline[1]))
print("cmdline[1:]: "+ str(cmdline[1:]))
total = 0
for number in cmdline[1:]:
    total += int(number)

print("total: "+str(total))
