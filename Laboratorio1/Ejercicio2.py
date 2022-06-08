import random
import string

def password_generator(num_digits, num_passwords):
    digits = string.digits + string.ascii_letters + string.punctuation
    for times in range(num_passwords):
        password = ''
        for i in range(num_digits):
            password += random.choice(digits)
        print(password)
        
num_digits = int(input('Elija la cantidad de caracteres para su contraseña: '))
num_passwords = int(input('Elija la cantidad de contraseñas a generar: '))
password_generator(num_digits, num_passwords)