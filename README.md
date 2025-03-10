# Courier_management_systam

# Courier Service API (Django REST Framework)

## 🚀 Features
- RESTful API with CRUD operations.
- JWT Authentication.
- Soft Delete Implementation (No hard deletion).
- Status Tracking for Packages.

## Live API(Render)

```python
https://courier-management-backend-1.onrender.com/
```

All API Endpoints:
```python
https://courier-management-backend-1.onrender.com/register/ (for Registration)
https://courier-management-backend-1.onrender.com/token/    (for Login)
https://courier-management-backend-1.onrender.com/packages/  (for get or create packages.create needs authentication)
https://courier-management-backend-1.onrender.com/packages/<id>/ (delete or update)
```



## 🔧 Installation
1. Clone the repo:
```python
git clone https://github.com/NitayDas/Courier_management_backend.git
```

2. Create virtual env and activate (Optiontal):

```python
python -m venv venv
```
```python
cd venv/Scripts
```
```python
.\actiavte
```
```python
cd ..
```
```python
cd ..
```


3. Install dependencies:
   
```python
pip install -r requirements.txt
```


4. Run migrations:
   
```python
python manage.py makemigrations
python manage.py migrate
```


5. Start server:
   
```python
python manage.py runserver
```

## API Documentation

Base URL

```python
http://127.0.0.1:8000/
```

🔐 Authentication
Obtain Token (Login)

```python
POST /token/
```

Description: Authenticate user and get access & refresh tokens.

```python
curl -X POST http://127.0.0.1:8000/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

Register New User

```python
POST /register/
```

Description: Create a new user account.

```python
curl -X POST http://127.0.0.1:8000/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "new_user", "email": "user@example.com", "password": "secure_password"}'
```

📦 Packages API
Get All Packages

```python
GET /packages/
```

Description: Retrieve a list of all packages.

```python
curl -X GET http://127.0.0.1:8000/packages/ \
     -H "Authorization: Bearer your_access_token"
```

Get a Package by ID

```python
GET /packages/<package_id>/
```

Description: Retrieve details of a specific package.

```python
curl -X GET http://127.0.0.1:8000/packages/1/ \
     -H "Authorization: Bearer your_access_token"
```

Create a New Package

```python
POST /packages/
```

Description: Add a new package to the system.

```python
curl -X POST http://127.0.0.1:8000/packages/ \
     -H "Authorization: Bearer your_access_token" \
     -H "Content-Type: application/json" \
     -d '{"name": "Package A", "weight": 2.5, "destination": "New York"}'
```

Update a Package

```python
PUT /packages/<package_id>/
```

Description: Update package details (e.g., delivery status).

```python
curl -X PUT http://127.0.0.1:8000/packages/1/ \
     -H "Authorization: Bearer your_access_token" \
     -H "Content-Type: application/json" \
     -d '{"status": "Delivered"}'
```

Delete a Package

```python
DELETE /packages/<package_id>/
```

Description: Remove a package from the system.

```python
curl -X DELETE http://127.0.0.1:8000/packages/1/ \
     -H "Authorization: Bearer your_access_token"
```

