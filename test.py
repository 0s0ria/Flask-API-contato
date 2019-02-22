from app.model.contato import Contato
from app.dao.contato_dao import Contato_Dao

contato_dao = Contato_Dao()
contato_dao.create(contato)
