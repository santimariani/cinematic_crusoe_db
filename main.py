import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Session, select, func
from db import get_session

from models.characters import Characters
from models.enemies import Enemies
from models.forts import Forts
from models.items import Items
from models.locations import Locations
from models.pets import Pets
from models.skills import Skills
from models.seasons import Seasons

app = FastAPI()

origins = [
  "http://localhost",
  "http://localhost:3000"
]
app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials =True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get("/")
async def root():
  return {'message': 'Hello Island'}

@app.get("/characters")
def list_characters(session: Session = Depends(get_session)):
  statement = select(Characters)
  results = session.exec(statement).all()
  return results

@app.post("/characters/add")
async def add_character(name: str, session: Session = Depends(get_session)):
    character = Characters(name=name)
    session.add(character)
    session.commit()
    return {"Character Added": character.name}

@app.get('/enemies')
def list_enemies(session: Session = Depends(get_session)):
  statement = select(Enemies)
  results = session.exec(statement).all()
  return results

@app.post("/enemies/add")
async def add_enemy(name: str, session: Session = Depends(get_session)):
    enemy = Enemies(name=name)
    session.add(enemy)
    session.commit()
    return {"Enemy Added": enemy.name}

@app.get('/forts')
def list_forts(session: Session = Depends(get_session)):
  statement = select(Forts)
  results = session.exec(statement).all()
  return results

@app.post("/forts/add")
async def add_fort(name: str, session: Session = Depends(get_session)):
    fort = Forts(name=name)
    session.add(fort)
    session.commit()
    return {"Fort Added": fort.name}

@app.get('/items')
def list_items(session: Session = Depends(get_session)):
  statement = select(Items)
  results = session.exec(statement).all()
  return results

@app.post("/items/add")
async def add_item(name: str, session: Session = Depends(get_session)):
    item = Items(name=name)
    session.add(item)
    session.commit()
    return {"Item Added": item.name}

@app.get('/locations')
def list_locations(session: Session = Depends(get_session)):
  statement = select(Locations)
  results = session.exec(statement).all()
  return results

@app.post("/locations/add")
async def add_location(name: str, session: Session = Depends(get_session)):
    location = Locations(name=name)
    session.add(location)
    session.commit()
    return {"Location Found": location.name}

@app.get('/pets')
def list_students(session: Session = Depends(get_session)):
  statement = select(Pets)
  results = session.exec(statement).all()
  return results

@app.post("/pets/add")
async def add_pet(pet: Pets, session: Session = Depends(get_session)):
    new_pet = Pets(name=pet.name)
    session.add(new_pet)
    session.commit()
    return {"Pet Added": pet.name}

@app.get('/seasons')
def list_students(session: Session = Depends(get_session)):
  statement = select(Seasons)
  results = session.exec(statement).all()
  return results

@app.get('/skills')
def list_students(session: Session = Depends(get_session)):
  statement = select(Skills)
  results = session.exec(statement).all()
  return results

@app.post("/skills/add")
async def add_skill(name: str, session: Session = Depends(get_session)):
    skill = Skills(name=name)
    session.add(skill)
    session.commit()
    return {"Skill Added": skill.name}

if __name__ == '__main__':
  uvicorn.run('main:app', host='localhost', port=8000, reload=True)

# @app.get(“/enrollments”)
# def list_enrollments(session: Session = Depends(get_session)):
#   statement = select(
#     Courses.name.label('course_name'),
#     func.array_agg(Students.name).label('students')
#   ).select_from(
#     Enrollments
#   ).join(
#     Students, Students.id == Enrollments.student_id
#   ).join(
#     Courses, Courses.id == Enrollments.course_id
#   ).group_by(
#     Courses.name
#   )
#   results = session.exec(statement).mappings().all()
#   return results