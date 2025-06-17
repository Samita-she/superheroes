# 🦸‍♀️ Flask Superheroes API

A RESTful API built using Flask and SQLAlchemy to manage superheroes, their powers, and the strength of those powers.

> **Owner:** Sheila Samita


## 📌 Description

This API allows you to:
- View all superheroes and their powers
- Update the description of a specific power
- Assign a power to a hero with a defined strength level

Ideal for use in projects that need basic CRUD operations and many-to-many relationships.



## 🌟 Features

- View all heroes and their details
- Assign powers to heroes with strengths
- Update powers with validation (description ≥ 20 characters)
- Strong error handling and input validation
- Preloaded seed data for quick testing



## 🛠️ Setup Instructions

### 1. Clone the project
git clone <your-repo-url>
cd flask-superheroes

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Seed the database
python seed.py

5. Run the server
python run.py
Server will run on http://127.0.0.1:5000

📮 API Endpoints
Heroes
Method	Endpoint	Description
GET	/heroes	List all heroes
GET	/heroes/<id>	Get a hero and their powers

Powers
Method	Endpoint	Description
GET	/powers	List all powers
GET	/powers/<id>	Get details of a specific power
PATCH	/powers/<id>	Update power description (≥ 20 chars)

Hero Powers
Method	Endpoint	Description
POST	/hero_powers	Assign a power to a hero with strength

🌱 Seeding the Database
To reset the database with demo data:
python seed.py
This drops all existing tables and populates fresh data including:

10 superheroes

4 superpowers

🧪 Postman Collection
To test endpoints easily:

Open Postman

Click Import

Select the file: challenge-2-superheroes.postman_collection.json

Run requests like:

GET /heroes

POST /hero_powers

📫 Contact
Owner: Sheila Samita
📧 Email: samitasheila1@gmail.com

🧾 License
This project is licensed under the MIT License.See the [LICENSE](./LICENSE) file for details.
