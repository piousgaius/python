#python 2048 programming thing for python 3.whatever

#setting stuff up
from random import *
from math import *
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
count = 0
count1 = 0



#randomly inserting 2 or 4
def newNum(matrix = matrix):
    thing = True
    numbersList = []
    count = 0
    count1 = 0
    while count < 4:
        while count1 < 4:
            numbersList.append([count, count1])
            count1 += 1
        count1 = 0
        count += 1
    numSelectList = [2, 2, 4]
    while thing == True :
        z = choice(numbersList)
        #print(z)
        x = z[0]
        y = z[1]
        if matrix[x][y] == 0:
            #print(matrix)
            matrix[x][y] = choice(numSelectList)
            #print(matrix)
            thing = False
        else:
            numbersList.remove([x, y])
    #print(matrix)
    return matrix
    

#check that u can make up moves
def checkU(matrix = matrix):
    mua = False
    cf = 1
    cg = 0
    while cf < 4 and mua == False:
        while cg < 4 and mua == False:
            if matrix[cf][cg] != 0 and matrix[cf-1][cg] == 0:
                mua = True
            elif matrix[cf][cg] == matrix[cf-1][cg] and matrix[cf][cg] != 0:
                mua = True
            else:
                mua = False
            cg += 1
        cg = 0
        cf += 1
    return bool(mua)

#check that u can make down moves
def checkD(matrix = matrix):
    mda = False
    cf = 1
    cg = 0
    while cf < 4 and mda == False:
        while cg < 4 and mda == False:
            if matrix[cf][cg] == 0 and matrix[cf-1][cg] != 0:
                mda = True
            elif matrix[cf][cg] == matrix[cf-1][cg] and matrix[cf][cg] != 0:
                mda = True
            else:
                mda = False
            cg += 1
        cg = 0
        cf += 1        
    return bool(mda)

#check that u can make right moves
def checkR(matrix = matrix):
    mra = False
    cf = 1
    cg = 0
    while cf < 4 and mra == False:
        while cg < 4 and mra == False:
            if matrix[cg][cf] == 0 and matrix[cg][cf-1] != 0:
                mra = True
            elif matrix[cg][cf] == matrix[cg][cf-1] and matrix[cg][cf] != 0:
                mra = True
            else:
                mra = False
            cg += 1
        cg = 0
        cf += 1
    return bool(mra)

#check that u can make left moves
def checkL(matrix = matrix):
    mla = False
    cf = 1
    cg = 0
    while cf < 4 and mla == False:
        while cg < 4 and mla == False:
            if matrix[cg][cf] != 0 and matrix[cg][cf-1] == 0:
                mla = True
            elif matrix[cg][cf] == matrix[cg][cf-1] and matrix[cg][cf] != 0:
                mla = True
            else:
                mla = False
            cg += 1
        cg = 0
        cf += 1
    return bool(mla)
    
#keeping things in line
def ktil(a, matrix = matrix):
    newMat = []
    b = 0
    while b < 4:
        newMat.append(len(str(matrix[b][a])))
        b += 1
    return max(newMat)

#print matrix function
def printMatrix(matrix = matrix):
    columnlist = []
    a = 0
    while a < 4:
        columnlist.append(ktil(a))
        a += 1
    count = 0
    for i in matrix:
        count1 = 0
        while count1 < 4:
            print(str(matrix[count][count1]).ljust(columnlist[count1]) + " ", end=' ')
            count1 += 1
        count += 1
        print("")

#get numbers back to nornal
def nbtn(matrix = matrix):
    cd = 0
    ce = 0
    while cd < 4:
        while ce < 4:
            x = log(matrix[cd][ce] + 0.1, 2)
            if matrix[cd][ce] > 0:
                matrix[cd][ce] = 2**int(x)
            ce += 1
        ce = 0
        cd += 1


#first round
#printMatrix()
#print(matrix)
#print(matrix[2][3])
#print(numbersList)
matrix = newNum()
matrix = newNum()
print("Let's do this! WASD controls")
printMatrix()
#print(matrix)

