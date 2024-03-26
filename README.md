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

---

# Final Notes

Unfortunately, I wasn't able to finish this on time. The backend is set up and layered properly although it still needs some cleaning. The frontend has the base setup for data display, though not all data is properly connected. Unfortunately, this can be tested but not deployed for production.

Just to iterate things I would like to implement but have not been able to yet:

BACKEND
- Authentication using jwt and oauth2 was started but not completed.
- I was supposed to make separate files for the model "User", so that admin and employee privileges can be built on top of it. But for now, "user" routes and actions are under employee files
- API endpoints fully functional and can be tested, although it would do better with more validation and error handling
- lots of cleanup

FRONTEND
- I'll admit I got caught up trying to make the frontend well-structured as someone who has higher standards for myself when it comes to frontend. But I also underestimated the time it would take to piece things together And troubleshoot with the backend. There was a lot I wanted to do that I couldn't do on time. Though the base for a possibly functional frontend is there, it isn't fully functional.
- Routes aren't layered with authentication checking yet
- Many services don't have a frontend counterpart yet
- Must register an admin user manually (send request to /register endpoint)

GENERAL
- Would very much like to add Lint/Pylint to help with cleanup
- Naming conventions can be more organized
- Unit tests must be in place before deploying to production
- Primary improvement/tech debt to focus on would be properly calling and displaying data

As much as I hate to submit an incomplete product, I am incredibly grateful for the opportunity to challenge myself and work on this. I've learned a lot about my way of getting tasks done and some patterns I still need to fix. This also gave me the chance to boost my confidence when it comes to backend development. I think I would like to finish this fully in my own time soon.