"""Password Strength Checker — DecodeLabs Project 1"""

import hmac
from pathlib import Path

_COMMON_FILE = Path(__file__).parent / "data" / "common_passwords.txt"
COMMON_PASSWORDS = (
    frozenset(
        line.strip().lower()
        for line in _COMMON_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    )
    if _COMMON_FILE.exists()
    else frozenset()
)


def check_password(password: str) -> dict:
    """Return strength (Weak/Medium/Strong) and character checks."""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() and not c.isspace() for c in password)

    if length < 8:
        strength, message = "Weak", "Password must be at least 8 characters."
    elif password.lower() in COMMON_PASSWORDS:
        strength, message = "Weak", "This password is commonly leaked."
    elif not (has_upper and has_digit and has_symbol):
        strength, message = "Weak", "Need uppercase, number, and symbol."
    elif length >= 12 and has_lower:
        strength, message = "Strong", "Strong password."
    else:
        strength, message = "Medium", "OK, but use 12+ characters for Strong."

    return {
        "strength": strength,
        "message": message,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
    }


def secure_compare(a: str, b: str) -> bool:
    return hmac.compare_digest(a.encode(), b.encode())
