import requests
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Cities, CitiesSevenDays, Base

from database import init_db

init_db()

engine = create_engine("sqlite:///weather_seven_days.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

requests_dct = {
    "Kyiv": "https://api.openweathermap.org/data/2.5/onecall?lat=50.450001&lon=30.523333&exclude=current,minutely,hourly,alerts&units=metric&appid=936c1d2029414a688f233b6f1d895e82",
    "Uzhhorod": "https://api.openweathermap.org/data/2.5/onecall?lat=48.621025&lon=22.288229&exclude=current,minutely,hourly,alerts&units=metric&appid=936c1d2029414a688f233b6f1d895e82",
    "Kharkiv": "https://api.openweathermap.org/data/2.5/onecall?lat=49.988358&lon=36.232845&exclude=current,minutely,hourly,alerts&units=metric&appid=936c1d2029414a688f233b6f1d895e82",
    "Odesa": "https://api.openweathermap.org/data/2.5/onecall?lat=46.482952&lon=30.712481&exclude=current,minutely,hourly,alerts&units=metric&appid=936c1d2029414a688f233b6f1d895e82",
    "Chernihiv": "https://api.openweathermap.org/data/2.5/onecall?lat=51.50551&lon=31.28487&exclude=current,minutely,hourly,alerts&units=metric&appid=936c1d2029414a688f233b6f1d895e82",
}

# Data for Cities
for key, value in requests_dct.items():
    city = Cities(name=key)
    session.add(city)
    session.commit()

    response = requests.get(value)
    data = response.json()
    days = [day for day in data["daily"]]

    for value in days:
        day = CitiesSevenDays(
            date=datetime.datetime.fromtimestamp(value.get("dt")),
            name=city.name,
            temp=value["temp"]["day"],
            pcp=value.get("rain"),
            clouds=value.get("clouds"),
            pressure=value.get("pressure"),
            humidity=value.get("humidity"),
            wind_speed=value.get("wind_speed"),
        )
        session.add(day)
        session.commit()
