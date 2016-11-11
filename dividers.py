#for finding out what the current and or voltage are across a certain resistor if you know the total current slash voltage and the values of the resistors
def d(ZeroForVoltageOneForCurrent):
    a =0
    b =0
    c =0
    d =0
    e =0
    f =0
    g =0
    h =0
    i =0
    j =0
    k =0
    l =0
    m =0
    n =0
    o =0
    p =0
    q =0
    r =0
    s =0
    t =0
    u =0
    v =0
    w =0
    x =0
    y =0
    z =0
    List1 = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    List2 = []
    List3 = []
    num = int(input("how many known resistors do you have? "))
    newList = List1[0:num]
    count = 0
    while count <= num-1:
        newList[count] = float(input("enter resistor number " + str(count+1) + ": "))
        List2.insert(0, 1/float(newList[count]))
        List3.insert(0, float(newList[count]))
        count = count + 1
    ReqI = 1/sum(List2)
    ReqV = sum(List3)
    if ZeroForVoltageOneForCurrent == 0:
        Vt = float(input("total voltage = "))
        indexR = int(int(input("which number resistor do you want to measure the voltage across? "))-1)
        Rn = float(newList[indexR])
        Vn = (Vt * Rn)/ReqV
        print(str(Vn))
    elif ZeroForVoltageOneForCurrent == 1:
        It = float(input("total current = "))
        indexR = int(int(input("which number resistor do you want to measure the current across? "))-1)
        Rn = float(newList[indexR])
        In = (It * ReqI)/Rn
        print(str(In))
    else:
        print("you've fucked up")

#for working out how close your guess is to the answer for those e12 and e24 qs
def d2(N, T, ZeroforVoltsOneforAmps):
    print(str(N/T))
    print("for amps it's R1/(R1+R2), for volts it's R2/(R1+R2)")
    R1 = float(input("R1 = "))
    R2 = float(input("R2 = "))
    if ZeroforVoltsOneforAmps == 1:
        Req = 1/((1/R1)+(1/R2))
        print(str(Req/R2))
        print("R2 is in line with the ammeter")
    elif ZeroforVoltsOneforAmps == 0:
        Req = R1 + R2
        print(str(R2/Req))
        print("R2 being measured by the voltmeter")

#work out the resistance if you know the current across it
def d3(ZeroinlinewithUnknownOneinlinewithKnown):
    It = float(input("It = "))
    In = float(input("In = "))
    r = float(input("r = "))
    if ZeroinlinewithUnknownOneinlinewithKnown == 0:
        R = r*((It/In)-1)
    elif ZeroinlinewithUnknownOneinlinewithKnown ==1:
        R = r/((It/In)-1)
    else:
        R = "what the fuck mang"
    print(str(R))

#work out the resistance if you know the voltage across it
def d4(ZeroinlinewithUnknownOneinlinewithKnown):
    Vt = float(input("Vt = "))
    Vn = float(input("Vn = "))
    r = float(input("r = "))
    if ZeroinlinewithUnknownOneinlinewithKnown == 0:
        R = (r*Vn)/(Vt - Vn)
    elif ZeroinlinewithUnknownOneinlinewithKnown == 1:
        R = (r*(Vt - Vn))/Vn
    else:
        R = "what ? ??"
    print(str(R))

#work out the resistance if you know the voltage
#see sheet for what's what on this one, it's a bit fucked
def d5():
    v1 = float(input("v1 = "))
    v2 = float(input("v2 = "))
    r1 = float(input("r1 = "))
    r2 = float(input("r2 = "))
    req = r1 + r2
    print(((r2*v1)/req)-((r1*v2)/req))
