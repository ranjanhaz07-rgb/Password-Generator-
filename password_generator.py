import string
import secrets


def generate_password(
    length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True
):
  # Build the character pool based on user choices
  char_pool = ""
  if use_upper:
    char_pool += string.ascii_uppercase
  if use_lower:
    char_pool += string.ascii_lowercase
  if use_digits:
    char_pool += string.digits
  if use_symbols:
    char_pool += string.punctuation

  if not char_pool:
    raise ValueError("At least one character set must be selected!")

  # Ensure length is reasonable
  if length < 6:
    print("⚠️ Warning: Passwords shorter than 6 characters are not secure.")

  # Generate a secure password using the secrets module
  while True:
    password = "".join(secrets.choice(char_pool) for _ in range(length))

    # Optional sanity checks to ensure at least one of each chosen type is present
    if (
        (not use_upper or any(c.isupper() for c in password))
        and (not use_lower or any(c.islower() for c in password))
        and (not use_digits or any(c.isdigit() for c in password))
        and (not use_symbols or any(c in string.punctuation for c in password))
    ):
      return password


if __name__ == "__main__":
  print("🔐 Secure Password Generator")

  try:
    length = int(input("Enter password length (default 16): ") or 16)
  except ValueError:
    length = 16

  pwd = generate_password(length=length)
  print(f"\nYour generated password is:\n👉 {pwd}")
