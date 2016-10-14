# Python code in one module gains access to the code
# in another module by the process of importing it.
# Modules in Python are simply Python files with the .py extension, which implement a set of functions.
# Modules are imported from other modules using the import command.
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line, how?
with open(from_file) as f:
    indata = f.read()
# in_file = open(from_file)
# indata = in_file.read()

with open(to_file, 'w') as f:
    f.write(indata)
# out_file = open(to_file, 'w')
# out_file.write(indata)

print "Alright, all done."

# Close is always necessary when dealing with files,
# it is not a good idea to leave open file handles all over the place.
# They will eventually be closed when the file object is garbage collected
# but you do not know when that will be and in the mean time
# you will be wasting system resources by holding to file handles you no longer need.
