print("\t\t\t\t\t\t\t\t:simple calculator program:\t\t\t\t\t\t\t\t")
a=float(input("enter the first number:\n"))
b=input("enter the operation you perfome(+,-,*,/,**,//):\n")
c=float(input("enter the second number:\n"))
if(b=="+"):
    d=a+c
    print("the addition is",d)
elif(b=="-"):
    d=a-c
    print("the substraction is",d)
elif(b=="*"):
    d=a*c
    print("the multiplication is",d)
elif(b=="/"):
    d=a/c
    print("the division is",d) 
elif(b=="**"):
    d=a**c 
    print("the exponentel is",d)  
elif(b=="//"):
    d=a**c 
    print("the mod is",d)  
else:
    print("enter the right operation")    
               
   
   

