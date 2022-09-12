age=int(input("Please provide your age:"))

#conditional statement
#if block only
print("Code started.....")
if age>18:
    print (f"You can play this game because your age is {age}.")
 
print ("Code ended.....")

#if-else block
if age>18:
    print (f"You can play this game because your age is {age}.")
else:
    print (f"You need to be above 18 years old to play these game.")

    ##proper use of if-elif-else block
if age<0:
    print ("Please eneter your valid age.")
elif 0<age<=10:
        print("So you are a kid,your movie ticket is Rs100.")
elif 10<age<=20:
        print ("Your movie ticket is Nrs.200.") 
else:
        print ("Your movie ticket is Nrs.300.")    