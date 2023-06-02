from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  relationship, backref
from models.user_model import Base



class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    catchPhrase = Column(String(500), nullable=True)
    bs = Column(String(500), nullable=True)

    users = relationship('User', backref=backref('company'))


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