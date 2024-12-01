# how to create string single line and multiline string 
# print('this is single line quotes string')
# print("this is double line quotes string")
# print('''this is
#       muilti line string''')
# #message muilti line string
# a=print('''hi 
#    hello
# kese ho
#     badiya,aap batao
# me bhi badiya hu
#       ok by see you
# by good night
#       good night''')
#string concatenation
# name1 = input("enter your name")
# name2 = input("enter your name ")
# print(name1+name2)
# print("  ")
# print("  ")
# print("  ")
#string contenation
#1.using the '+' operator
# first_name="aditya"
# last_name="porwal"
# print(first_name + " " + last_name)
#2.concetenation muiltipal string
# name="aditya porwal"
# friend="rohan porwal"
# fan="nsb pictures"
# #example2
# print("hello"+" "+name+" " +"and hello"+" " +friend+" " +"and hello"+" " +fan)
# greeting="hello"
# subject="world"
# message=greeting+" " +"python"+" " +subject
# print(message)
# name="aditya"
# age=25
# description=("name:" + name + ",age:"+str(age))
# print(description)
# print(name + str(4))

# name="aditya porwal"
# print(name[-8:3:-1])
# name=("hello world")
# print(name[-7:-12:-1])
# print(name[-1::-1])
# print(name[6:11])
# name="python programming"
# print(name[2:3:-1])

'''string methode in python'''
# text="hello, world!"
# leanth=len(text)
# print(leanth)

# name = "aditya porwal"
# father_name = "shiv prakash porwal"
# print(name.lower())
# print(father_name.upper())
# text=""
# print(text.strip())
# name = " aditya porwal ".strip()
# father = "###shiv prakash porwal####".strip('#')
# mother = "@maya devi prowal@".strip('@')
# print(name,"\n",father,"\n",mother)
# print(name.strip())
# str = "i am jaspreet  ."
# print(str.lstrip('i am.'))
# print(str.rstrip('i am.'))
# print(str.strip())
# name  = " my name is jaspreet ".rstrip('my ')
# print(name)
# name="aditya,porwal@anshul@porwal"
# print(name.split(','))
# print(name.rsplit('@' , maxsplit=2))
# text = "aditya porwal"
# print(text.replace("porwal","kabra"))
# print(text.capitalize())
# print(text.casefold())
# name = "aditya porwal ji"
# print(name.replace(' ', '-',2))
# s = "Neso3academy3is3the3best3academy."
# print(s.replace('3',' '))
# name = "Aditya porwal"
# father ="SHIV"
# print(father.isupper())
# print(name.isupper())

# celebraity = "Elvish yadav"
# celebraity = "Elvishyadav"
# print(celebraity.isalpha())

# phone = "12345"
# print(phone.isnumeric())

# print("aadityporwal96@gmail.com".islower())
# print("aadityporwal96@gmail.com".upper())
# print("aadityporwal96@gmail.com".isalnum())

# name = "aditya"
# if name in ["john","bob","rohan"]:
#     print("access granted")
# else:
#     print("access not guranted")

# num1 = 1_0000_0000
# num2 = 2_0000_0000

# ans=num1*num2
# print(f'{ans:,}')

#string slicing
# x = [1,2,3,4,5,6,7,8,9,10]
# y = x[::-1]
# y = x[1:10:2]
# print(y)

# cholate = int(input("enter the cholate:"))
# childeren = int(input("enter the childern:"))
# total = int(cholate/childeren)
# print("childern par given:",total)
# remind = int(cholate%childeren)
# print("remind cholates",remind)

# #string concatenation
# name = "aditya porwal"
# father = "shiv prakash porwal"
# print(name+"welcome to the dell laptop")
# print(father + "of"+ name + "welcome to the dell laptop")

