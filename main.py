from typing import Union

from fastapi import FastAPI

from db import connect_db

app = FastAPI()
db = connect_db().db
collection = db.hotels


@app.get("/cities")
def get_all_cities():
    cities = collection.distinct('city')
    return cities


@app.get("/countries")
def get_all_countries():
    countries = collection.distinct('country')
    return countries


@app.get("/city/{city}/hotels")
def get_hotels_by_city(city, limit=0):
    hotels = list(collection.find({'city': city}, {'_id': False}).limit(limit))
    return hotels


@app.get("/country/{country}/hotels")
def get_hotels_by_country(country, limit=0):
    hotels = list(collection.find(
        {'country': country}, {'_id': False}).limit(limit))
    return hotels
