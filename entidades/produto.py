from sqlalchemy import Column, Integer, String, Date, Sequence, BINARY
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Produto(base):
    __tablename__ = 'produto'
    id = Column(Integer, Sequence('sq_id_produto'),
                primary_key=True, nullable=False)
    descricao = Column(String())
    nome = Column(String())
    cadastro = Column(Date)
    foto = Column(BINARY)

    def tostring(self):
        str_cadastro = ''
        str_foto = ''

        if (self.cadastro):
            str_cadastro = self.cadastro.strftime('%d/%m/%Y')

        if (self.foto):
            str_foto = self.foto.tostring()

        return {'id': self.id, 'nome': self.nome, 'cadastro': str_cadastro, 'foto': str_foto}
