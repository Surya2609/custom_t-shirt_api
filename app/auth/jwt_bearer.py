from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        if credentials:
            return credentials
        raise HTTPException(status_code=403, detail="Invalid authorization")
