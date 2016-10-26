the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# This is a versatile function to create lists containing arithmetic progressions.
# It is most often used in for loops. The arguments must be plain integers.
# If the step argument is omitted, it defaults to 1.
# If the start argument is omitted, it defaults to 0.
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

elements1 = []
elements1 = range(0,6)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

print elements1
print elements

# Other functions used on list are:
# append, count, extend, index, insert, pop, remove, reverse, sort
