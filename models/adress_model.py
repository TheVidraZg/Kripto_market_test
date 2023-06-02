from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base , relationship, backref
from models.user_model import Base
from models.geo_model import Geo

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(500), nullable=True)
    suite = Column(String(250), nullable=True)
    city = Column(String(250), nullable=False)
    zipcode = Column(String(50), nullable=False)
    
    geo_id = Column(Integer, ForeignKey('geos.id'), nullable=True)
    users = relationship('User', backref=backref('address'))


    def __init__(self,
                 suite: str,
                 street: str,
                 city: str,
                 zipcode: str,
                 geo: Geo):
        self.street: str = street
        self.suite: str = suite
        self.city: str = city
        self.zipcode: str = zipcode
        self.geo: Geo = geo

    @staticmethod
    def from_dict(obj) -> 'Address':
        _street = str(obj.get("street"))
        _suite = str(obj.get("suite"))
        _city = str(obj.get("city"))
        _zipcode = str(obj.get("zipcode"))
        _geo = Geo.from_dict(obj.get("geo"))
        return Address(_street, _suite, _city, _zipcode, _geo)