# # a=10
# # b=20
# # if (a>b):
# #     print("a is greater")
# # else:
# #     print("b is greater")

# n=int(input("enter a number:"))
# if(n%2!=0 or n>=6 and n<=20):
#     print("weird")
# elif(n<=2 and n>=5 or n>=20):
#     print("not weird")

# import math
# "area of circle"
# "area=pi*r*r"  
# radius=float(input("enter the radius:"))
# if(radius>0):
#      print(math.pi*radius*radius)
# else:
#      print("invalid radius")   

# a=int(input("enter number"))  
# b=int(input("enter number"))  
# c=int(input("enter number"))  
# if(a!=b and a!=c and b!=c):
#     print(1)
# else:
#     print(0)    
# m=int(input("enter number"))  
# n=int(input("enter number"))  
# if(m%n==0):
#     print(int(m/n))
# else:
# #     print(0)    
# a=int(input("enter number"))  
# b=int(input("enter number"))  
# c=int(input("enter number"))
# if(a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a):
#     print(1)
# else:
# #     print(0)    

# a=float(input("enter a number"))
# print("hello kese ho aap log")
# if(a>40):
#     print("you are pass and your number is",a)
# else:
#     print("you are fail bacause your number is",a)    
# # print("ha bhai aa gaya swad")    
# a=float(input("enter how many ammount you are shopping"))
# if(a<=10000 and a>0):
#     print("you get 10% \discount")
# elif(a>=10000 and a<=20000):
#     print("you get 20% \discount")
# elif(a<=30000 and a>=20000):
#     print("you get 30% \discount")
# elif(a>=30000):
#     print("you get 40% \discount") 
# else:
#     print("invalid number")             
# # print("thanks for menshioning")
# a=float(input("enter the value of a \n"))
# b=float(input("enter the value of b \n"))
# c=float(input("enter the value of c \n"))
# if(a>0 and a>b and a>c):
#     print("a is greater")
# elif(b>0 and b>a and b>c):
#     print("b is greater") 
# elif(c>0 and c>b and c>a):
#     print("c is greater")    
# else:
# #     ("thanku")       
# print("ram\t\t5000")
# print("radhakrishna\t5000")
# print("shyam\t\t5000")
# print("\t\t\t\t\t\t\t\tKUNDALI 2023\t\t\t\t\t\t\t\t")
# num=float(input("Enter your luckey number-->"))
# if(num>0 and num<10):
#     print("you are very intellegent \n you will grow in your life \n you are celebrity of future \n you are very cute")
# elif(num>10 and num<100):
#     print("you are best \n you tired in your life \n you are enginner of future")
# elif(num>100 and num<1000):
#     print("wow nice \n you are not a bad boy \n you are the future google ceo") 
# else:
#     print("enter the number in your limit \n you are very bad boy \n and go out from go there \n GO GO GO! ")   

time=float(input("enter the time"))
ampm=input("enter the time am/pm")
if(ampm=="am" and time>=5 and time<=12):
    print("gm")
elif(ampm=="pm"and time>12 and time<5):
    print("afternoon")
elif(ampm=="pm" and time>=5 and time<12):
    print("evening")
elif(ampm=="am" and time>=12 and time<5):
    print("morning")
else:
    print("bye")