from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship, backref

from repositories.db_repo_init import Base
from infrastructure.constants import (ENTITY_PRECISION,
                                      ENTITY_SCALE)


class Geo(Base):
    __tablename__ = 'geos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float(precision=ENTITY_PRECISION, decimal_return_scale=ENTITY_SCALE), nullable=False)
    lng = Column(Float(precision=ENTITY_PRECISION, decimal_return_scale=ENTITY_SCALE), nullable=False)

    addresses = relationship('Address', backref=backref('geo'))


    def __init__(self, lat: str, lng: str):
        self.lat: str = lat
        self.lng: str = lng

    @staticmethod
    def from_dict(obj) -> 'Geo':
        _lat = str(obj.get("lat"))
        _lng = str(obj.get("lng"))
        return Geo(_lat, _lng)