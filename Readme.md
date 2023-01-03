# FLASK API IN POSTGRESQL   
- link -> https://betterprogramming.pub/crud-api-with-flask-and-postgresql-15548d9ee48e
## Steps:
- Create and activate a virtual environment named .venv:

           
            py -3 -m venv .venv
            .venv\scripts\activate
- Update pip in the virtual environment:


            python -m pip install --upgrade pip
- Install Flask in the virtual environment:

            python -m pip install flask
- Install required libraries from the requirements file:

            pip install -r requirements.txt
- Create a new file in your project folder named app.py
- Runs the Flask development server(i.e. app.py):

            flask run

# Postgresql
- Download Postgresql DB latest version, install copy the password while installing.
- Copy "C:\Program Files\PostgreSQL\14\lib" and "C:\Program Files\PostgreSQL\14\bin" and paste them in environment variables path to enable psql command line.
- login in command in terminal(i.e. in any directory level i.e. "C:\Users\Wainaina") :

       psql -U postgres
- Password:

      1234
- Check/View all available databases

      postgres=# \l
- Create Database command:

      CREATE DATABASE martin;
- View all rows in db:

      postgres=# \du
- Create database:

      CREATE DATABASE pets;
- Create role:

            CREATE ROLE martin WITH LOGIN PASSWORD ‘1234’;
Grant database access to the user you created above:

            GRANT ALL PRIVILEGES ON DATABASE pets TO martin;

# API 
1. POST -> Create a new pet
- endpoint -> http://127.0.0.1:5000/pets
- body :

            {
                "pet_name": "Winnie",
                "pet_type": "Cat",
                "pet_age": 2,
                "pet_description": "My pet"
            }
- response:

            {
                "pet": {
                    "pet_age": 2,
                    "pet_description": "My pet",
                    "pet_name": "Winnie",
                    "pet_type": "Cat"
                },
                "response": "Pet added successfully",
                "success": true
            }

2. GET -> Retrieve all pets
- endpoint -> http://127.0.0.1:5000/get-pets
- response :

            {
                "pets": [
                    {
                        "pet_age": 22,
                        "pet_description": "1",
                        "pet_id": 1,
                        "pet_name": "Kelly",
                        "pet_type": "Cat"
                    },
                    {
                        "pet_age": 2,
                        "pet_description": "My pet",
                        "pet_id": 2,
                        "pet_name": "Winnie",
                        "pet_type": "Cat"
                    }
                ],
                "success": true,
                "total_pets": 2
            }

3. PATCH -> Update pet
- endpoint -> http://127.0.0.1:5000/pets/1
- body :

            {
                "pet_name": "Winnie 2",
                "pet_type": "Cat 3",
                "pet_age": 3,
                "pet_description": "My pet 1"
            }
- response:

            {
                "pet": {
                    "pet_age": 3,
                    "pet_description": "My pet 1",
                    "pet_name": "Winnie 2",
                    "pet_type": "Cat 3"
                },
                "response": "Pet Details updated",
                "success": true
            }

4. DELET - delete pet
- endpoint -> http://127.0.0.1:5000/pets/1
response -> 

            {
                "response": "Pet deleted successfully",
                "success": true
            }