import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567891011121314@£§€"

while 1:
    password_len = int(input("what lenght would you like your password to be ? "))
    password_count = int(input("how many passwords would you like ? "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("here is your password : ", password)
        


