from datetime import datetime,timezone,timedelta
from uuid import uuid4

from fastapi import HTTPException
from app.config import security_settings as st 

import jwt

def generate_access_token(data : dict,expiry: timedelta = timedelta(days=1)):
    return jwt.encode(
            payload={
                **data,
                 "jti":str(uuid4()),
                "exp": datetime.now(timezone.utc)+ expiry
            },
            algorithm=st.JWT_ALGORITHM,
            key=st.JWT_SECRET
        )

def decode_access_token(token: str) -> dict:

    try:
        return jwt.decode(
                    jwt=token,
                    algorithms=[st.JWT_ALGORITHM],
                    key=st.JWT_SECRET
                )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Expired Token"
        )

    
    except jwt.PyJWTError:
        return None