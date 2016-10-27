#setting stuff up

k0 = 1
k1 = 1

#inputting what numbers you want


n = input("n = ")


#the calculation


if int(n) == 2:
	k = 1
elif int(n) == 1:
	k = 1
elif int(n) == 0:
	k = 0
else:
  while int(n)-2 > 0:
	  k = k0 + k1
	  k0 = k1
	  k1 = k
	  n = n-1


#output


print("your number is " + str(k))
