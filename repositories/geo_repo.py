from sqlalchemy import and_

from models.geo_model import Geo
from repositories.db_repo_init import session



def geo_create(geo: Geo):
    entity = (session.query(Geo)
              .filter(and_(
                    Geo.lat == geo.lat,
                    Geo.lng == geo.lng
                ))
              .one_or_none())
    
    if entity is None:
        entity = geo
        session.add(entity)
        session.commit()


def geo_get_all() -> list[Geo]:
    return (session.query(Geo).all())


def geo_get(id: int) -> Geo:
    return (session.query(Geo)
              .filter(Geo.id == id)
              .one_or_none())


def geo_update(geo: Geo):
    entity = (session.query(Geo)
              .filter(Geo.id == geo.id)
              .one_or_none())
    
    if entity is not None:
        entity = geo
        session.commit()



def geo_delete(id: int):
    entity = (session.query(Geo)
              .filter(Geo.id == id)
              .one_or_none())
    
    if entity is not None:
        session.delete(entity)
        session.commit()