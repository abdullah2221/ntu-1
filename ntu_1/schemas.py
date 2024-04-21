from pydantic import BaseModel
import json

class TripInput(BaseModel):
    start:int
    end:int
    description:str
class TripOutput(TripInput):
    id:int    

class CarInput(BaseModel):
    fuel:str| None = "electric"
    size:str
    doors:int
    transmission:str | None="auto"

    
class CarOutput(CarInput):
    id:int
    trips:list[TripInput]=[]
    
def load_db()->list[CarOutput]:
    with open("cars.json") as f:
        return [CarOutput.model_validate(obj) for obj in json.load(f)]    
    
    
def save_db(cars:list[CarOutput]):
    with open("cars.json","w") as f:
        json.dump([car.model_dump() for car in cars],f,indent=4)    