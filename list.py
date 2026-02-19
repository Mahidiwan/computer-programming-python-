#WAP to find out no.of boys and girls in the list
students=input("enter student names:").split()
print(type(students),students)
boys=0
girls=0
for i in students:
    if isinstance(i,tuple):
        l=len(i)
        boys+=l
    else:
        girls+=1
print("boys:",boys)
print("girls:",girls)
        

   
