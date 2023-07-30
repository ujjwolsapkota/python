x=input('Enter Number')
y=input('Enter second Number')
z=input('Enter third Number')
if int(x)>int(y) and int(x)>int(z) :
    print('greater is',x)

elif int(y)>int(x) and int(y)>int(z):
    print('greater is',y)


else:
    print('greater is',z)