#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(10, 12)
nr_symbols = random.randint(5, 8)
nr_numbers = random.randint(4, 6)

password_list = []

#Use List Comprehension
password_list+=[random.choice(letters) for char in range(nr_letters)]
password_list+=[random.choice(symbols) for char in range(nr_symbols)]
password_list+=[random.choice(numbers) for char in range(nr_numbers)]

# for char in range(nr_letters):
#   password_list.append(random.choice(letters))

# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)
#
random.shuffle(password_list)
#
#Use the join method
password="".join(password_list)
# password = ""
# for char in password_list:
#   password += char

print(f"Your password is: {password}")