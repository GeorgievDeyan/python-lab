import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== Secure Password Generator ===")
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        pwd = generate_password(length, use_digits, use_special)
        print(f"\nGenerated password: {pwd}")
    except ValueError as e:
        print(f"Error: {e}")
