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
for position in range(1,len(week_day_list)+1):
    print(f"The {position} position in day is: --> {week_day_list[position]}")

#enumerate function
for position,day in(week_day_list):
    print(f"The{position+1} ######## : -->{day}")

odd_list =[]
even_list=[]
def filter_odd_number(user_provided_num):
    for num in range(1,user_provided_num+1):
         if num % 2==0:
            even_list.append(num)
         else:
            odd_list.append(num)
    
any_num= int(input("Please provide anu number:-->"))   
filter_odd_number(any_num)

print(f"Now,the odd list is: {[odd_list]}")
print(f"Now,the even list is:{[even_list]}")    

