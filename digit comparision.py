a = int(input())
b = int(input())
c = int(input())
if (a >= b) and (b >= c):
    print(f"{a}" + '\n' + f"{c}" + '\n' + f"{b}")
elif (a >= c) and (c >= b):
    print(f"{a}" + '\n' + f"{b}" + '\n' + f"{c}")
elif (b >= a) and (a >= c):
    print(f"{b}" + '\n' + f"{c}" + '\n' + f"{a}")
elif (b >= c) and (c >= a):
    print(f"{b}" + '\n' + f"{a}" + '\n' + f"{c}")
elif (c >= a) and (a >= b):
    print(f"{c}" + '\n' + f"{b}" + '\n' + f"{a}")
elif (c >= b) and (b >= a):
    print(f"{c}" + '\n' + f"{a}" + '\n' + f"{b}")


'''x = int( input() )
y = int( input() )
z = int( input() )

if x <= y <= z:
	print(z, "\n", x, "\n", y)
elif y <= x <= z:
	print(z, "\n", y, "\n", x)
elif y <= z <= x:
	print(x, "\n", y, "\n", z)
elif x <= z <= y:
	print(y, "\n", x, "\n", z)
elif z <= x <= y:
	print(y, "\n", z, "\n", x)
elif z <= y <= x:
	print(x, "\n", z, "\n", y)'''




    #print(a + '\n' + b + '\n'+ c)