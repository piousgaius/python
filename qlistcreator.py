#this is to quickly input values for qlists in pure data
#needs to have a variable number of like variables or whatever

def qList(variables):
    print("nb, your first variable won't show on the output since it needs to be use for time delay or whatever")
    vList = []
    nList = []
    fuckLists = []
    a = 0
    countA = variables
    while countA > 0:
        placeholderA = raw_input("Variable name: ")
        vList.insert(0, placeholderA)
        countA = countA - 1
    vList.reverse()
    countB = int(input("how many lines do you want to input? "))
    countC = countB
    originalcountB = countB
    otheroriginalcountB = countB
    while countB > 0:
        placeholderB = int(input(vList[a%variables] + " = "))
        nList.insert(0, placeholderB)
        a = a + 1
        if originalcountB == countB:
            countB = countB*variables
            originalcountB = -1
        countB = countB - 1
    nList.reverse()
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
