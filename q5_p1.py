password = input("Please enter a password: ")


def length(the_password):
    if len(the_password) >= 8:
        return True
    else:
        return False

def numero_alpha(the_password):
    return False