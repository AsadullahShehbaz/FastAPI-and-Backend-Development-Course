from passlib.context import CryptContext

# Initialize object 
password_context = CryptContext(schemes="bcrypt")

password = "Asadullah AI"

hashed = password_context.hash(password)

print(password_context.verify("Asadullah",hashed))

from secrets import token_hex

print(token_hex())