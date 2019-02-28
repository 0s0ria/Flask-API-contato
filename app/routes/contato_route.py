from app import app
from flask import request
import json
from app.controller.contato_controller import Contato_Controller



@app.route("/contato", methods=['GET'])
def get_contatos():
    response = Contato_Controller.get_all()
    return response

@app.route("/contato/<id>", methods=['GET'])
def get_contato(id):
    response = Contato_Controller.get_one(id)
    return response


@app.route('/contato', methods=['POST'])
def create_contato():
    data = request.get_json()
    response = Contato_Controller.create(data)
    return response


@app.route('/contato/<id>', methods=['PUT'])
def update_contato(id):
    data = request.get_json()
    response = Contato_Controller.update(id,data)
    return  response

@app.route('/contato/<id>', methods=['DELETE'])
def delete_contato(id):
    response = Contato_Controller.delete(id)
    return response
