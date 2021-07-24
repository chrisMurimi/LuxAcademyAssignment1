import random
import string

def password_generator():
    lower_case_letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    all_characters = lower_case_letters + upper_case_letters + numbers + special_characters
    temp = random.sample(all_characters,8)
    password="".join(temp)
    return password

print(password_generator())