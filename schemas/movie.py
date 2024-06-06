from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=15, min_length=5)
    overview: str = Field(default="Mi descripcion", max_length=50, min_length=15)
    year: int = Field(default=2024, le=2025)
    rating: float
    category: str

    class Config:
        schema_extra = {
            "example": {
                "title": "The Godfather",
                "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                "year": "1972",
                "rating": "9.2",
                "category": "Crime"
            }
        }
