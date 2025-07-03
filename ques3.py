def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("test@example.com"))  
print(is_valid_email("invalidemail.com")) 
