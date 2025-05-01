import string

def check_password_strength(password):
    length = len(password)>=8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score=sum([length,has_upper,has_lower,has_digit,has_special])

    if score ==5:
        return "Strong"
    elif 3<=score <5:
        return "Medium"
    else:
        return "Weak"
    
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"The password strength is: {strength}")
