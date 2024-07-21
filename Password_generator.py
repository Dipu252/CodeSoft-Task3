import string
import random

string_lower=string.ascii_lowercase

string_upper=string.ascii_uppercase

string_digit=string.digits

string_special=string.punctuation

complete_string=[]

complete_string.extend(list(string_lower))
complete_string.extend(list(string_digit))
complete_string.extend(list(string_special))
complete_string.extend(list(string_upper))

random.shuffle(complete_string)

length=int(input("Enter password length: "))
password="".join(complete_string[:length])
print(password)