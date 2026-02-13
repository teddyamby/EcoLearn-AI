from app.auth import hash_password, verify_password

def test_password_hashing():
    password = "securepassword"
    hashed = hash_password(password)
    assert verify_password(password, hashed)
