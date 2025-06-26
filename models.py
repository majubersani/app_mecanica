from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv
import os  # criar variavel de ambiente '.env'
import configparser  # criar arquivo de configuração 'config.ini'


load_dotenv()
url_ = os.environ.get("DATABASE_URL")
print(f"modo1:{url_}")


config = configparser.ConfigParser()
config.read('config.ini')

engine = create_engine('sqlite:///database.db') # conectar local alterado/substituído


local_session = sessionmaker(bind=engine)

Base = declarative_base()
#Base.query = db_session.query_property()


class Cliente(Base):
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False, index=True)
    telefone = Column(String(11), nullable=False, unique=True, index=True)
    endereco = Column(String(40), nullable=False, index=True)
    cpf = Column(String(11), nullable=False, unique=True, index=True)

    def __repr__(self):
        return f'<Cliente: Nome={self.nome}, CPF={self.cpf}, Endereco={self.endereco}, Telefone={self.telefone}>'

    def save(self, db_session):
        db_session.add(self)
        db_session.commit()

    def delete(self, db_session):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        return {
            'id': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'endereco': self.endereco,
            'cpf': self.cpf,
        }

class Veiculos(Base):
    __tablename__ = 'veiculos'

    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey(Cliente.id_cliente))
    marca = Column(String(40), nullable=False, index=True)
    modelo = Column(String(40), nullable=False, index=True)
    placa = Column(String(40), nullable=False, unique=True, index=True)
    ano_de_fabricacao = Column(Integer, nullable=False, index=True)

    def __repr__(self):
        return f'<Veiculo: Marca={self.marca}, Modelo={self.modelo}, Placa={self.placa}, Ano={self.ano_de_fabricacao}, ClienteID={self.id_cliente}>'

    def save(self, db_session):
        db_session.add(self)
        db_session.commit()

    def delete(self, db_session):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        return {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'marca': self.marca,
            'modelo': self.modelo,
            'placa': self.placa,
            'ano_de_fabricacao': self.ano_de_fabricacao,
        }

class Ordens_de_servicos(Base):
    __tablename__ = 'ordens_de_servicos'

    id_servicos = Column(Integer, primary_key=True)
    veiculos_associados = Column(String(40), nullable=False, index=True)
    descricao_de_servico = Column(String(100), nullable=False, index=True)
    data_de_abertura = Column(String(10), nullable=False, index=True)
    status = Column(String(20), nullable=False)
    valor_total = Column(Float, nullable=False, index=True)

    def __repr__(self):
        return (f'<OrdemServico: ID={self.id_servicos}, '
                f'Veiculo={self.veiculos_associados},'
                f' Descricao={self.descricao_de_servico}, '
                f'Data={self.data_de_abertura}, '
                f'Status={self.status},'
                f' Valor={self.valor_total}>')

    def save(self, db_session):
        db_session.add(self)
        db_session.commit()

    def delete(self, db_session):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        return {
            'id_servicos': self.id_servicos,
            'veiculos_associados': self.veiculos_associados,
            'descricao_de_servico': self.descricao_de_servico,
            'data_de_abertura': self.data_de_abertura,
            'status': self.status,
            'valor_total': self.valor_total,
        }

def init_db():
    Base.metadata.create_all(bind=engine)

# Executa a criação das tabelas se o arquivo for rodado diretamente
if __name__ == '__main__':
    init_db()