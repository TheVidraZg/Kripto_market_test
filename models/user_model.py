from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Geo(Base):
    __tablename__ = 'geos'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float( precision = 8 , decimal_return_scale = 6), nullable=False)
    lng = Column(Float( precision = 8 , decimal_return_scale = 6), nullable=False)
    
    
    def __init__(self, lat: str, lng: str):
        self.lat: str = lat
        self.lng: str = lng

    @staticmethod
    def from_dict(obj) -> 'Geo':
        _lat = str(obj.get("lat"))
        _lng = str(obj.get("lng"))
        return Geo(_lat, _lng)


class Address(Base):
     __tablename__ = 'Adresses'
     id =  Column(Integer, primary_key=True, autoincrement=True)
     street = Column(String(500), nullable=True)
     suite = Column(String(250), nullable=True)
     city = Column(String(250), nullable=False)
     zipcode = Column(String(50), nullable=False)
     geo
    def __init__(self,
                 street: str,
                 suite: str,
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


class Company:
    def __init__(self,
                 name: str,
                 catchPhrase: str,
                 bs: str):
        self.name: str = name
        self.catchPhrase: str = catchPhrase
        self.bs: str = bs

    @staticmethod
    def from_dict(obj) -> 'Company':
        _name = str(obj.get("name"))
        _catchPhrase = str(obj.get("catchPhrase"))
        _bs = str(obj.get("bs"))
        return Company(_name, _catchPhrase, _bs)


class User:
    def __init__(self,
                 id: int,
                 name: str,
                 username: str,
                 email: str,
                 address: Address,
                 phone: str,
                 website: str,
                 company: Company):
        self.id: int = id
        self.name: str = name
        self.username: str = username
        self.email: str = email
        self.phone: str = phone
        self.website: str = website
        self.address: Address = address
        self.company: Company = company


    @staticmethod
    def from_dict(obj) -> 'User':
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        _username = str(obj.get("username"))
        _email = str(obj.get("email"))
        _address = Address.from_dict(obj.get("address"))
        _phone = str(obj.get("phone"))
        _website = str(obj.get("website"))
        _company = Company.from_dict(obj.get("company"))
        return User(_id, _name, _username, _email, _address, _phone, _website, _company)