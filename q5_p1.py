import re

def length(the_password):
    if len(the_password) >= 8:
        return True
    else:
        return False

def numero_alpha(the_password):
                    #\w
    if re.match(r'[A-Za-z0-9@#$%^&+=]', the_password):
        return True
    else:
        return False

def twice_consecutive(the_password):
    if re.findall(r'((\w)\2+)', the_password):
        return True
    else:
        return False

def ascending(the_password):
    str_array = list(the_password)
    for i in range(0, len(str_array)):
        if i + 1 == len(str_array):
            return False
        if (ord(str_array[i+1])) - ord(str_array[i]) == 1:
            if (ord(str_array[i + 2])) - ord(str_array[i]) == 2:
                return True
            else:
                continue
        else:
            continue

def distinct_character(the_password):
    pass_copy = the_password
    pass_copy = "".join(set(pass_copy))
    if  len(pass_copy) < (len(the_password)/2):
        return False
    else:
        return True

def password_check(the_password):
    if length(the_password):
        if numero_alpha(the_password) and not twice_consecutive(the_password) and not ascending(the_password) and distinct_character(the_password):
            return True
        else:
            return False
    else:
        return False