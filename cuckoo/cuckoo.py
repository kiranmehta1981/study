import hashlib
from sys import exit
#Number of elements in hash table
N=2
#Number of hash tables
T = 2

DEFAULT=0

#Number of inserth attempts before giving up
threshold = 10

#storage for hashed data
H = [[DEFAULT for x in range(N)] for y in range(T)]

def hash(h, n):
    if (h == 0):
        m = hashlib.md5(str(n))
        return int(m.hexdigest(), 16) % N
    else:
        m = hashlib.sha1(str(n))
        return int(m.hexdigest(), 16) % N

def printmap():
    for i in range(T):
        for j in range(N):
            print " Table %d value[%d]" % (i, H[i][j])

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
        return int(n)   
    else:
        oldval = H[t][hash(t,n)]
        H[t][hash(t,n)] = n
        return oldval

def insert_element(n):
    t = 0
    for i in range(threshold):
        print "Attempting insertion of %d " % (n)
        r = insert_element_in_table(t, n)
        if (r == n or r == DEFAULT):
	    print "* Element inserted "
            return True
        else:
            print "Displaced element %d from 1st table " % (r)
            n = r
            r = insert_element_in_table(t+1 % T, n)
            if (r == n or r == DEFAULT):
	        print "** Element inserted "
                return True
            print "Displaced element %d from 2nd table" % (r)
        n = r

    print "=======Could not insert value in hash table. Threshold reached======"
    return False

def query_element(n):
    if (H[0][hash(0, n)] == n):
        print "Element %s present in hash table" % (n)
        return True
    elif (H[1][hash(1, n)] == n):
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
                              

