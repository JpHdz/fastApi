from utils.jwt_manager import validate_token
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request



class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        email = data.get('email')  # Obtenemos el valor de 'email' o None si no existe
        if email != 'admin@gmail.com':
            raise HTTPException(status_code=403, detail='Las credenciales son inválidas')