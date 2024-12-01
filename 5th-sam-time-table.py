print("this is cs-5th sam time table".title().center(200,'-').upper())
day=input("enter the today day name".lower().title())
d="day"
t="time"
tea="teacher"
if(day=='monday'):
    print(f"%s\t%26s\t%22s"%(d,t,tea))
    print("""Monday\t09:00 to 10:00\t1.D.Bhattacharjee
Monday\t10:00 to 11:00\t2.Dasrath sigh
Monday\t11:00 to 12:00\t3.Bhawani Kanwar
Monday\t12:00 to 01:00\t4.Dasrath Singh""".expandtabs(25))
elif(day=='tuesday'):
    print(f"%s\t%26s\t%22s"%(d,t,tea))
    print("""Tuesday\t09:00 to 10:00\t1.D.Bhattacharjee
Tuesday\t10:00 to 11:00\t2.Niranjan Sharma
Tuesday\t11:00 to 12:00\t3.Dasrath Singh
Tuesday\t12:00 to 01:00\t4.Narendra Kumar""".expandtabs(25))
elif(day=='wednesday'):
    print(f"%s\t%26s\t%22s"%(d,t,tea))
    print("""Wednesday\t09:00 to 10:00\t1.Dasrath Singh
Wednesday\t10:00 to 11:00\t2.Niranjan Sharma
Wednesday\t11:00 to 12:00\t3.Dasrath Singh
Wednesday\t12:00 to 01:00\t4.Bhawani Kanwar""".expandtabs(25))
elif(day=='thursday'):
    print(f"%s\t%26s\t%22s"%(d,t,tea))
    print("""Thursday\t09:00 to 10:00\t1.Dasrath Singh
Thursday\t10:00 to 11:00\t2.Bhawani Kanwar
Thursday\t11:00 to 12:00\t3.Dasrath Singh
Thursday\t12:00 to 01:00\t4.Deepak Saini""".expandtabs(25))
elif(day=='friday'):
    print(f"%s\t%26s\t%22s"%(d,t,tea))
    print("""Friday\t09:00 to 10:00\t1.Dasrath Singh
Friday\t10:00 to 11:00\t2.Bhawani Kanwar
Friday\t11:00 to 12:00\t3.D.Bhattacharjee
Friday\t12:00 to 01:00\t4.Niranjan Sharma
Friday\t02:30 to 04:00\t2.Bhawani Kanwar(Lab)""".expandtabs(25))
elif(day=='saturday'):
    print(f"%s\t%26s\t%22s"%(d,t,tea))
    print("""Friday\t09:00 to 10:00\t1.D.Bhattacharjee
Friday\t10:00 to 11:00\t2.Dasrath Singh
Friday\t11:00 to 12:00\t3.Niranjan Sharma
Friday\t12:00 to 01:00\t4.Bhawani Kanwar""".expandtabs(25))
elif(day=='sunday'):
    print("its holiday time\nuper ke 7 din aa jayega jo hi bahut badi bat he hamare liye\nja chill kar".title())
else:
    print("enter the right day name or Spelling".title())    