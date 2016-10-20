#task: to create a program that differentiates 3 term polynomials

yn = "no" #setting up for the while loop

#entering inputs n stuff
while (yn == "no"):
    print('so you need help differentiating something of the form ax^m + bx^n + cx^o...')
    input_a = input('a = ')
    input_b = input('b = ')
    input_c = input('c = ')
    input_m = input('m = ')
    input_n = input('n = ')
    input_o = input('o = ')

    a = float(input_a)
    b = float(input_b)
    c = float(input_c)
    m = float(input_m)
    n = float(input_n)
    o = float(input_o)

    yn = input('so ' + str(a)+'x^'+str(m)+ ' + ' +
              str(b)+'x^'+str(n)+ ' + ' +
              str(c)+'x^'+str(o)+
              ' is your function? (type no to go back): ')
#stopping code from being wrong if two values are typed in as 0
    if m == n: 
        yn = "no"
        print("nahhhhh... type in your polynomial less dumbly")
    elif n == m:
        yn = "no"
        print("nahhhhh... type in your polynomial less dumbly")
    elif m == o:
        yn = "no"
        print("nahhhhh... type in your polynomial less dumbly")
    else:
        yn = str(yn)
    

#the differentiation bit

if o == 0:
    m1 = m-1
    n1 = n-1
    o1 = 0
    a1 = a*m
    b1 = b*n
    c1 = 0

elif n == 0:
    m1 = m-1
    n1 = 0
    o1 = o-1
    a1 = a*m
    b1 = 0
    c1 = c*o

elif m == 0:
    m1 = 0
    n1 = n-1
    o1 = o-1
    a1 = 0
    b1 = b*n
    c1 = c*o

else:
    m1 = m-1
    n1 = n-1
    o1 = c-1
    a1 = a*m
    b1 = b*n
    c1 = c*o


#the output of the result
    
print( 'then... ' +
       str(a1)+'x^'+str(m1)+ ' + ' +
       str(b1)+'x^'+str(n1)+ ' + ' +
       str(c1)+'x^'+str(o1)+
       ' is your result!')
