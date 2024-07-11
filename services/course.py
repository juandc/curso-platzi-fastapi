from typing import List, Optional

from models.course import Course, Review
from data.mock import courses as mock_courses, reviews as mock_reviews

class CourseService:
  def __init__(self, courses = []):
    self.courses = courses

  def get_courses(self) -> List[Course]:
    return self.courses

  def get_course(self, course_id: int) -> Optional[Course]:
    for course in self.courses:
      if course.id == course_id:
        return course
    return None

  def add_course(self, course) -> Course:
    self.courses.append(course)
    return course

  def update_course(self, course_id: int, course) -> Optional[Course]:
    for index, course in enumerate(self.courses):
      if course.id == course_id:
        self.courses.pop(index)
        self.courses.append(course)
        return course
    return None

  def delete_course(self, course_id: int) -> bool:
    for index, course in enumerate(self.courses):
      if course.id == course_id:
        self.courses.pop(index)
        return True
    return False
  
  def get_reviews_by_course_id(self, course_id: int) -> Optional[List[Review]]:
    course = self.get_course(course_id)
    if course is None:
      return None
    course_reviews = []
    for course_review_id in course.review_ids:
      for review in mock_reviews:
        if review.id == course_review_id:
          course_reviews.append(review)
    return course_reviews
  
  def create_review(self, course_id: int, new_review: Review) -> Optional[Review]:
    course = self.get_course(course_id)
    if course is None:
      return None
    mock_reviews.append(new_review)
    course.review_ids.append(new_review.id)
    return new_review
  
  def delete_review(self, course_id: int, review_id: int) -> bool:
    course = self.get_course(course_id)
    if course is None:
      return False
    for index, course_review_id in enumerate(course.review_ids):
      if course_review_id == review_id:
        course.review_ids.pop(index)
        for index, review in enumerate(mock_reviews):
          if review.id == review_id:
            mock_reviews.pop(index)
            return True
    return False

mock_courses_service = CourseService(courses=mock_courses)
