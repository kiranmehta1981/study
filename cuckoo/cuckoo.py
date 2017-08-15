import hashlib
import sys
#Number of elements in hash table

if len(sys.argv) != 2 :
    print "Required format: <python> <program> <size of hash table>"
    sys.exit(0)

if int(sys.argv[1]) <= 0:
    print "Required format: <python> <program> <size of hash table>"
    sys.exit(0)

N=int(sys.argv[1])

F=[hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]
#Number of hash tables
T = len(F)

#Default value in hash table
DEFAULT=-1

#Number of insert attempts before giving up
R = 10

#storage for hashed data
H = [[DEFAULT for x in range(N)] for y in range(T)]

def hash(h, n):
    m = F[h](str(n))
    return int(m.hexdigest(), 16) % N

def printmap():
    count = 0
    for i in range(T):
        for j in range(N):
            if H[i][j] != DEFAULT:
                print " Table %d value[%d]" % (i, H[i][j])
                count = count  + 1
    print "Total elements  = %d" % (count)

def populatemap(filename):
    with open(filename) as f:
        for line in f:
            line = line.split()
            if line:
                for n in line:
                    print "Inserting element %s" % (n)
                    insert_element(int(n))

def insert_element_in_table(t, n):
    print "insert_element_in_table: t = %d n = %d  hash = %d" % (t,n, hash(t, n))
    if (H[t][hash(t, n)] == n):
        return n   
    else:
        oldval = H[t][hash(t,n)]
        H[t][hash(t,n)] = n
        return oldval

def insert_element(n):
    t = 0
    for r in range(R):
        for t in range(T):
            print "Attempting insertion of %d " % (n)
            d = insert_element_in_table(t, n)
            if (d == n or d == DEFAULT):
	        print "* Element inserted "
                return True
            else:
                print "Displaced element %d from 1st table " % (d)
                n = d

    print "=Could not insert value in hash table. Threshold reached="
    return False

def query_element(n):
    for t in range(T):
        if (H[t][hash(t, n)] == n):
            print "Element %s present in hash table" % (n)
            return True
    return False 

def do_printmap():
    printmap()

def do_insert_element():
    n = raw_input("Enter the element to be inserted: ")
    insert_element(int(n))

def do_query_element():
    n = raw_input("Enter the element to be queried: ")
    r = query_element(int(n))
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
    print "1. Print all elements"
    print "2. Insert an element"
    print "3. Query an element"
    print "4. Populate cuckoo hash table using file"
    print "5. Exit"
    option = raw_input()
    print "Option selected is (%d)\n\n" % int(option)
    options[int(option)]()
                              

