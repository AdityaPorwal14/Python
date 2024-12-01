print("\tpizza order program\t")
bill=0
size=(input("what pizza you want small/large/medium:"))
if(size=="small"):
    bill+=100
    print("you choosen the small pizza")
elif(size=="medium"):
    bill+=200
    print("you choosen the medim pizza")
elif(size=="large"):
    bill+=300
    print("you choosen the large pizza")
else:
    print("enter the right size of pizza")
add_peproni=input(print("do you want peproni yes/no\n"))
if(add_peproni=="yes"):
      if(size=="small"):
       bill+=30
      else:
       bill+=50
else:
   print("enter the right size")
extra_cheese=str(input("do you want extra cheese yes or no"))
if(extra_cheese=="yes"):
    bill+=20
print("your total bill is",bill)

