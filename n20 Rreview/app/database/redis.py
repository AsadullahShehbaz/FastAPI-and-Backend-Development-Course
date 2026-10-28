from redis.asyncio import Redis
from app.config import db_settings

_db = Redis.from_url(url=db_settings.REDIS_URL,decode_responses=True)

# Add jwt id in the database and blacklist it
async def add_jti_to_blacklist(jti: str):
    await _db.set(jti,"blacklisted")

# Verify jwt id from blacklisted ids in database
async def is_jti_blacklisted(jti: str)->bool:
    return await _db.exists(jti) 

