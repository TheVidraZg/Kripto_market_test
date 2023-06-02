from models.company_model import Company
from repositories.db_repo_init import session



def company_create(company: Company):
    entity = (session.query(Company)
              .filter(Company.name == company.name)
              .one_or_none())
    
    if entity is None:
        entity = company
        session.add(entity)
        session.commit()


def company_get_all() -> list[Company]:
    return (session.query(Company).all())


def company_get(id: int) -> Company:
    return (session.query(Company)
              .filter(Company.id == id)
              .one_or_none())


def company_update(company: Company):
    entity = (session.query(Company)
              .filter(Company.id == company.id)
              .one_or_none())
    
    if entity is not None:
        entity = company
        session.commit()


def company_delete(id: int):
    entity = (session.query(Company)
              .filter(Company.id == id)
              .one_or_none())
    
    if entity is not None:
        session.delete(entity)
        session.commit()


def company_delete(id: int):
    entity = (session.query(Company)
              .filter(Company.id == id)
              .one_or_none())
    
    if entity is not None:
        session.delete(entity)
        session.commit()