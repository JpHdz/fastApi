from fastapi import Path, Query, Depends, APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/', tags=['home'], dependencies=[Depends(JWTBearer())])
def message():
    return HTMLResponse('<h1>Hello world</h1>')
    

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200 , dependencies=[Depends(JWTBearer())])
def movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie , dependencies=[Depends(JWTBearer())])
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=400, content={"message": "Movie not found"})
    return JSONResponse(status_code=400, content=jsonable_encoder(result))

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie] , dependencies=[Depends(JWTBearer())])
def get_movie_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies/', tags=['movies'], response_model=dict, status_code=201 , dependencies=[Depends(JWTBearer())])
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Movie created"})

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200 , dependencies=[Depends(JWTBearer())])
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=400, content={"message": "Movie not found"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Movie updated"})

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200 , dependencies=[Depends(JWTBearer())])
def delete_movie(id: int) -> dict:
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=400, content={"message": "Movie not found"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Movie deleted"})