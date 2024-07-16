# from typing import List, Optional
# from pydantic import BaseModel, Field, PrivateAttr, computed_field
# from uuid import uuid4
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from config.db import BaseModelDB

class ReviewModel(BaseModelDB):
  __tablename__ = "reviews"

  course_id = Column(Integer, ForeignKey("courses.id"))
  id = Column(Integer, primary_key = True)
  rating = Column(Integer)
  comment = Column(String)

  course = relationship("CourseModel", back_populates="reviews")

class CourseModel(BaseModelDB):
  __tablename__ = "courses"

  id = Column(Integer, primary_key = True)
  title = Column(String)
  overview = Column(String)
  price = Column(Float)

  reviews = relationship("ReviewModel", back_populates="course")
