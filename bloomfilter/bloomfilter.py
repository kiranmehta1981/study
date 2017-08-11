from bitstring import BitArray
import hashlib
from sys import exit

N=101
bitmap = BitArray(N)

def setbit(position):
    bitmap.set(True, position)
	
def getbit(position):
    return bool(bitmap[position:position+1])

def printmap():
    for position, bit in enumerate(bitmap):
        if (bool(bit) == True):
    	    print '%d  %5r (%d)' % (position, bool(bit), bit)

def populatemap(filename):
    with open(filename) as f:
        for line in f:
            line = line.split()
            if line:
                for n in line:
		    print "Setting bits for number %s" % (n)
		    insert_element(n)

def insert_element(n):
    m = hashlib.md5(n)
    b1 = int(m.hexdigest(), 16) % N
    setbit(b1)
    m = hashlib.sha1(n)
    b2 = int(m.hexdigest(), 16) % N
    setbit(b2)
    m = hashlib.sha512(n)
    b3 = int(m.hexdigest(), 16) % N
    setbit(b3)
    print "Inserted elements %d with bits %d %d %d" % (int (n), b1, b2, b3)

def query_element(n):
    m = hashlib.md5(n)
    r = getbit(int(m.hexdigest(), 16) % N)
    if (r):
        m = hashlib.sha1(n)
        r = r and getbit(int(m.hexdigest(), 16) % N)
    if (r):
        m = hashlib.sha512(n)
        r = r and getbit(int(m.hexdigest(), 16) % N)
    return r

def do_printmap():
    printmap()

def do_insert_element():
    n = raw_input("Enter the element to be inserted: ")
    insert_element(n)

def do_query_element():
    n = raw_input("Enter the element to be queried: ")
    r = query_element(n)
    if (r):
        print "Element %s found" % (n)
    else:
        print "Element %s not found" % (n)

def do_populatemap():
    path = raw_input("Enter the file path containing data: ")
    populatemap(path)

def do_exit():
    print "Exiting ...."
    exit(0)

options = {1: do_printmap, 2: do_insert_element, 3: do_query_element, 4: do_populatemap, 5: do_exit}

while True:
    print "Select an option\n"
    print "1. Print bitmap"
    print "2. Insert an element"
    print "3. Query an element"
    print "4. Populate bitmap using file"
    print "5. Exit"
    option = raw_input()
    print "Option selected is (%d)\n\n" % int(option)
    options[int(option)]()
