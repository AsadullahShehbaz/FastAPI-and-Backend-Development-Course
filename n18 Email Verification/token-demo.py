from datetime import timedelta
import time
from app.utils import generate_url_safe_token,decode_url_safe_token

token = generate_url_safe_token({
    "id":"2212"
})
print(token)

time.sleep(2)
# user = decode_url_safe_token(token + "x")
user = decode_url_safe_token(token,expiry=timedelta(seconds=1))
print(user)
