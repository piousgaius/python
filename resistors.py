#this is the chain gang aspect of the program, it is for working out how (up to) four resistors should be linked in a resistor network when you’ve been given the total resistance across two points
def cg():
    #setting up all the variables
    print("layout of resistors: a is top left, b is bottom left, c is top right, d is bottom right")
    R = float(input("Total Resistance = "))
    a = float(input("Resistor a = "))
    b = float(input("Resistor b = "))
    c = float(input("Resistor c = "))
    d = float(input("Resistor d = "))
    
    #now for all the possible variations
    r1 = a
    r2 = b
    r3 = c
    r4 = d
    r5 = a + b
    r6 = a + c
    r7 = a + d
    r8 = b + c
    r9 = b + d
    r10 = c + d
    r11 = a + b + c
    r12 = a + b + d
    r13 = a + c + d
    r14 = b + c + d
    r15 = a + b + c + d
    r16 = 1/((1/a) + (1/b))
    r17 = 1/((1/a) + (1/c))
    r18 = 1/((1/a) + (1/d))
    r19 = 1/((1/b) + (1/c))
    r20 = 1/((1/b) + (1/d))
    r21 = 1/((1/c) + (1/d))
    r22 = 1/((1/a) + (1/b) + (1/c))
    r23 = 1/((1/a) + (1/b) + (1/d))
    r24 = 1/((1/a) + (1/c) + (1/d))
    r25 = 1/((1/b) + (1/c) + (1/d))
    r26 = 1/((1/a) + (1/b) + (1/c) + (1/d))
    r27 = c + r16
    r28 = d + r16
    r29 = b + r17
    r30 = d + r17
    r31 = b + r18
    r32 = c + r18
    r33 = a + r19
    r34 = d + r19
    r35 = a + r20
    r36 = c + r20
    r37 = a + r21
    r38 = b + r21
    r39 = d + r27
    r40 = d + r29
    r41 = c + r31
    r42 = d + r33
    r43 = c + r35
    r44 = b + r37
    r45 = d + r22
    r46 = c + r23
    r47 = b + r24
    r48 = a + r25
    r49 = 1/((1/(a+b)) + (1/c))
    r50 = 1/((1/(a+b)) + (1/d))
    r51 = 1/((1/(a+c)) + (1/b))
    r52 = 1/((1/(a+c)) + (1/d))
    r53 = 1/((1/(a+d)) + (1/b))
    r54 = 1/((1/(a+d)) + (1/c))
    r55 = 1/((1/(b+c)) + (1/a))
    r56 = 1/((1/(b+c)) + (1/d))
    r57 = 1/((1/(b+d)) + (1/a))
    r58 = 1/((1/(b+d)) + (1/c))
    r59 = 1/((1/(c+d)) + (1/a))
    r60 = 1/((1/(c+d)) + (1/b))
    r61 = 1/((1/(a+b)) + (1/c) + (1/d))
    r62 = 1/((1/(a+c)) + (1/b) + (1/d))
    r63 = 1/((1/(a+d)) + (1/b) + (1/c))
    r64 = 1/((1/(b+c)) + (1/a) + (1/d))
    r65 = 1/((1/(b+d)) + (1/a) + (1/c))
    r66 = 1/((1/(c+d)) + (1/a) + (1/a))
    r67 = 1/((1/(a+b+c)) + (1/d))
    r68 = 1/((1/(a+b+d)) + (1/c))
    r69 = 1/((1/(a+c+d)) + (1/b))
    r70 = 1/((1/(b+c+d)) + (1/a))
    r71 = 1/((1/(a+b)) + (1/(c+d)))
    r72 = 1/((1/(a+c)) + (1/(b+d)))
    r73 = 1/((1/(a+d)) + (1/(b+c)))
    r74 = r49 + d
    r75 = r50 + c
    r76 = r51 + d
    r77 = r52 + b
    r78 = r53 + c
    r79 = r54 + b
    r80 = r55 + d
    r81 = r56 + a
    r82 = r57 + c
    r83 = r58 + a
    r84 = r59 + b
    r85 = r60 + a
    
    #now to take the absolute value of the total resistance minus each of the variations since the correct answer won’t be exact and we want to find out whichever answer is closest
    rn1 = abs(R - r1)
    rn2 = abs(R - r2)
    rn3 = abs(R - r3)
    rn4 = abs(R - r4)
    rn5 = abs(R - r5)
    rn6 = abs(R - r6)
    rn7 = abs(R - r7)
    rn8 = abs(R - r8)
    rn9 = abs(R - r9)
    rn10 = abs(R - r10)
    rn11 = abs(R - r11)
    rn12 = abs(R - r12)
    rn13 = abs(R - r13)
    rn14 = abs(R - r14)
    rn15 = abs(R - r15)
    rn16 = abs(R - r16)
    rn17 = abs(R - r17)
    rn18 = abs(R - r18)
    rn19 = abs(R - r19)
    rn20 = abs(R - r20)
    rn21 = abs(R - r21)
    rn22 = abs(R - r22)
    rn23 = abs(R - r23)
    rn24 = abs(R - r24)
    rn25 = abs(R - r25)
    rn26 = abs(R - r26)
    rn27 = abs(R - r27)
    rn28 = abs(R - r28)
    rn29 = abs(R - r29)
    rn30 = abs(R - r30)
    rn31 = abs(R - r31)
    rn32 = abs(R - r32)
    rn33 = abs(R - r33)
    rn34 = abs(R - r34)
    rn35 = abs(R - r35)
    rn36 = abs(R - r36)
    rn37 = abs(R - r37)
    rn38 = abs(R - r38)
    rn39 = abs(R - r39)
    rn40 = abs(R - r40)
    rn41 = abs(R - r41)
    rn42 = abs(R - r42)
    rn43 = abs(R - r43)
    rn44 = abs(R - r44)
    rn45 = abs(R - r45)
    rn46 = abs(R - r46)
    rn47 = abs(R - r47)
    rn48 = abs(R - r48)
    rn49 = abs(R - r49)
    rn50 = abs(R - r50)
    rn51 = abs(R - r51)
    rn52 = abs(R - r52)
    rn53 = abs(R - r53)
    rn54 = abs(R - r54)
    rn55 = abs(R - r55)
    rn56 = abs(R - r56)
    rn57 = abs(R - r57)
    rn58 = abs(R - r58)
    rn59 = abs(R - r59)
    rn60 = abs(R - r60)
    rn61 = abs(R - r61)
    rn62 = abs(R - r62)
    rn63 = abs(R - r63)
    rn64 = abs(R - r64)
    rn65 = abs(R - r65)
    rn66 = abs(R - r66)
    rn67 = abs(R - r67)
    rn68 = abs(R - r68)
    rn69 = abs(R - r69)
    rn70 = abs(R - r70)
    rn71 = abs(R - r71)
    rn72 = abs(R - r72)
    rn73 = abs(R - r73)
    rn74 = abs(R - r74)
    rn75 = abs(R - r75)
    rn76 = abs(R - r76)
    rn77 = abs(R - r77)
    rn78 = abs(R - r78)
    rn79 = abs(R - r79)
    rn80 = abs(R - r80)
    rn81 = abs(R - r81)
    rn82 = abs(R - r82)
    rn83 = abs(R - r83)
    rn84 = abs(R - r84)
    rn85 = abs(R - r85)
    
    #time to put them in a list in and find return find the smallest value
    fohl = [rn1, rn2, rn3, rn4, rn5, rn6, rn7, rn8, rn9, rn10, rn11, rn12, rn13, rn14, rn15, rn16, rn17, rn18, rn19, rn20, rn21, rn22, rn23, rn24, rn25, rn26, rn27, rn28, rn29, rn30, rn31, rn32, rn33, rn34, rn35, rn36, rn37, rn38, rn39, rn40, rn41, rn42, rn43, rn44, rn45, rn46, rn47, rn48, rn49, rn50, rn51, rn52, rn53, rn54, rn55, rn56, rn57, rn58, rn59, rn60, rn61, rn62, rn63, rn64, rn65, rn66, rn67, rn68, rn69, rn70, rn71, rn72, rn73, rn74, rn75, rn76, rn77, rn78, rn79, rn80, rn81, rn82, rn83, rn84, rn85]
    if min(fohl) == rn1:
        print("a")
    if min(fohl) == rn2:
        print("b")
    if min(fohl) == rn3:
        print("c")
    if min(fohl) == rn4:
        print("d")
    if min(fohl) == rn5:
        print("a isw b")
    if min(fohl) == rn6:
        print("a isw c")
    if min(fohl) == rn7:
        print("a isw d")
    if min(fohl) == rn8:
        print("b isw c")
    if min(fohl) == rn9:
        print("b isw d")
    if min(fohl) == rn10:
        print("c isw d")
    if min(fohl) == rn11:
        print("a isw b isw c")
    if min(fohl) == rn12:
        print("a isw b isw d")
    if min(fohl) == rn13:
        print("a isw c isw d")
    if min(fohl) == rn14:
        print("b isw c isw d")
    if min(fohl) == rn15:
        print("a isw b isw c isw d")
    if min(fohl) == rn16:
        print("a pt b")
    if min(fohl) == rn17:
        print("a pt c")
    if min(fohl) == rn18:
        print("a pt d")
    if min(fohl) == rn19:
        print("b pt c")
    if min(fohl) == rn20:
        print("b pt d")
    if min(fohl) == rn21:
        print("c pt d")
    if min(fohl) == rn22:
        print("a pt b pt c")
    if min(fohl) == rn23:
        print("a pt b pt d")
    if min(fohl) == rn24:
        print("a pt c pt d")
    if min(fohl) == rn25:
        print("b pt c pt d")
    if min(fohl) == rn26:
        print("a pt b pt c pt d")
    if min(fohl) == rn27:
        print("c isw a pt b")
    if min(fohl) == rn28:
        print("d isw a pt b")
    if min(fohl) == rn29:
        print("b isw a pt c")
    if min(fohl) == rn30:
        print("d isw a pt c")
    if min(fohl) == rn31:
        print("b isw a pt d")
    if min(fohl) == rn32:
        print("c isw a pt d")
    if min(fohl) == rn33:
        print("a isw b pt c")
    if min(fohl) == rn34:
        print("d isw b pt c")
    if min(fohl) == rn35:
        print("a isw b pt d")
    if min(fohl) == rn36:
        print("c isw b pt d")
    if min(fohl) == rn37:
        print("a isw c pt d")
    if min(fohl) == rn38:
        print("b isw c pt d")
    if min(fohl) == rn39:
        print("c isw d isw a pt b")
    if min(fohl) == rn40:
        print("b isw d isw a pt c")
    if min(fohl) == rn41:
        print("b isw c isw a pt d")
    if min(fohl) == rn42:
        print("a isw d isw b pt c")
    if min(fohl) == rn43:
        print("a isw c isw b pt d")
    if min(fohl) == rn44:
        print("a isw b isw c pt d")
    if min(fohl) == rn45:
        print("d isw a pt b pt c")
    if min(fohl) == rn46:
        print("c isw a pt b pt d")
    if min(fohl) == rn47:
        print("b isw a pt c pt d")
    if min(fohl) == rn48:
        print("a isw b pt c pt d")
    if min(fohl) == rn49:
        print("ab pt c")
    if min(fohl) == rn50:
        print("ab pt d")
    if min(fohl) == rn51:
        print("ac pt b")
    if min(fohl) == rn52:
        print("ac pt d")
    if min(fohl) == rn53:
        print("ad pt b")
    if min(fohl) == rn54:
        print("ad pt c")
    if min(fohl) == rn55:
        print("bc pt a")
    if min(fohl) == rn56:
        print("bc pt d")
    if min(fohl) == rn57:
        print("bd pt a")
    if min(fohl) == rn58:
        print("bd pt c")
    if min(fohl) == rn59:
        print("cd pt a")
    if min(fohl) == rn60:
        print("cd pt b")
    if min(fohl) == rn61:
        print("ab pt c pt d")
    if min(fohl) == rn62:
        print("ac pt b pt d")
    if min(fohl) == rn63:
        print("ad pt b pt c")
    if min(fohl) == rn64:
        print("bc pt a pt d")
    if min(fohl) == rn65:
        print("bd pt a pt c")
    if min(fohl) == rn66:
        print("cd pt a pt b")
    if min(fohl) == rn67:
        print("abc pt d")
    if min(fohl) == rn68:
        print("abd pt c")
    if min(fohl) == rn69:
        print("acd pt b")
    if min(fohl) == rn70:
        print("bcd pt a")
    if min(fohl) == rn71:
        print("ab pt cd")
    if min(fohl) == rn72:
        print("ac pt bd")
    if min(fohl) == rn73:
        print("ad pt bc")
    if min(fohl) == rn74:
        print("d isw ab pt c")
    if min(fohl) == rn75:
        print("c isw ab pt d")
    if min(fohl) == rn76:
        print("d isw ac pt b")
    if min(fohl) == rn77:
        print("b isw ac pt d")
    if min(fohl) == rn78:
        print("c isw ad pt b")
    if min(fohl) == rn79:
        print("b isw ad pt c")
    if min(fohl) == rn80:
        print("d isw bc pt a")
    if min(fohl) == rn81:
        print("a isw bc pt d")
    if min(fohl) == rn82:
        print("c isw bd pt a")
    if min(fohl) == rn83:
        print("a isw bd pt c")
    if min(fohl) == rn84:
        print("b isw cd pt a")
    if min(fohl) == rn85:
        print("a isw cd pt b")
    print("isw means -in series with-")
    print("pt means -parallel to-")
    return;

#this is to solve those problems that look like a figure 8
def f():
    #setting up variables
    print("layout: a is top left, b is top right, c is centre, d is bottom left, e is bottom right")
    a = float(input("Resistor a = "))
    b = float(input("Resistor b = "))
    c = float(input("Resistor c = "))
    d = float(input("Resistor d = "))
    e = float(input("Resistor e = "))

    #calculations
    #see http://www.calvin.edu/~svleest/circuitExamples/equRes/irred.ans.html for why this works
    v = (a*b*d + a*c*d + b*c*d + a*b*e + a*c*e + b*c*e + a*d*e + b*d*e)/(a*b + a*c + b*c + b*d + c*d + a*e + c*e + d*e)
    print(v)
    return;
