from fastapi import HTTPException
from typing import List

from schemas.course import CourseSchema, ReviewSchema
from models.course import CourseModel, ReviewModel
from config.db import Session

class CoursesService:
  def __init__(self):
    self.db = Session()
  
  def get_courses(self) -> List[CourseModel]:
    courses = self.db.query(CourseModel).all()
    for course in courses:
      course.reviews
    return courses

  def get_course(self, id: int) -> CourseModel:
    course = self.db.query(CourseModel).filter(CourseModel.id == id).first()
    course.reviews
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
  
  def delete_course(self, id: int) -> bool:
    course = self.get_course(id)
    if not course:
      return False
    self.db.delete(course)
    self.db.commit()
    return True

  def get_reviews_by_course_id(self, course_id: int):
    course = self.get_course(course_id)
    if not course:
      return None
    return course.reviews
  
  def add_review_to_course(self, course_id: int, review: ReviewSchema) -> ReviewModel:
    course = self.get_course(course_id)
    if not course:
      return None
    dump_review = review.model_dump()
    dump_review.update({ "course_id": course_id })
    new_review = ReviewModel(**dump_review)
    self.db.add(new_review)
    self.db.commit()
    self.db.refresh(new_review)
    return new_review
  
  def delete_review(self, course_id, review_id: int) -> bool:
    review = self.db.query(ReviewModel).filter(ReviewModel.id == review_id, ReviewModel.course_id == course_id).first()
    if not review:
      return False
    self.db.delete(review)
    self.db.commit()
    return True

courses_service = CoursesService()
