from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base 

from models.adress_model import Address
from models.company_model import Company

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=True)
    website = Column(String(250), nullable=True)

    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=True)



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