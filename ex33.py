
def while_list(max_no, step):
    i = 0
    numbers = []

    while i < max_no:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

        print "The numbers: "

    for num in numbers:
        print num

while_list(1,1)
while_list(2,2)
while_list(4,2)
while_list(8,2)
