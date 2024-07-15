from pydantic import BaseModel, Field
from typing import Optional

class CourseSchema(BaseModel):
  id: Optional[int] = None
  title: str
  overview: str
  price: float = Field(default=10)
  # review_ids: List[int] = Field(default=[])

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
