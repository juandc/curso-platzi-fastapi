from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from data.mock import *

app = FastAPI()
app.title = "Perrito Movies para la Tropa Alpinito"

@app.get("/", tags=["root"])
def root():
  return {
    "movies": movies
  }

@app.get("/html", tags=["root"])
def html():
  return HTMLResponse(content="<h1>Esto es un mensaje en HTML</h1>")


class Movie(BaseModel):
  id: int
  title: str
  overview: str
  year: str
  rating: float
  category: str

@app.get('/movies', tags=["movies"])
def get_all_movies():
  return {
    "movies": movies
  }

@app.get('/movies/', tags=["movies"])
def get_movies_by_category(category: str):
  movies_with_category = []
  for movie in movies:
    if movie["category"] == category:
      movies_with_category.append(movie)
  if len(movies_with_category) > 0:
    return {
      "movies": movies_with_category
    }
  raise HTTPException(status_code=404, detail="No movies with category " + category)

@app.get('/movies/{id}', tags=["movies"])
def get_movie_by_id(id: int):
  for movie in movies:
    if movie["id"] == id:
      return movie
  raise HTTPException(status_code=404, detail="Movie not found")

@app.post('/movies', tags=["movies"])
def create_movie(new_movie: Movie):
  for movie in movies:
    if movie["id"] == new_movie.id:
      raise HTTPException(status_code=409, detail="Movie already exists")
  movies.append(new_movie.model_dump())
  return {
    "movie": new_movie
  }

@app.put('/movies', tags=["movies"])
def update_movie(updated_movie: Movie):
  for index, movie in enumerate(movies):
    if movie["id"] == updated_movie.id:
      movies.pop(index)
      movies.append(updated_movie.model_dump())
      return {
        "movie": updated_movie
      }
  raise HTTPException(status_code=404, detail="Movie not found")

@app.delete('/movies', tags=["movies"])
def update_movie(id: int):
  for index, movie in enumerate(movies):
    if movie["id"] == id:
      movies.pop(index)
      return {
        "success": True
      }
  raise HTTPException(status_code=404, detail="Movie not found")
