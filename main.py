"""CLI — run: python main.py"""

from getpass import getpass

from password_checker import check_password

password = getpass("Enter password: ")
if not password:
    print("No password entered.")
else:
    r = check_password(password)
    print(f"\nStrength: {r['strength']}")
    print(f"Details : {r['message']}")
    print(f"Length  : {r['length']} | Upper: {r['has_upper']} | Lower: {r['has_lower']} | Digit: {r['has_digit']} | Symbol: {r['has_symbol']}")
