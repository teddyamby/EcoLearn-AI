def test_password_hash():
    from app.auth import hash_password, verify_password
    pwd = "secret"
    hashed = hash_password(pwd)
    assert verify_password(pwd, hashed)
