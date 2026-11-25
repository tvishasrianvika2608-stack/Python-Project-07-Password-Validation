
n = int(input("Enter number of passwords: "))

for i in range(n):
    password = input("\nEnter password: ")

    errors = []

    if len(password) < 8:
        errors.append("Password must contain at least 8 characters.")

    if not any(ch.isupper() for ch in password):
        errors.append("Password must contain an uppercase letter.")

    if not any(ch.islower() for ch in password):
        errors.append("Password must contain a lowercase letter.")

    if not any(ch.isdigit() for ch in password):
        errors.append("Password must contain a number.")

    if not any(not ch.isalnum() for ch in password):
        errors.append("Password must contain a special character.")

    if "123" in password:
        errors.append("Password must not contain 123.")

    if errors:
        print("Invalid Password:")
        for error in errors:
            print("-", error)
    else:
        print("Valid Password!")

print("\nPassword checking completed.")
