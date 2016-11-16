matrix = []
row = []
count = 1
lister = []
quicklist = []
columnlist = []
columncount = 0
size = int(input("what size is your matrix? "))
print("left to right, top to bottom")
while len(matrix) < size:
    while len(row) < size:
        val = float(input("value " + str(count) + " = "))
        row.append(val)
        lister.append(val)
        count = count + 1
    matrix.append(row)
    row = []

count = 0
print("")
while count < size:
    while columncount < size**2:
        quicklist.append(lister[columncount])
        columncount += size
    quicklist.sort()
    bignum = quicklist[size-1]
    length = len(str(bignum))
    columnlist.append(length) 
    count +=1
    columncount = count
    quicklist = []
print(columnlist)

count = 0
print("")
print("sweet, this is your matrix")
for i in matrix:
    count1 = 0
    while count1 < size:
        print(str(matrix[count][count1]).ljust(columnlist[count1]) + " "),
        count1 += 1
    count += 1
    print("")
count = 0
count1 = 0

def rCW(matrix = matrix, size = size):
    lister = []
    count = 0
    count1 = size-1
    while len(lister) < size**2:
        while count < size:
            lister.insert(0, matrix[count][count1])
            count += 1
        count1 -= 1
        count = 0
    matrix = []
    row = []
    count = 0
    quicklist = []
    columnlist = []
    columncount = 0
    while len(matrix) < size:
        while len(row) < size:
            val = lister[count]
            row.append(val)
            count = count + 1
        matrix.append(row)
        row = []

    count = 0
    print("")
    while count < size:
        while columncount < size**2:
            quicklist.append(lister[columncount])
            columncount += size
        quicklist.sort()
        bignum = quicklist[size-1]
        length = len(str(bignum))
        columnlist.append(length) 
        count +=1
        columncount = count
        quicklist = []

    count = 0
    print("sweet, this is your matrix rotated clockwise")
    for i in matrix:
        count1 = 0
        while count1 < size:
            print(str(matrix[count][count1]).ljust(columnlist[count1]) + " "),
            count1 += 1
        count += 1
        print("")

def rACW(matrix = matrix, size = size):
    lister = []
    count = 0
    count1 = size-1
    while len(lister) < size**2:
        while count < size:
            lister.insert(0, matrix[count][count1])
            count += 1
        count1 -= 1
        count = 0

    matrix = []
    row = []
    count = 0
    quicklist = []
    columnlist = []
    columncount = 0
    while len(matrix) < size:
        while len(row) < size:
            val = lister[count]
            row.append(val)
            count = count + 1
        matrix.append(row)
        row = []

    lister = []
    count = 0
    count1 = size-1
    while len(lister) < size**2:
        while count < size:
            lister.insert(0, matrix[count][count1])
            count += 1
        count1 -= 1
        count = 0

    matrix = []
    row = []
    count = 0
    quicklist = []
    columnlist = []
    columncount = 0
    while len(matrix) < size:
        while len(row) < size:
            val = lister[count]
            row.append(val)
            count = count + 1
        matrix.append(row)
        row = []

    lister = []
    count = 0
    count1 = size-1
    while len(lister) < size**2:
        while count < size:
            lister.insert(0, matrix[count][count1])
            count += 1
        count1 -= 1
        count = 0

    matrix = []
    row = []
    count = 0
    quicklist = []
    columnlist = []
    columncount = 0
    while len(matrix) < size:
        while len(row) < size:
            val = lister[count]
            row.append(val)
            count = count + 1
        matrix.append(row)
        row = []
    

    count = 0
    print("")
    while count < size:
        while columncount < size**2:
            quicklist.append(lister[columncount])
            columncount += size
        quicklist.sort()
        bignum = quicklist[size-1]
        length = len(str(bignum))
        columnlist.append(length) 
        count +=1
        columncount = count
        quicklist = []

    count = 0
    print("sweet, this is your matrix rotated anti-clockwise")
    for i in matrix:
        count1 = 0
        while count1 < size:
            print(str(matrix[count][count1]).ljust(columnlist[count1]) + " "),
            count1 += 1
        count += 1
        print("")


def r180(matrix = matrix, size = size):
    lister = []
    count = 0
    count1 = size-1
    while len(lister) < size**2:
        while count < size:
            lister.insert(0, matrix[count][count1])
            count += 1
        count1 -= 1
        count = 0

    matrix = []
    row = []
    count = 0
    quicklist = []
    columnlist = []
    columncount = 0
    while len(matrix) < size:
        while len(row) < size:
            val = lister[count]
            row.append(val)
            count = count + 1
        matrix.append(row)
        row = []

    lister = []
    count = 0
    count1 = size-1
    while len(lister) < size**2:
        while count < size:
            lister.insert(0, matrix[count][count1])
            count += 1
        count1 -= 1
        count = 0

    matrix = []
    row = []
    count = 0
    quicklist = []
    columnlist = []
    columncount = 0
    while len(matrix) < size:
        while len(row) < size:
            val = lister[count]
            row.append(val)
            count = count + 1
        matrix.append(row)
        row = []
    

    count = 0
    print("")
    while count < size:
        while columncount < size**2:
            quicklist.append(lister[columncount])
            columncount += size
        quicklist.sort()
        bignum = quicklist[size-1]
        length = len(str(bignum))
        columnlist.append(length) 
        count +=1
        columncount = count
        quicklist = []

    count = 0
    print("sweet, this is your matrix rotated 180 degrees")
    for i in matrix:
        count1 = 0
        while count1 < size:
            print(str(matrix[count][count1]).ljust(columnlist[count1]) + " "),
            count1 += 1
        count += 1
        print("")

def hf(matrix = matrix, size = size):
    lister = []
    count = 0
    count1 = 0
    count2 = 0
    columncount = 0
    quicklist = []
    while count2 < size:
        matrix[count2].reverse()
        count2 += 1
    print(matrix)
    
    while len(lister) < size**2:
        while count < size:
            lister.insert(0, matrix[count1][count])
            count += 1
        count1 += 1
        count = 0
    print(matrix)
        
    count = 0
    print("")
    while count < size:
        while columncount < size**2:
            quicklist.append(lister[columncount])
            columncount += size
        quicklist.sort()
        bignum = quicklist[size-1]
        length = len(str(bignum))
        columnlist.append(length) 
        count +=1
        columncount = count
        quicklist = []
    print(matrix)

    count = 0
    print("sweet, this is your matrix flipped horizontally")
    for i in matrix:
        count1 = 0
        while count1 < size:
            print(str(matrix[count][count1]).ljust(columnlist[count1]) + " "),
            count1 += 1
        count += 1
        print("")

def vf(matrix = matrix, size = size, lister = lister):
    matrix.reverse()
    count = 0
    columncount = 0
    quicklist = []
    print("")
    while count < size:
        while columncount < size**2:
            quicklist.append(lister[columncount])
            columncount += size
        quicklist.sort()
        bignum = quicklist[size-1]
        length = len(str(bignum))
        columnlist.append(length) 
        count +=1
        columncount = count
        quicklist = []        

    count = 0
    print("sweet, this is your matrix flipped vertically")
    for i in matrix:
        count1 = 0
        while count1 < size:
            print(str(matrix[count][count1]).ljust(columnlist[count1]) + " "),
            count1 += 1
        count += 1
        print("")

