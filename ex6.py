#Define string x with %d format specifier
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Define string y with %s format specifier
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# What is the difference between %r and %s?
# Use the %r for debugging, since it displays the "raw" data of the variable,
# but the others are used for displaying to users.
# The %r is best for debugging, and the other formats are
# for actually displaying variables to users.
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
