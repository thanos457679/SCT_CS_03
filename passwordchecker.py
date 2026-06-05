import re

print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter Password: ")

if password == "":
    print(" Please enter a password.")
else:
    missing = []
    strength = 0

    if len(password) >= 8:
        strength += 1
    else:
        missing.append("At least 8 characters")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        missing.append("One uppercase letter")

    if re.search("[a-z]", password):
        strength += 1
    else:
        missing.append("One lowercase letter")

    if re.search("[0-9]", password):
        strength += 1
    else:
        missing.append("One number")

    if re.search("[!@#$%^&*]", password):
        strength += 1
    else:
        missing.append("One special character")

    print("\nPassword Strength:")

    if strength <= 2:
        print(" Weak")
    elif strength <= 4:
        print(" Medium")
    else:
        print(" Strong")

    if missing:
        print("\n Password should contain:")
        for item in missing:
            print("•", item)
    else:
        print("\n Such a great password!")