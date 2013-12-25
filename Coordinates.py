def CreateTable(length, height):
    '''
    Creates a coordinate plane as used in computer science
    int length for x coords
    int hieght for y coords
    '''
    for l in xrange(length):
        print
        for h in xrange(height):
            print "(" + str(l) + "," + str(h) + ")",