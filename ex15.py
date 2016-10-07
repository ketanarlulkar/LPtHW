# Import argv from sys module
from sys import argv

# Assign arguments to variables
script, filename = argv

# Open a file, returning an object of the file type described in section File Objects.
txt = open(filename)

print "Here's your file %r:" % filename
# Read from txt file object
print txt.read()

# Close the txt file object
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# Close the txt_again file object
txt_again.close()
