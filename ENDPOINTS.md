# School API Endpoints

## Student 
### GET student_grades 
Relative path: /student
Returns a list of all their homework submissions, filter by name, grade

### POST create_gradeable 
Relative path: /upload
Create submission with uploaded file for homework 

## Teacher
### GET gradeables 
Relative path: /teacher
Returns a list of all homework submissions, filter by name, date range, and student

### POST grade
Update gradeable homework with a grade and notes.