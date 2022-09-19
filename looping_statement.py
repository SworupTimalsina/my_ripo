"""
def sum(_num1,_num2):
    print(f"sum={_num1+_num2}")
   

def laptop(_name,_model,_price):
    print (f"Your laptopname is {_name} and the model is {_model},the cost of laptop is {_price}.")

num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))

sum(num1,num2)

name=input("Enter your laptop name:")
model=input("Enter your laptop model:")
price=input("Enter the cost of laptop:")

laptop(name,model,price)
"""

##################################


def addition(_num1,_num2):
    sum=_num1+_num2
    return sum


def laptop_info(_name,_model,_price):
    return f"{_name} {_model} {_price}"   

num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))


print(addition(num1,num2))
name=input("Enter your laptop name:")
model=input("Enter your laptop model:")
price=input("Enter the cost of laptop:")

#print("Your laptopname is {_name} and the model is {_model},the cost of laptop is {_price}.")

print(laptop_info(name,model,price))

  