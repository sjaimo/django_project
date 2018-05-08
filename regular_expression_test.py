import re

def validate_phone_number(number):
    #016
    if not re.match(r'^01[016789][1-9]\d{6,7}$',number):
        return False
    return True

print(validate_phone_number('01012341234'))
print(validate_phone_number('0181234123'))
print(validate_phone_number('019123412'))
print(validate_phone_number('010123412345'))