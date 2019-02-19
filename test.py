from app.model.contato import Contato
from app.dao.contato_dao import Contato_Dao


contato = Contato()
contato.id = 2
contato.name = 'fer'

contato_dao = Contato_Dao(contato)
test = contato_dao.search()
print(test)
