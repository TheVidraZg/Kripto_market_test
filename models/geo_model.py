from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship, backref
from models.user_model import Base


class Geo(Base):
    __tablename__ = 'geos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float(precision=8, decimal_return_scale=6), nullable=False)
    lng = Column(Float(precision=8, decimal_return_scale=6), nullable=False)

    addresses = relationship('Address', backref=backref('geo'))


    def __init__(self, lat: str, lng: str):
        self.lat: str = lat
        self.lng: str = lng

    @staticmethod
    def from_dict(obj) -> 'Geo':
        _lat = str(obj.get("lat"))
        _lng = str(obj.get("lng"))
        return Geo(_lat, _lng)
