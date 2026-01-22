#check if triangle or not
a=int(input("enter first angle:"))
b=int(input("enter second angle:"))
c=int(input("enter third angle:"))
if a>0 and b>0 and c>0 and (a+b+c==180):
    print("valid triangle")
else:
    print("not a valid triangle")
