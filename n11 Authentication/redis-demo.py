from redis import Redis
from dotenv import load_dotenv
import os 

load_dotenv()

# 1.Connect with Redis DB
db= Redis.from_url(url=os.getenv('REDIS_URL'),decode_responses=True)

# 2.Save Data
db.set('ID','blacklisted')

# 3.Read Data
print(db.exists('22'))
