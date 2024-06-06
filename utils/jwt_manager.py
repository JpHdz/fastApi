#Created on Sat May 04 2024 at 2:21:59 by Kevin Jonathan Tavera Perez

#File: jwt_manager.py

#Copyright (c) 2024 company

from jwt import encode, decode

def create_token(data: dict):
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data : dict = decode(token, key="my_secret_key", algorithms=["HS256"])
    return data

