# Task-Management-API
ALX Capstone Project


## Week 1: Set up Project and User Authentication
*Previoulsy installed Django*
Set up a Django project, *task_manager* 
*Previously installed Django REST Framework (DRF).*
Installed Django bearer tokens and registered in REST Framework settin
Created a Django app for tasks called *tasks*.
Installed app *tasks* in settings.py
Created Task Model
Ran migrations

## Week 2
1. created a token API endpoint
2. Created serializers RegisterSerializer, LoginSerializer, TaskSerializer
3. created authentication api endpoints
    - /api/users/register/
    - /api/users/login/
    - /api/users/logout/

4. created task api endpoints using ModelViewSet
    - /api/tasks/
    - /api/tasks_list/
    - /api/tasks/{id}/
    - /api/tasks/{id}/
    - /api/tasks/{id}/

## Week 3
1. updated Task Serializer to allow task instance to be updated with validated data
2. created task complete view and task complete endpoint
    - /api/tasks/<int:pk>/complete/
3. added backends.py file to ensure that users login using email instead of custom username
4. registerd the emailbackend in settings.py
5. Added filters to Task view using DRF Filter Backend for specific-field based filtering, SearchFilter for text-based searches and OrderingFilter for sorting results. 



# TESTING ENDPOINTS USING CURL (NB: token number would differ)
- *register endpoint*
    curl -X POST http://localhost:8000/api/users/register/ \
    -d "username=abc&email=abc@gmail.com&password=abc123abc"
# expected output:
    {"message":"User registered successfully."}

- *login endpoint*
    curl -X POST http://localhost:8000/api/users/login/ \
    -H "Content-Type: application/json"\
    -d '{"email": "abc@gmail.com", "password": "abc123abc"}'
# expected output:
    {"token":"83cf62f2935add732cfd00dbe399ba81907f77cb","username":"abc","message":"Login successful"}

- *create task*
    curl -X POST http://localhost:8000/api/tasks/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Token 83cf62f2935add732cfd00dbe399ba81907f77cb"
     -d '{"title": "Exercise", "description": "Lose 20 pounds", "due_date": "2025-04-20", "priority_level": "high", "status": "false", "user": "2"}'
# expected output:
    {"id":2,"title":"Exercise","description":"Lose 20 pounds","due_date":"2025-04-20","priority_level":"high","status":false,"user":2}

- *list task*
    curl -X GET http://localhost:8000/api/tasks/ 
    -H "Content-Type: application/json" 
    -H "Authorization: Token 83cf62f2935add732cfd00dbe399ba81907f77cb"
# expect output:
    [{"id":1,"title":"Submit Capstone Project","description":"Complete all API endpoints","due_date":"2025-04-06","priority_level":"high","status":false,"user":1}]

- *update task*
    - for partial update of task1
    curl -X PATCH http://localhost:8000/api/tasks/1/ 
    -H "Content-Type: application/json" 
    -H "Authorization: Token 83cf62f2935add732cfd00dbe399ba81907f77cb"
    -d '{"title": "Submit Captstone Project", "description": "Complete ALX Capstone Project to be considered a junior software engineer"}'
# expected output: 
    [{"id":1,"title":"Submit Captstone Project","description":"Complete ALX Capstone Project to be considered a junior software engineer","due_date":"2025-04-06","priority_level":"high","status":false,"user":1}]

- *logout*
    curl -X POST http://localhost:8000/api/users/logout/ \
    -H "Authorization: Token 83cf62f2935add732cfd00dbe399ba81907f77cb"
# expected output:
    {"message":"Successfully logged out."}

- *filtering*
 for example, BASED ON FIELD due_date
    curl -X GET "http://localhost:8000/api/tasks/?status=False&priority_level=High \
    -H "Authorization: Token 83cf62f2935add732cfd00dbe399ba81907f77cb"

# expected output:
    [
  {
    "id": 1, "title": "Submit Capstone Project", "description": ""Complete ALX Capstone Project to be considered a junior software engineer","due_date": "2025-04-06","priority_level": "high", "status": false,"user": 1}]

