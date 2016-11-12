#this is to quickly input values for qlists in pure data
#slightly different way of doing it
#needs to have a variable number of like variables or whatever

def qList(variables):
    print("nb, your first variable won't show on the output since it needs to be use for time delay or whatever")
    vList = []
    nList = []
    fuckLists = []
    a = 0
    b = 0
    c = 1
    countA = variables
    while countA > 0:
        placeholderA = raw_input("Variable name: ")
        vList.insert(0, placeholderA)
        countA = countA - 1
    vList.reverse()
    countB = int(input("how many lines do you want to input? "))
    countC = countB
    originalcountB = countB
    variablecount = variables
    while variablecount > 0:
        while countB > 0:
            placeholderB = int(input(vList[a] + " = "))
            nList.insert(b, placeholderB)
            countB = countB - 1
            b = b + c
        c = c + 1
        b = c - 1
        a = a + 1
        countB = originalcountB
        variablecount = variablecount - 1
    a = 0
    countD = variables - 1
    originalcountD = countD
    print("")         
    print("clear; ")
    while countC > 0:
        print(str(nList[a])),
        while countD > 0:
            a = a+1
            countD = countD - 1
            print(str(vList[a%variables]) + " " + str(nList[a]) + ";"),
        print("")
        a = a+1
        countD = originalcountD
        countC = countC - 1
