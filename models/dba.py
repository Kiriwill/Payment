import logging as logger
from config import db
import schemas

def insert_row(Table:str, **kwargs):
    Table = getattr(schemas, Table)

    row = Table(**kwargs)
    db.session.add(row)
    db.session.commit()

    logger.info(f'{Table} inserido.')

def insert_dp_row(Parent:str, Child:str, **kwargs):
    parent = getattr(schemas, Parent)
    id = kwargs.pop('id_child')

    p = parent(**kwargs)
    c = query(Child, id=id).one()

    p.items.append(c)
    db.session.add(p)
    db.session.commit()

    logger.info(f'Inserido.')

def query(Table:str, **kwargs):
    Table = getattr(schemas, Table)

    row = Table.query.filter_by(**kwargs)
    return row

def delete_row(Table:str, id:int):
    row = query(Table, id=id).one()
    
    db.session.delete(row)
    db.session.commit()

def delete_dp_row(Parent:str, Child:str, **kwargs): #checagem para se tem child=relação
    id_parent = kwargs.pop('id_parent')

    p = query(Parent, id=id_parent).one()

    db.session.delete(p)
    db.session.commit()

    logger.info(f'Deletado.')

def update_row(Table:str, id:int, **kwargs):
    row = query(Table, id=id).one()
    for k,v in kwargs.items():
        setattr(row, k, v)
    
    db.session.commit()