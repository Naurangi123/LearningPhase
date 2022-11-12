import random

latters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z',
'a','b','c','d','e','f','g','h','i','j','k','l','m'
,'n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','+','(',')']

print("Welcome to password generator:")

nr_latters=int(input("How many latters would you like in your password\n"))

nr_numbers=int(input("How many numbers would you like in your password\n"))

nr_symbols=int(input("How many Symbols would you like in your password\n"))

#Eazy level

# password=""
# for char in range(1,nr_latters+1):
#     password+=random.choice(latters)
# for char in range(1,nr_symbols+1):
#     password+=random.choice(symbols)
# for char in range(1, nr_numbers):
#     password+=random.choice(numbers)
#     print(password)

# Hard level
password_list=[]

for char in range(1,nr_latters+1):
    password_list.append(random.choice(latters))

for char in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)

for char in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)

#print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char

print(f"your password is: {password}")



