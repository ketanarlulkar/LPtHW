age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Learn pydoc
# Pydoc is a standard documentation module for the programming language Python
# On linux type pydoc raw_input.
# On Windows try python -m pydoc raw_input.

# What's the difference between file and open in Python? When should I use which one?
# When opening a file, it's preferable to use open() instead of
# invoking this constructor directly. file is more suited to type testing
# (for example, writing "isinstance(f, file)").
# Also, file() has been removed since Python 3.0.
