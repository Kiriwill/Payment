from flask import jsonify

def response(sucesso, msg, codigo, data = None):
    """Retorna um :class:`~flask.Flask.response_class`"""
    if data != None:
        return jsonify({
            'sucesso': sucesso,
            'data': data,
            'message': msg
        }), codigo
    else:
        return jsonify({
            'sucesso': sucesso,
            'message': msg
        }), codigo