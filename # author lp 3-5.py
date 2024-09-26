# author lp 3-5
import re

def validate_username(username):
    
    if len(username) < 6 or len(username) > 12:
        return False
    
    
    if not username[0].isalpha():
        return False
    
    
    if not username.isalnum() and not username.endswith('123') and not username.endswith('!'):
        return False

    
    if not (username.endswith('123') or username.endswith('!')):
        return False
    
    return True


print(validate_username("logan123"))  
print(validate_username("logan!"))    
print(validate_username("logan"))    
print(validate_username("log!an"))    
print(validate_username("lo123"))       
