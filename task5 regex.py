import re
def validate_email(email):
    pattern_email= r'^[a-zA-Z0-9._%+_]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'
    pattern_email=re.compile(pattern_email)
    return re.match(pattern_email,email) is not None
print(validate_email("sowndhu2000@gmail.com"))