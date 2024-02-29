#!/usr/bin/env python3
import bcrypt
def hash_password(password: str) -> bytes:
    """Hashes a password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

if __name__ == "__main__":
    has = hash_password("sssaa")
    print(has)
    if bcrypt.checkpw("sssaa".encode("utf-8"), has):
        print(700)
