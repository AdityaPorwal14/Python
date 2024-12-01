name=str(input("what is your name:"))
cgpa=float(input("what is your CGPA:"))
if(cgpa>0 and cgpa<9.5):
    calculate=cgpa*9.5
    print("your cgpa is:",calculate)
else:
    print("enter the right cgpa")

#feedback
if(cgpa>=8):
    print("you are good student",name,"keep it up\n i am vary happy to know you cgpa")
else:
    print("belive in yourself and keep growing")    