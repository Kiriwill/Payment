from flask import Blueprint, request
from config import db

from utils import response
from schemas.payments import Payment, PaymentSchema
from models.dba import insert_dp_row, delete_dp_row, update_row, query

payment = Blueprint('Payments', __name__)

@payment.route('/payment', methods=['POST'])
def insert():
    ''' Insere dados na tabela de pagamentos '''

    data = request.json

    if isinstance(data, dict) and not data.get('id_item'):
        return response(True, "id_item é obrigatório", 400)
    
    if isinstance(data, list) and len(data):
        for d in data:
            if not d.get('id_item'):
                return response(True, "id_item é obrigatório", 400)

            d.update(id_child=d.pop('id_item'))
            insert_dp_row('Payment', 'Item', **d)

        return response(True, "200 OK", 200)
    
    data.update(id_child=data.pop('id_item'))
    insert_dp_row('Payment', 'Item', **data)

    return response(True, "200 OK", 200)
    
@payment.route('/payment', methods=['DELETE'])
def delete():
    ''' Deleta dados da tabela de pagamentos '''

    data = request.json

    if not data.get('id_payment'):
        return response(True, "id_payment obrigatório", 400)

    data.update(id_parent=data.pop('id_payment'))
    delete_dp_row('Payment', 'Item', **data) 

    return response(True, "200 OK", 200)

@payment.route('/payment', methods=['PUT'])
def update():
    ''' Atualiza dados da tabela de pagamentos '''
    data = request.json

    if not data.get('id_payment'):
        return response(True, "id_payment e id_items são obrigatórios", 400)

    id = data.pop('id_payment')
    update_row('Item', id=id, **data)

    return response(True, "200 OK", 200)


@payment.route('/payment', methods=['GET'])
def filter():
    ''' Recupera dados da tabela de pagamentos '''
    data = request.json

    if data.get('id'):
        rows = query('Payment', **data).all()
        result = PaymentSchema(many=True).dump(rows)

        return response(True, "200 OK", 200, result)
