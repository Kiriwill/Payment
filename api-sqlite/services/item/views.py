from flask import Blueprint, request
from config import db

from utils import response
from schemas.items import ItemSchema
from models.dba import insert_row, delete_row, update_row, query

items = Blueprint('Items', __name__)

@items.route('/item', methods=['POST'])
def insert():
    try:
        data = request.json

        if isinstance(data, list) and len(data):
            for d in data:
                ItemSchema().load(d)
                insert_row('Item', **d)

            return response(True, "200 OK", 200)
        
        ItemSchema().load(data)
        insert_row('Item', **data)
        return response(True, "200 OK", 200)

    except Exception as e:
        return response(True, f"Bad Request. Error: {e}", 400)

@items.route('/item/<id>', methods=['DELETE'])
def delete(id):
    try:
        delete_row('Item', id=id)
        
        return response(True, "200 OK", 200)
    except Exception as e:
        return response(True, f"Internal Error. Error: {e}", 500)

@items.route('/item', methods=['PUT'])
def update():
    try:
        data = request.json
        
        if data.get('id'):
            id = data.pop('id')
            update_row('Item', id=id, **data)
    
            return response(True, "200 OK", 200)
        
        raise Exception('Id é obrigatório para atualização.')
    except Exception as e:
        return response(True, f"Bad Request. Erro: {e}", 400)

@items.route('/item', methods=['GET'])
def filter():
    try:
        data = request.json
        rows = query('Item', **data).all()
        result = ItemSchema(many=True).dump(rows)
        return response(True, "200 OK", 200, result if len(result) else {})

    except Exception as e:
        return response(True, f'{e}', 404, {})
        