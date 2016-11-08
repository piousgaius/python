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