# print(name.upper())#ADITYA PORWAL
# print(name.lower())#aditya porwal
# print(name.capitalize())#Aditya prowal
# print(name.islower())#true
# print(name.isupper())#false
# print(name.strip())#aditya
# print(name.lstrip())#porwal
# print(name.rstrip())
# print(name.split())
# print(name.rsplit('#'))
# print(name.replace("porwal","kabra"))
# print(name.casefold())#aditya prowal
# print(name.isalpha())#false
# print(name.islower())#true
# print(name.isalnum())#false
# name = "aditya porwal from btti pilani rajasthan"
# print(name.count('a',0,8))
# name = "aditya porwal".isdigit()
# phone = "123456".isdigit()
# text = "python"
# print(text.center(66,'#'))
# name = "aditya\tporwal"
# print(name.expandtabs())
# name = "aditya porwal".title()
# print(name)
# name = "aditya porwal"
# print(name.isidentifier())
# a="wrids%23"
# print(a.isidentifier())
# a="aditgya".isidentifier()#true
# b="wos%^&&&".isidentifier()
# c=" ".isidentifier()
# d="9348".isidentifier()
# e="yurti_67".isidentifier()
# f="Y&^+_0".isidentifier()
# print(a,b,c,d,e,f)
# a = "aditya porwal"
# print(a.isprintable())
# b = "ashutosh_porwal123"
# print(b.isprintable())
# c = "2342sl\nfasjkfj"
# print(c.isprintable())
# a="rohanporwal"
# print(min(a))
# a = "aditya porwal".zfill(16)
# print(a)
# b = "-rohan porwal_14"
# c=b.zfill(len(b)+5)
# print(c)
# a = "my name is aditya aditya i am from pilani rajasthan"
# print(a.partition('my'))
# text = "python is fun"
# print(text.partition('python'))
# name = "my name is aditya".partition('my')
# print(name)
# name =input("enter your name")
# if(name.startswith('a')):
#     print("you are good")
# else:
#     print("bad")
# name = "my name is aditya porwal".capitalize()
# print(name)
# name = 'aditya porwal'
# father = 'shiv prakash porwal'
# mother = "maya devi porwal"
# print(f"your name is {name}\nyour father name is {father}\nyour mother name is {mother}")
# number = 100.000000
# print(f"number is {number:.2f}")
# print(f"{{20*30}}")
# a = 2
# b = 325
# c = 1272
# print("a=",a)
# print("b=",b)
# print("c=",c)
# print("")
# print("")
# print("")
# print("a =\t".expandtabs(6),a)
# print("b =\t".expandtabs(1),b)
# print("c =\t".expandtabs(0),c)
# print("")
# a = 65
# b = 3
# print(f"a=%#x\nb=%#x\nc=%d"%(a,b,(a+b)))
# a=234567.2324576857
# b=65
# c=66
# print(f"a=%6.1f"%a)
# print(f"a=%07.2f"%b)
# print(f"a=%19.2s"%c)
# print(f"b=%#o"%b)
# print(f"b=%#x"%c)
# x=65384023883
# y=3638469
# print(f"x=%0-11d"%x)
# print(f"x=%011d"%y)
# print(f"x=%011d"%c)
# a=38942.2492
# b=28324.23423
# c=42.52294273
# print(f"a=%013.4f"%a)
# print(f"b=%013.3f"%b)
# print(f"c=%013.9f"%c)
# n="aditya porwal"
# c="bhilwara"
# print("my name is {name} and i live in {city}.".format(name=n,city=c))
# marks=99.99
# name = "aditya"
# print(f"my name is {name} and i got {marks}%")
# num1=1
# num2=234
# num3=567
# num4=8910
# num5=11121314
# # print(f"%0d\n%0d\n%0d\n%0d\n%0d"%(num1,num2,num3,num4,num5))
# print(F"num1=%08d"%num1)
# print(F"num2=%08d"%num2)
# print(F"num3=%08d"%num3)
# print(F"num4=%08d"%num4)
# print(F"num5=%d"%num5)

# num=42
# print(f"%05d"%num)

# num=3.14159
# print(f"%-010.2f"%num)

# name="Hello"
# print(f"%-8s"%name)

# num="goodbye"
# print(f"num=%.4s"%num)

# hexa=12.34
# print(f"%e"%hexa)

# num=1.6180339887498948
# print(f"%15.5f"%num)

# num=255
# print(f"%-06x"%num)

# name = "aditya porwal".upper()
# father = "shiv prakash porwal".lower()
# mother = "maya devi porwal".title()#Maya Devi Porwal
# address = "bhilwara".capitalize()#Bhilwara
# print(f"{name}\n{father}\n{mother}\n{address}")

# school="SoHaRd ViDya nIkeTan BarlIyAS".casefold()
# print(f"{school}")

# shop = "porwal store".center(17,"$")
# print(shop)

# str="demiostringi"
# print(str.count("o",0,4))

# name = "my name is aditya porwal and i am living in the bhilwara city"
# print(name.rfind("bhil"))
# name="this is aditya".startswith("d",9,90)
# print(name)
# name="this is aditya".endswith("aditya",8,28)
# print(name)
# collage="birla\ttechnical\ttraining\tinstitue"
# print(collage.expandtabs(1))
# langauge = "this is python langauge"
# print(langauge.index("is",3,9))
# langauge = "this is a python and python is my favourite langauge"
# print(langauge.rindex("e",0,54))
# print(len(langauge))

# name = ["my","name","is","aditya","porwal"]
# print("_".join(name))

# name2={'student'.title():'aditya','father'.title():'shivprakshporwal'}
# print("or".swapcase().join(name2))

# name ='my name is aditya'
# print(name.rsplit(" ",maxsplit=2))

# name = "$aditya porwal"
# print(name.zfill(20))

# name = "my name is rohan porwal and aditya porwal"
# print(name.partition('porwal'))

# name = f"""{f'''{f'{f"{1+1}"}'}'''}"""
# print(name)

# name="aditya porwal"
# father = "shiv prakash porwal"
# mother = "maya devi porwal"
# introduction = f"my name is {name}." \
#                f"my father name is {father}." \
#                f"my mother name is {mother}."
# print(introduction)