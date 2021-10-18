from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

city_database = ["Ankara", "İstanbul", "Bursa", "Denizli"]


class CityModel(BaseModel):
    name: str


@app.get("/")
def index() -> List[str]:
    return city_database


@app.get("/cities")
def get_cities() -> List[str]:
    return city_database


@app.get("/cities/{city_id}")
def get_city(city_id: int) -> str:
    if city_id <= len(city_database):
        return city_database[city_id]
    else:
        return "Index out of range"


@app.post("/cities")
def create_city(city: CityModel) -> List[str]:
    if not city in city_database:
        city_database.append(city.name)
    return city_database


@app.put("/cities/{city_id}")
def update_city(city_id: int) -> str:
    city_database[city_id] == "Updated"
    if city_id <= len(city_database):
        return city_database[city_id]
    else:
        return "This city index doesnt exist in the database"


@app.delete("/cities/{city_id}")
def delete_city(city_id: int) -> List[str]:
    if city_database[city_id] != None:
        city_database.pop(city_id)
    return city_database
