import secrets
import string
import bcrypt

ALPHABET = string.ascii_letters + string.digits + '!@#$%&*'

def generate_password(length: int = 16) -> str:
    return ''.join(secrets.choice(ALPHABET) for _ in range(length))

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12)).decode()

def verify_password(password: str, password_hash: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode(), password_hash.encode())
    except (ValueError, TypeError):
        return False