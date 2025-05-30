from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv
import os  # criar variavel de ambiente '.env'
import configparser  # criar arquivo de configuração 'config.ini'

# configurar banco vercel
# ler variavel de ambiente
load_dotenv()
# Carregue as configurações do banco de dados
url_ = os.environ.get("DATABASE_URL")
print(f"modo1:{url_}")

# Carregue o arquivo de configuração
config = configparser.ConfigParser()
config.read('config.ini')
# Obtenha as configurações do banco de dados
database_url = config['database1']['url']
print(f"mode2:{database_url}")

engine = create_engine('sqlite:///database.db')


local_session = sessionmaker(bind=engine)

Base = declarative_base()
#Base.query = db_session.query_property()


class Cliente_Principal(Base):
    __tablename__ = 'Cliente'
    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False, index=True)
    telefone = Column(String(11), nullable=False, index=True, unique=True)
    endereco = Column(String(40), nullable=False, index=True)
    cpf = Column(String(11), nullable=False, index=True, unique=True)


    def __repr__(self):
        return '<Funcionario: Nome: {} CPF: {} Endereco: {} Telefone: {} >'.format(self.nome, self.cpf, self.endereco, self.telefone )

    def save(self,db_session):
        db_session.add(self)
        db_session.commit()

    def delete(self, db_session):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_funcionario = {
            'id': self.id_cliente,
            'nome': self.nome,
            'telefone': self.telefone,
            'endereco': self.endereco,
            'cpf': self.cpf,

        }

        return dados_funcionario


class Veiculos_Principal(Base):
    __tablename__ = 'Veiculos_Principal'
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer,ForeignKey(Cliente_Principal.id_cliente))
    marca = Column(String(40), nullable=False, index=True)
    modelo = Column(String(40), nullable=False, index=True)
    placa = Column(String(40), nullable=False, index=True)
    ano_de_fabricacao = Column(Integer, nullable=False, index=True)

    def __repr__(self,):
        return '<Veiculos_Principal: {} {} {} {} {} >'.format(self.marca, self.modelo, self.placa, self.ano_de_fabricacao, self.id_cliente)

    def save(self,db_session):
        db_session.add(self)
        db_session.commit()

    def delete(self, db_session):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_Veiculos_Principal = {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'marca': self.marca,
            'modelo': self.modelo,
            'placa': self.placa,
            'ano_de_fabricacao': self.ano_de_fabricacao,
        }
        return dados_Veiculos_Principal

class Servicos_Principal(Base):
    __tablename__ = 'Servicos_Principal'
    id_servicos = Column(Integer, primary_key=True)
    Veiculos_Principal_associados = Column(String(40), nullable=False, index=True)
    descricao_de_servico= Column(String(40), nullable=False, index=True)
    data_de_abertura = Column(String(10), nullable=False, index=True, autoincrement=True)
    status = Column(String(10), nullable=False)
    valor_total = Column(Float, nullable=False, index=True)

    def __repr__(self):
        return '<Servicos_Principal:  {} {} {} {} {} {}>'.format(self.id_servicos, self.Veiculos_Principal_associados, self.descricao_de_servico, self.data_de_abertura, self.status, self.valor_total)

    def save(self,db_session):
        db_session.add(self)
        db_session.commit()

    def delete(self, db_session):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_movimentacao = {

            'id_servicos': self.id_servicos,
            'Veiculos_Principal_associados': self.Veiculos_Principal_associados,
            'descricao_de_servico':self.descricao_de_servico,
            'status': self.status,
            'data_de_abertura': self.data_de_abertura,
            'valor_total': self.valor_total,

        }

        return dados_movimentacao


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()