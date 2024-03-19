import secrets

a = secrets.token_bytes(1)
b = secrets.token_bytes(1)

while (not secrets.compare_digest(a,b)):
    a = secrets.token_bytes(1)
    b = secrets.token_bytes(1)
    print(f"{a} {b} / {secrets.compare_digest(a,b)}")