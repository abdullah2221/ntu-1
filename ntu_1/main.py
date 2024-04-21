from fastapi import FastAPI, HTTPException
from ntu_1.schemas import load_db, CarInput, save_db, CarOutput,TripInput,TripOutput
from datetime import datetime, date
app: FastAPI = FastAPI(title="My API")

db = load_db()
userName: str = "ahmad"


@app.get("/")
def get_message(name: str):
    return {"message": f"{name} is my best friend!"}

# @app.get("/cars")
# def getCars():
#     return db


@app.get("/cars")
def get_car(size: str | None = None, doors: int | None = None):
    result = db
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors == doors]
    return result


# @app.get("/cars/{id}")
# def getcar(id: int):
#     for car in db:
#         if car["id"] == id:
#             return car
#     return None
@app.get("/cars/{id}")
def getCar(id: int) -> list[CarOutput]:
    result = [car for car in db if car.id == id]
    if result:
        return result
    else:
        raise HTTPException(
            status_code=404, detail=f"No car found with that id")


@app.post("/cars/")
def AddCar(car: CarInput) -> CarOutput:
    newCar = CarOutput(size=car.size, fuel=car.fuel,
                       transmission=car.transmission, doors=car.doors, id=len(db)+1)

    db.append(newCar)
    save_db(db)
    return newCar


@app.delete("/cars/{id}")
def deleteCar(id: int) -> bool:
    matches= [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        db.remove(car)
        save_db(db)
        return True
    else:
        raise HTTPException(status_code=404,detail=f"that id is not present")
    

@app.put('/cars/{id}')
def updateCar(id:int,newcar:CarInput)->CarOutput:
    matches= [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        car.fuel = newcar.fuel
        car.transmission = newcar.transmission
        car.size= newcar.size
        car.doors = newcar.doors
        save_db(db)
        return car
    else:
        raise HTTPException(status_code=404,detail="that specific id {id} is not present")    
            


@app.post("/cars/{id}/trips")
def add_trips(id:int,trip:TripInput)->TripOutput:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        new_trip = TripOutput(id=len(car.trips)+1,start=trip.start,end=trip.end,description=trip.description)
        car.trips.append(new_trip)
        save_db(db)
        return new_trip
    else:
        raise HTTPException(status_code=404,detail=f"that id is not present")


    