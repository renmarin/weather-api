from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from database import Base


class Cities(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class CitiesSevenDays(Base):
    __tablename__ = "data_for_7_days"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), ForeignKey("cities.name"), nullable=False)
    date = Column(Date())
    temp = Column(Float)
    pcp = Column(Float, default="NaN")
    clouds = Column(Integer)
    pressure = Column(Integer)
    humidity = Column(Integer)
    wind_speed = Column(Float)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": str(self.date),
            "temp": self.temp,
            "pcp": self.pcp,
            "clouds": self.clouds,
            "pressure": self.pressure,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
        }
