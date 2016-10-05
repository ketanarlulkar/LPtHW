# Script will need exact 3 arguments to eexecute
# If arguments are less than 3 we will get
# ValueError: need more than 3 values to unpack
# If arguments are more than 3 we will get
# ValueError: too many values to unpack

#Command line arguments are strings
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
