import json
from flask import Response
from app.model.contato import Contato
from app.dao.contato_dao import Contato_Dao
from app.commons.message import MESSAGE
from app.commons.status import STATUS


class Contato_Controller():

    def get_all():
        return (MESSAGE['OK'],STATUS['OK'])

    def get_one():
        pass

    def create(data):
        try:
            print(data)
            contato = Contato()
            contato.name = data['name']
            contato.tell = data['tell']
            contato.email = data['email']
            contato_dao = Contato_Dao()
            contato_dao.create(contato)
            content = {
                'code': 10,
                'user_message':'contato criado com sucesso',
                'internal_message':'novo contato inserido na base'
            }
            return Response(response=json.dumps(content), status=STATUS['OK'], mimetype='application/json')

        except:
            content = {
                'code': 15,
                'user_message':'falha ao criar contato',
                'internal_message':' erro ao inserir na base'

            }
            return Response(response=json.dumps(content), status=STATUS['NOT_FOUND'], mimetype='application/json')

    def update():
        pass

    def delete():
        pas
