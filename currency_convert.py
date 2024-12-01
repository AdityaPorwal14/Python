#fix rate of currency 
exchange_usd_to_inr=83.24
exchange_usd_to_gbp=0.73
exchange_usd_to_eur=0.85

#display available currency option
print("inr=indian rupees")
print("usd=united state")
print("eur=euro")
print("gbp=british pound")

#get user input from source and target currency
source_currency=str(input("enter the source currency:"))
target_currency=str(input("enter the target currency:"))

#get the ammount to converter:
currency=float(input("enter the currency to convert:"))

#perform currency convertion based on user choise

if(source_currency=="usd" and target_currency=="inr"):
    print("the usd dollar into indian ruppes is:",currency*83.24)
elif(source_currency=="usd" and target_currency=="eur"):
    print("the usd into british pound is :",currency*0.85)   
elif(source_currency=="usd" and target_currency=="gbp"):
    print("the usd into gbp is:",currency*0.73)
else:
    print("enter the right currency")
