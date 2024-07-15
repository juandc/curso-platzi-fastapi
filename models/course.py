# from typing import List, Optional
# from pydantic import BaseModel, Field, PrivateAttr, computed_field
# from uuid import uuid4
from sqlalchemy import Column, Integer, String, Float
from config.db import BaseModelDB

class CourseModel(BaseModelDB):
  __tablename__ = "courses"

  id = Column(Integer, primary_key = True)
  title = Column(String)
  overview = Column(String)
  price = Column(Float)

# class Review(BaseModel):
#   _id: str = PrivateAttr(default_factory = lambda: str(uuid4()))
#   @computed_field
#   @property
#   def id(self) -> str:
#     return self._id

#   rating: int = Field(min=0, max=5)
#   comment: Optional[str] = Field(default=None)

#   def __getitem__(self, item):
#     return getattr(self, item)

# class Course(BaseModel):
#   _id: str = PrivateAttr(default_factory = lambda: str(uuid4()))
#   @computed_field
#   @property
#   def id(self) -> str:
#     return self._id

#   title: str
#   description: str
#   price: float = Field(default=10)
#   review_ids: List[int] = Field(default=[])

#   @computed_field
#   @property
#   def reviews_count(self) -> List[Review]:
#     return len(self.review_ids)

#   model_config = {
#     "json_schema_extra": {
#       "examples": [
#         {
#           "title": "Curso de Ejemplo",
#           "description": "Descripción de ejemplo",
#           "price": 1,
#           "review_ids": []
#         }
#       ]
#     }
#   }

#   def __getitem__(self, item):
#     return getattr(self, item)
