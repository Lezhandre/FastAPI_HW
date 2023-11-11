from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse
from time import time

app = FastAPI()

class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int

dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    return JSONResponse("Welcome to dog service!")

@app.post('/post')
def post():
    return JSONResponse(vars(post_db[-1]))

@app.get('/dog')
def get_dogs(kind: DogType | None = None):
    if kind is None:
        return JSONResponse([vars(dog) for dog in dogs_db.values()])
    return JSONResponse([vars(dog) for dog in dogs_db.values() if dog.kind == kind])

@app.post('/dog')
def create_dog(dog: Dog):
    error_response = { "detail": [] }
    if dog.pk in dogs_db.keys():
        dummy = dict()
        dummy['loc'] = ["body", "pk"]
        dummy['msg'] = "There exists already dog in database with same pk"
        dummy['type'] = "Dog"
        error_response['detail'].append(dummy)
        
        return JSONResponse(error_response, 422)
    
    dogs_db[dog.pk] = dog
    post_db.append(Timestamp(id=dog.pk, timestamp=int(time())))
    
    return JSONResponse(vars(dog))

@app.get('/dog/{pk}')
def get_dog(pk: int):
    error_response = { "detail": [] }
    if not pk in dogs_db.keys():
        dummy = dict()
        dummy['loc'] = ["path", "pk"]
        dummy['msg'] = "There is no dog in database with such pk"
        dummy['type'] = "int"
        error_response['detail'].append(dummy)
        
        return JSONResponse(error_response, 422)
    return JSONResponse(vars(dogs_db[pk]))

@app.patch('/dog/{pk}')
def update_dog(pk: int, new_dog: Dog):
    error_response = { "detail": [] }
    if not pk in dogs_db.keys():
        dummy = dict()
        dummy['loc'] = ["path", "pk"]
        dummy['msg'] = "There is no dog in database with such pk"
        dummy['type'] = "int"
        error_response['detail'].append(dummy)
        
        return JSONResponse(error_response, 422)
    old_dog = dogs_db[pk]
    dogs_db[pk] = new_dog
    return JSONResponse(vars(old_dog))