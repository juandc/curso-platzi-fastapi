from pydantic import BaseModel, Field
from typing import Optional, List

class ReviewSchema(BaseModel):
  id: Optional[int] = None
  rating: int = Field(min=0, max=5)
  comment: Optional[str] = Field(default=None)

  course_id: Optional[int] = None

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "rating": 5,
          "comment": "Excelente curso",
        }
      ]
    }
  }

class CourseSchema(BaseModel):
  id: Optional[int] = None
  title: str
  overview: str
  price: float = Field(default=10)
  reviews: List[ReviewSchema] = Field(default=[])

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "title": "Curso de Ejemplo",
          "overview": "Descripción de ejemplo",
          "price": 1,
        }
      ]
    }
  }
