from fastapi import HTTPException
from typing import List

from schemas.course import CourseSchema
from models.course import CourseModel
from config.db import Session
# from data.mock import courses as mock_courses, reviews as mock_reviews

class CoursesService:
  def __init__(self):
    self.db = Session()
  
  def get_courses(self) -> List[CourseModel]:
    courses = self.db.query(CourseModel).all()
    return courses

  def get_course(self, id: int) -> CourseModel:
    course = self.db.query(CourseModel).filter(CourseModel.id == id).first()
    return course
  
  def add_course(self, course: CourseSchema) -> CourseModel:
    new_course = CourseModel(**course.model_dump())
    print(course)
    print(new_course)
    print(new_course.__dict__)
    self.db.add(new_course)
    self.db.commit()
    self.db.refresh(new_course)
    return new_course
  
  def partial_update_course(self, id: int, updated_course: dict) -> CourseModel:
    course = self.get_course(id)
    if not course:
      return None
    course_keys = course.__dict__.keys()
    for key, value in updated_course.items():
      if key == "id":
        continue
      if not key in course_keys:
        print(f"Key {key} not found in course keys")
        raise HTTPException(status_code=400, detail=f"Key {key} not found in course keys")
      setattr(course, key, value)
    print(course.__dict__)
    self.db.commit()
    self.db.refresh(course)
    return course
  
  def update_course(self, id: int, updated_course: CourseSchema) -> CourseModel:
    course = self.get_course(id)
    if not course:
      return None
    for key, value in updated_course.__dict__.items():
      if not key == "id":
        setattr(course, key, value)
    self.db.commit()
    self.db.refresh(course)
    return course

courses_service = CoursesService()
