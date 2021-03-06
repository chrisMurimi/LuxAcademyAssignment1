# code by Chris
import random  # random module
import string  # string module

# function generating the password


def password_generator():
    lower_case_letters = string.ascii_lowercase  # getting lower case strings
    upper_case_letters = string.ascii_uppercase  # getting upper case strings
    numbers = string.digits  # getting digit strings '0123456789'
    special_characters = string.punctuation  # getting the special character string

    # creating random strings
    lower = random.sample(lower_case_letters, 2)
    upper = random.sample(upper_case_letters, 2)
    num = random.sample(numbers, 2)
    special = random.sample(special_characters, 2)
    temp = upper + lower + num + special
    password = "".join(temp)
    return password


password_generator()
