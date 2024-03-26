# SPROUT SOLUTIONS FULL STACK TECHNICAL EXAM
Niña Gabrielle (Ninielle) Pascual
* This is a "crud" app intended for viewing and managing users (employees) made with FastAPI, Postgre, and Vue.js
* This app is containerized in Docker

## Build Docker Image
**To build:**
`$ docker-compose up -d --build`

**To initialize db config**
`$ docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM`

`$ docker-compose exec backend aerich init-db`

**To access the services, you may open:**
* `http://localhost:5001` - to access backend services
* `http://localhost:5001/docs` - to access api documentation with swagger
* `http://localhost:8080` - to access frontend

**When making changes to data models, update database with:**

1. `$ docker-compose exec backend aerich migrate`
2. `$ docker-compose exec backend aerich upgrade`

---

### *This app is intended to bee run through docker, but to test the services individualy...*

## Build Backend Service
1. `$ pip install --upgrade pip` ensure pip is up to date
2. `$ pip install -r requirements.txt` install python dependencies
3. `$ uvicorn src.main:app --reload --host 0.0.0.0 --port 5001` run backend on `http://localhost:5001`

## Build Frontend Service
1. `$ npm install` to install node dependencies
2. `$ npm run serve` to run frontend on `http://localhost:8080`