lonUL1 = [0, 1, 0, 2, 1, 0]
lonUL = [1, 2, 1, 3, 2, 1]
lonDR1 = [3, 2, 3, 1, 2, 3]
lonDR = [2, 1, 2, 0, 1, 2]
ca = 0
cb = 0
cc = 0
cd = 0

#mechanics of movement
#WASD input
while checkU() == True or checkD() == True or checkL() == True or checkR() == True:
    direction = input("Which way you wanna go? ")
    if bool(direction) == True:
        direction = direction.lower()
        direction = direction[0]
    ca = 0
    cb = 0
    cc = 0.1
    
    if direction == "w":
        if checkU() == True:
            while ca < 6:
                while cb < 4:
                    if matrix[lonUL1[ca]][cb] == 0:
                        matrix[lonUL1[ca]][cb] = matrix[lonUL[ca]][cb]
                        matrix[lonUL[ca]][cb] = 0
                    elif matrix[lonUL[ca]][cb] == matrix[lonUL1[ca]][cb]:
                        matrix[lonUL1[ca]][cb] = matrix[lonUL[ca]][cb]*2 + cc
                        matrix[lonUL[ca]][cb] = 0
                    cc += 0.1
                    cb += 1
                cb = 0
                ca += 1
            #print(matrix)
            nbtn()
            matrix = newNum()
        else:
            print("you can't do that ._.")

        
    elif direction == "a":
        if checkL() == True:
            while ca < 4:
                while cb < 6:
                    if matrix[ca][lonUL1[cb]] == 0:
                        matrix[ca][lonUL1[cb]] = matrix[ca][lonUL[cb]]
                        matrix[ca][lonUL[cb]] = 0
                    elif matrix[ca][lonUL[cb]] == matrix[ca][lonUL1[cb]]:
                        matrix[ca][lonUL1[cb]] = matrix[ca][lonUL[cb]]*2 + cc
                        matrix[ca][lonUL[cb]] = 0
                    cc += 0.1
                    cb += 1
                cb = 0
                ca += 1
            #print(matrix)
            nbtn()
            matrix = newNum()
        else:
            print("you can't do that ._.")
    
    elif direction == "s":
        if checkD() == True:
            while ca < 6:
                while cb < 4:
                    if matrix[lonDR1[ca]][cb] == 0:
                        matrix[lonDR1[ca]][cb] = matrix[lonDR[ca]][cb]
                        matrix[lonDR[ca]][cb] = 0
                    elif matrix[lonDR[ca]][cb] == matrix[lonDR1[ca]][cb]:
                        matrix[lonDR1[ca]][cb] = matrix[lonDR[ca]][cb]*2 + cc
                        matrix[lonDR[ca]][cb] = 0
                    cc += 0.1
                    cb += 1
                cb = 0
                ca += 1
            #print(matrix)
            nbtn()
            matrix = newNum()
        else:
            print("you can't do that ._.")

        
    elif direction == "d":
        if checkR() == True:
            while ca < 4:
                while cb < 6:
                    if matrix[ca][lonDR1[cb]] == 0:
                        matrix[ca][lonDR1[cb]] = matrix[ca][lonDR[cb]]
                        matrix[ca][lonDR[cb]] = 0
                    elif matrix[ca][lonDR[cb]] == matrix[ca][lonDR1[cb]]:
                        matrix[ca][lonDR1[cb]] = matrix[ca][lonDR[cb]]*2 + cc
                        matrix[ca][lonDR[cb]] = 0
                    cc += 0.1
                    cb += 1
                cb = 0
                ca += 1
            #print(matrix)
            nbtn()
            matrix = newNum()
        else:
            print("you can't do that ._.")
            
    else:
        print("huh?")

    printMatrix()
    #movesAvailable = ctust()

#losing screen
#printMatrix()
print("you have lost, loser")
