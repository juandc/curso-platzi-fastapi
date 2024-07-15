from fastapi import FastAPI, HTTPException

# from models.course import Course, Review
from config.db import BaseModelDB, engine
from schemas.course import CourseSchema
from services.course import courses_service

app = FastAPI(
  title = "Platzito: Platzi versión Alpinito",
  version = "0.0.2",
)

BaseModelDB.metadata.create_all(bind=engine)

@app.get('/courses', tags=["courses"])
def get_all_courses():
  courses = courses_service.get_courses()
  if len(courses) > 0:
    return {
      "courses": courses,
    }
  raise HTTPException(status_code=404, detail="No courses created yet")

@app.get('/courses/{id}', tags=["courses"])
def get_course_by_id(id: str):
  course = courses_service.get_course(id)
  if course:
    return {
      "course": course,
    }
  raise HTTPException(status_code=404, detail="Course not found")

@app.post('/courses', tags=["courses"])
def create_course(course: CourseSchema):
  new_course = courses_service.add_course(course)
  return {
    "course": new_course,
  }

@app.patch('/courses/{id}', tags=["courses"])
def partial_update_course(id: str, updated_course: dict):
  course = courses_service.partial_update_course(id, updated_course)
  if course:
    return {
      "course": course,
    }
  raise HTTPException(status_code=404, detail="Course not found")

@app.put('/courses/{id}', tags=["courses"])
def update_course(id: str, updated_course: CourseSchema):
  course = courses_service.update_course(id, updated_course)
  if course:
    return {
      "course": course,
    }
  raise HTTPException(status_code=404, detail="Course not found")

# @app.delete('/courses', tags=["courses"])
# def delete_course(id: str):
#   if courses_service.delete_course(id):
#     return {
#       "success": True
#     }
#   raise HTTPException(status_code=404, detail="Course not found")

# @app.get('/courses/{course_id}/reviews', tags=["reviews"])
# def get_reviews_by_course_id(course_id: str):
#   course_reviews = courses_service.get_reviews_by_course_id(course_id)
#   if len(course_reviews) > 0:
#     return {
#       "reviews": course_reviews
#     }
#   raise HTTPException(status_code=404, detail="No reviews found for course " + course_id)

# @app.post('/courses/{course_id}/reviews', tags=["reviews"])
# def create_review(course_id: str, new_review: Review):
#   course_review = courses_service.create_review(course_id, new_review)
#   if course_review:
#     return {
#       "review": course_review
#     }
#   raise HTTPException(status_code=404, detail="Course not found")

# @app.delete('/courses/{course_id}/reviews/{review_id}', tags=["reviews"])
# def delete_review(course_id: str, review_id: str):
#   if courses_service.delete_review(course_id, review_id):
#     return {
#       "success": True
#     }
#   raise HTTPException(status_code=404, detail="Course or review not found")
