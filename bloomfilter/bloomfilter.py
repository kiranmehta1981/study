from bitstring import BitArray
from math import sqrt
from itertools import count, islice
import hashlib
import sys

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

H=[hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]
T=len(H)

if len(sys.argv) != 4 or bool(isPrime(int(sys.argv[1])) == False):
    print "Required format: <python> <program> <prime size of bitmap> <number of hash functions (<=4)> <config file>"
    sys.exit(0)
if int(sys.argv[1]) <= 0:
    print "Required format: <python> <program> <prime size of bitmap> <number of hash functions (<=4)> <config file>"
    sys.exit(0)
if int(sys.argv[2]) <= 0 or int(sys.argv[2])  > T:
    print "Required format: <python> <program> <prime size of bitmap> <number of hash functions (<=4)> <config file>"
    sys.exit(0)

N=int(sys.argv[1])
K=int(sys.argv[2])
config_file = sys.argv[3]
bitmap = BitArray(N)
elem_count = 0
fp_count = 0;


def setbit(position):
    bitmap.set(True, position)
	
def getbit(position):
    return bool(bitmap[position:position+1])

def printmap():
    count = 0
    for position, bit in enumerate(bitmap):
        if (bool(bit) == True):
    	    print '%d  %5r (%d)' % (position, bool(bit), bit)
            count = count + 1
    print "Total bits set  = %d" % (count)

def populatemap(filename, s, e):
    print " Trying to populate map with file=%s start=%d end=%d" % (filename, s, e)
    with open(filename) as f:
        for i,line in enumerate(f, 1):
            if ( i < s):
                continue;
            if line:
	        print "Setting bits for %s" % (line)
	        insert_element(line)
            s = s + 1
            if (s  > e):
                break;

def insert_element(n):
    global elem_count, fp_count
    is_fp = True
    for h in range(K):
        m = H[h](n)
        b = int(m.hexdigest(), 16) % N
        is_fp = is_fp and getbit(b)
        setbit(b)

    if (is_fp):
        fp_count = fp_count + 1

    elem_count = elem_count + 1

def query_element(n):
    r = True
    for h in range(K):
        m = H[h](n)
        b = int(m.hexdigest(), 16) % N
        if (getbit(b) == False):
            r = False
            break

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

def do_populate_using_config():
    with open(config_file) as f:
        for line in f:
            line = line.split(",")
            if line:
                if (int(line[1]) < int(line[2]) and  int(line[1] >= 1 )):
                    populatemap(line[0], int(line[1]), int(line[2]))
                    print "element count = %d fp = %d " % (elem_count, fp_count)

def do_exit():
    print "Exiting ...."
    exit(0)

options = {1: do_printmap, 2: do_insert_element, 3: do_query_element, 4:do_populate_using_config, 5: do_exit}

while True:
    print "Select an option\n"
    print "1. Print bitmap"
    print "2. Insert an element"
    print "3. Query an element"
    print "4. Populate bitmap using specified config file"
    print "5. Exit"
    option = raw_input()
    print "Option selected is (%d)\n\n" % int(option)
    options[int(option)]()
