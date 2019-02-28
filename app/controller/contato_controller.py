import json
from flask import Response
from app.model.contato import Contato
from app.dao.contato_dao import Contato_Dao
from app.commons.message import MESSAGE
from app.commons.status import STATUS


class Contato_Controller():

    def get_all():
        try:
            contato = Contato()
            contato_dao = Contato_Dao()
            data =  contato_dao.read_all()
            content = {
                'message': MESSAGE['GET']['SUCCESS'],
                'data': contato.converter(data)
            }
            return Response(response=json.dumps(content), status=STATUS['OK'], mimetype='application/json')
        except Exception as error:
            print(error)
            content = {
                'message': MESSAGE['GET']['ERROR']
            }
            return Response(response=json.dumps(content), status=STATUS['ERROR'], mimetype='application/json')

    def get_one(id):
        try:
            contato = Contato()
            contato.id = id
            contato_dao = Contato_Dao()
            data = contato_dao.read_one(contato)
            content = {
                'message': MESSAGE['GET']['SUCCESS'],
                'data': contato.converter(data)
            }
            return Response(response=json.dumps(content), status=STATUS['OK'], mimetype='application/json')

        except Exception as error:
            print(error)
            content = {
                'message': MESSAGE['GET']['ERROR']
            }
            return Response(response=json.dumps(content), status=STATUS['ERROR'], mimetype='application/json')
        

    def create(data):
        try:
            contato = Contato()
            contato.parce(data)
            contato_dao = Contato_Dao()
            contato_dao.create(contato)
            content = {
                'message': MESSAGE['CREATE']['SUCCESS']
            }
            return Response(response=json.dumps(content), status=STATUS['CREATE'], mimetype='application/json')

        except Exception as error:
            print(error)
            content = {
                'message': MESSAGE['CREATE']['ERROR']
            }
            return Response(response=json.dumps(content), status=STATUS['ERROR'], mimetype='application/json')

    def update(id,data):
        try:
            contato = Contato()
            contato.id = id
            contato.parce(data)
            contato_dao = Contato_Dao()
            contato_dao.update(contato)
            print('aqui')
            data = contato_dao.read_one(contato)
            print(data)
            content = {
               'message': MESSAGE['UPDATE']['SUCCESS'],
               'data': contato.converter(data)
            }
            return Response(response=json.dumps(content), status=STATUS['OK'], mimetype='application/json')

        except Exception as error:
            print(error)
            content = {
              'message': MESSAGE['UPDATE']['ERROR']
            }
            return Response(response=json.dumps(content), status=STATUS['ERROR'], mimetype='application/json')


    def delete(id):
        try:
            contato = Contato()
            contato.id = id
            contato_dao = Contato_Dao()
            print(contato.id)
            contato_dao.delete(contato)
            content = {
                'message' : MESSAGE['DELETE']['SUCCESS']
            }
            return Response(response=json.dumps(content), status=STATUS['OK'], mimetype='application/json')

        except Exception as error:
            print(error)
            content = {
                'message': MESSAGE['DELETE']['ERROR']
            }
            return Response(response=json.dumps(content), status=STATUS['ERROR'], mimetype='application/json')
        
