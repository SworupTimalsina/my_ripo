#loops in python
#range function in python
#print(f"The rage from 1 to 10 is: {range:1,18+1}")

#list object
num_list = []
week_day_list = [
"Sunday",
"Monday",
"Tuesday",
"Wenesday",
"Thursday",
"Friday",
"Saturday",]

for num in range(1,11):
    print(f"The number is range is --> {num}")
    num_list.append(num)

print(num_list)

counter=0
for day in week_day_list:
    counter += 1
    print(f"The {counter} day is : -->  {day}")

#same program with the help of range function
for position in range(len(week_day_list)):
    print(f"The {position} position in day is: --> {week_day_list[position]}")

#enumerate function
for position,day in enumerate(week_day_list):
    print(f"The{position+1} ######## : -->{day}")

odd_list =[]
even_list=[]
def filter_odd_number(user_provided_num):
    for num in range(1,user_provided_num+1):
        {even_list.append(num)if num%2 ==0 else odd_list.append(num)}
         
any_num= int(input("Please provide any number:-->"))   
filter_odd_number(any_num)

print(f"Now,the odd list is: {odd_list}")
print(f"Now,the even list is:{even_list}")    



#1 ask a num with user and filter odd and add into the odd list
#2 ask a num with user and filter even and odd into the even list
#3 ask a age with user and check he/she is elegible for vote(must be greater than 19)
# 4Application of loop into the week of day:
    #for eg:
# Day 1 --> Sunday 
# Day 2 --> Monday
#ask a first_name and second_name from user and retuen its full name as:
 #for eg: Oh! So,your fullname is:John Doe

