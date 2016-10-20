#asking for numbers

a = input("enter your first number: ")
b = input("enter your second number: ")
c = input("enter your third number: ")
d = input("enter your fourth number: ")
e = input("enter your final number: ")


#calculate the mean

mean = (int(a)+int(b)+int(c)+int(d)+int(e))/5
print(mean)


#check what it's divisible by

if mean%3 == 0:
    print(str(mean) + " is divisible by 3")
else:
    print(str(mean) + " is not divisible by 3")
    
if mean%5 == 0:
    print(str(mean) + " is divisible by 5")
else:
    print(str(mean) + " is not divisible by 5")
