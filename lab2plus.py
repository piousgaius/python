#ask for triangle sides
a = float(input("enter your first side: "))
b = float(input("enter your second side: "))
c = float(input("enter your third and final side: "))

#calculate whether triangle is valid
if a > (b+c) or b > (a+c) or c > (a+b):
    print("yr triangel sux")
else:


#if triangle is valid then tell what kinda triangle it is
    print("nice tringle!")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 == a**2 + b**2:
        rangle = bool(1)
        print("you got urselv a good right angl")
    else:
        rangle = bool(0)
    if a == b or b == c or a == c:
        iso = bool(1)
        print("cool isosescleses triangle")
    else:
        iso = bool(0)
    if a == b == c:
        print("equalataral")
    if rangle == bool(0) and iso == bool(0):
        print("found a scary scalenen")
