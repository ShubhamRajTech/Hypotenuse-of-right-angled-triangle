a= int(input("Enter the length of base:"))
b= int(input("Enter the length of perpendicular:"))
c= a**2
d= b**2
e= c+d
f= e**0.5
g= "{:.2f}".format(f)
print("Hypotenuse of right angled triangle is:" ,g)
