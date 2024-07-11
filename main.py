from fastapi import FastAPI, HTTPException

from models.course import Course, Review
from services.course import mock_courses_service

app = FastAPI(
  title = "Platzito: Platzi versión Alpinito",
  version = "0.0.2",
)

@app.get('/courses', tags=["courses"])
def get_all_courses():
  courses = mock_courses_service.get_courses()
  if len(courses) > 0:
    return {
      "courses": courses
    }
  raise HTTPException(status_code=404, detail="No courses created yet")

@app.get('/courses/{id}', tags=["courses"])
def get_course_by_id(id: str):
  course = mock_courses_service.get_course(id)
  if course:
    return {
      "course": course
    }
  raise HTTPException(status_code=404, detail="Course not found")

@app.post('/courses', tags=["courses"])
def create_course(new_course: Course):
  mock_courses_service.add_course(new_course)
  return {
    "course": new_course
  }

@app.put('/courses/{id}', tags=["courses"])
def update_course(id: str, updated_course: Course):
  course = mock_courses_service.update_course(id, updated_course)
  if course:
    return {
      "course": course
    }
  raise HTTPException(status_code=404, detail="Course not found")

@app.delete('/courses', tags=["courses"])
def delete_course(id: str):
  if mock_courses_service.delete_course(id):
    return {
      "success": True
    }
  raise HTTPException(status_code=404, detail="Course not found")

@app.get('/courses/{id}/reviews', tags=["reviews"])
def get_reviews_by_course_id(id: str):
  course_reviews = mock_courses_service.get_reviews_by_course_id(id)
  if len(course_reviews) > 0:
    return {
      "reviews": course_reviews
    }
  raise HTTPException(status_code=404, detail="No reviews found for course " + id)

@app.post('/courses/{id}/reviews', tags=["reviews"])
def create_review(id: str, new_review: Review):
  course_review = mock_courses_service.create_review(id, new_review)
  if course_review:
    return {
      "review": course_review
    }
  raise HTTPException(status_code=404, detail="Course not found")

@app.delete('/courses/{course_id}/reviews/{review_id}', tags=["reviews"])
def delete_review(course_id: str, review_id: str):
  if mock_courses_service.delete_review(course_id, review_id):
    return {
      "success": True
    }
  raise HTTPException(status_code=404, detail="Course or review not found")
