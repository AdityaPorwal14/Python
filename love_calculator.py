print("\tthis is love calculator\t")
boy=(input("enter your name\n"))
girl=(input("enter your girlfriend name\n"))
combine_string=boy+girl
lower_case_string=combine_string.lower()
t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true=t+r+u+e
l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love=l+o+v+e

love_score=int(str(true)+str(love))
print("Your Love Score Is",love_score)
if(love_score<10 and love_score>90):
    print("you are ture lover")
elif(love_score>=40 and love_score<=50):
    print("you are all right and future may be you are lover")
else:
    print("they are made for each other")
