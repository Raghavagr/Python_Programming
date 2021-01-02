#you can run the code at below link:
# URL:  https://ide.geeksforgeeks.org/S8L7PgZNPB

import random

def getchar(char_list,number):
    temp_list = []
    for i in range(number):
        temp_list.append(random.choice(char_list))
    return temp_list

while True:
    num_char = int(input("enter the no. of char you want in password"))
    num_upper = int(input("enter the no. of upperCase char you want in password"))
    num_lower = int(input("enter the no. of LOwerCase char"))
    num_digit = int(input("enter the no. digits"))
    num_symbol = int(input("enter the no. symbols"))
    if num_char < num_upper + num_lower + num_digit +num_symbol:
        print("the character no. does not match")
    else:
        break

upper_list = [chr(i) for i in range(65, 65+26)]
upper_char = getchar(upper_list, num_upper)
lower_list = [chr(i) for i in range(97, 97+26)]
lower_char = getchar(lower_list,num_lower)
digit_list = [str(i) for i in range(0, 10)]
digit_char = getchar(digit_list,num_digit)
symbol_list = [chr(i) for i in range(32,48)]
symbol_list += [chr(i) for i in range(58,65)]
symbol_list += [chr(i) for i in range(91,97)]
symbol_list += [chr(i) for i in range(123,127)]
symbol_char = getchar(symbol_list,num_symbol)

num_unfilled_char = num_char - num_upper - num_lower - num_digit - num_symbol
whole_list = upper_list + lower_list + digit_list + symbol_list
remaining_char = getchar(whole_list, num_unfilled_char)

password = upper_char + lower_char + digit_char + symbol_char + remaining_char
random.shuffle(password)
password =''.join(password)
print(password)




URL : https://ide.geeksforgeeks.org/3tGMCOzmg8
