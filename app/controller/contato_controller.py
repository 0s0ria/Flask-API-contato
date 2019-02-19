from app import app
from flask import request, abort
import json
from app.model.contato import Contato
from app.dao.contato_dao import Contato_Dao


@app.route("/contato", methods=['GET'])
def get_contatos():

    return 'não autorizado',401


@app.route('/contato', methods=['POST'])
def create_contato():
    data = request.get_json()

    pass

@app.route('/contato/<id>', methods=['PUT'])
def update_contato(id):
    return id

@app.route('/contato', methods=['DELETE'])
def delete_contato():
    pass
