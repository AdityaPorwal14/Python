#1.how to assign variable in short cut
# a,b=3,4
# print(a,b)

#2.how to change output color 
# print("\033[94m this is a different color")
#94m is change the colour you can increase the value and the color will change

#3.the best way to multiply the number
# print(5*5*5*5*5)
#the best way is this
# print(5**5)

#4.how to convert the round figer of numbers
# print(round(10.56))

#5.you can use the underscore between the value
# my_bank=87_232_452_24235
# print(my_bank) 

#6.how to open a wensite using the code
# import webbrowser
# webbrowser.open('https://www.codebreakthrough.com''/python-bootcamp')

#7.how to write long string in very easy way and you write the string in the list format 
# msg="this is a really " \
#     "long string for a very "\
#     "i am very hungry " \
#     "i hope you are the best stuent"
# print(msg)

#8.how to reverse a string
# str=[2,4,6]
# print(str[::-1])

#9.how to cheak list this is null
# list=[]
# print(len(list)==0)

# list=None
# print(not list)

# list=None
# print(list is None)

#10.how to show list data in the proper line
# list=['c','python','photoshop','design']
# print(list,end=" ")

#11.how to write list with the simple string
# name="aditya"
# age=17
# favourite_langauges= ['c++','python']
# print(f"{name} is {age} years old and love {favourite_langauges[0]} and {favourite_langauges[1]}")


#12.how to convert list into the simple word using * method
# data=[10,20,30]
# print(*data)

#12.how to write one if else condition in one line
# reputation=20
# status=None
# if reputation>15:
#     status="admin"
# else:
#     status="user"
#this is short cut rather then upper    
# status="admin" if reputation>15 else "user"
# print(status)

#13.multipal if condition in the program usingh this method
# weather = "stormy"
# if weather in ['rainy','stormy','snowy']:
#     print("cansel")

#14.how to write condition in one list and using the all and any method
# name="aditya"
# age=17
# reputation=20
# condition=[age<=21,reputation>=20]
# if all(condition):
#     print("admin")
# else:
#     print("standered user")

    