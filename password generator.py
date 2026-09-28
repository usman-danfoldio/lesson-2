import random
letters= ["a", "b", "c", "d"," e", "f", "g", "h", "i", "j", "k", "l", "m"
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E"
"F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z  "]
numbers= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols= ["!", "@", "#", "$","%", "^", "&", "*", "+" ]
print("=====Welcome to the PyPassword Generator=====")
how_many_letters=int(input("How many letters would you like in your passwords?\n"))

how_many_symbols=int(input("How many symbols would you like?\n"))
how_many_numbers=int(input("How many numbers would you like?\n"))

password_list= []
for i in range (1, how_many_letters + 1):
    password_list.append(random.choice(letters))


for i in range (1, how_many_numbers + 1):
    password_list += random.choice(numbers)


for i in range (1, how_many_symbols + 1):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)

password= ""
for char in password_list:
    password += char
print(f"Your password is:{password}")







# name = ["Danfoldio", "jago", "darasimi"]
# for name in name:
#     print(name)
    

# student_score= input().split()
# for n in range(0, len(student_score)):
#     student_score [n]=int(student_score[n])
# highest_score=0
# for score in student_score:
#     if score > highest_score:
#         highest_score=score
# print(f"The highest score in the class is: {highest_score}")



# target= int(input())
# even_sum=0
# for number in range(2, target + 1, 2):
#     even_sum += number
# print(even_sum) 



# target= 10
# for number in range(1, target + 1):
#     if number % 3== 0 and number % 5==0:
#         print("FizzBuzz")
#     elif number % 3==0:
#         print("Fizz")
#     elif number % 5==0:
#         print("Buzz")
#     else:
#         print(number)
    