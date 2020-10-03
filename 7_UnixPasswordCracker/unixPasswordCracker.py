import crypt
import time

# Open password file and read the data
password_file = 'myPassword.txt'
dict_file = 'dictionary.txt'

f = open(password_file, 'r')
fp = open(dict_file, 'r')

passwd_str = f.read()


# Splitting the password string
splitted_str = passwd_str.split(":")
hash_str = splitted_str[1]
h_id,salt,passwd_hash = hash_str.split('$')[1:4]
print(h_id,salt, passwd_hash)
input_salt = f'${h_id}${salt}'
print(input_salt)



for password in fp.readlines():
    # password = 'superman'
    calc_hash_value = crypt.crypt(password[:-1], input_salt)
    if(calc_hash_value == hash_str):
        print(f"Password is {password[:-1]}")
        break
    else:
        print(f"Wrong Password {password[:-1]}")
    # time.sleep(0.2)