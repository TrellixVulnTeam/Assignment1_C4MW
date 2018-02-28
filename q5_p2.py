from q5_p1 import password_check

while True:
    password = input("Please enter a password: ")
    if password_check(password):
        break
