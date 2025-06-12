from venv import create

from colorama.ansi import clear_line
from flask import Flask, render_template, request, jsonify
from sqlalchemy import select
from sqlalchemy.util import non_memoized_property
from models import Cliente,  Veiculos, Ordens_de_servicos, local_session

app = Flask(__name__)

app.config['SECRET_KEY'] = '<KEY>'


@app.route('/cadastro_clientes', methods=['POST'])
def cadastro_cliente():
    db_session = local_session()
    try:

        dados = request.get_json()
        if not dados['nome'] or not dados['cpf'] or not dados['telefone'] or not dados['endereco']:
            return jsonify({'error': 'Preencha todos os campos'})
        else:
            print(dados)
            sql = select(Cliente).where(Cliente.telefone == dados['telefone'])
            telefone_existe = db_session.execute(sql).scalar()
            print(telefone_existe)

            sql = select(Cliente).where(Cliente.cpf == dados['cpf'])
            cpf_existe = db_session.execute(sql).scalar()
            print(cpf_existe)

            if telefone_existe:
                return jsonify({
                    "erro": "esse telefone ja existe!"
                }), 400

            if cpf_existe:
                return jsonify({

                    "erro": "esse cpf já existe!"
                }), 400

            form_novo_cliente = Cliente(
                nome=dados['nome'],
                cpf=dados['cpf'],
                endereco=dados['endereco'],
                telefone=dados['telefone'],
            )
            form_novo_cliente.save(db_session)

            return jsonify({
                'nome': dados['nome'],
                'cpf': dados['cpf'],
                'telefone': dados['telefone'],
                'endereco': dados['endereco'],
            }),201
    except ValueError:
        return jsonify({'Error': 'Não foi possível cadastrar'})
    finally:
        db_session.close()




# não pode ser acessado
@app.route('/lista_clientes', methods=["GET"])
def lista_clientes():
    db_session = local_session()
    sql_lista = select(Cliente)
    lista_resultado = db_session.execute(sql_lista).scalars().all()
    resultado_lista = []
    for n in lista_resultado:
        resultado_lista.append(n.serialize_user())

    return jsonify({'lista': resultado_lista})


# não pode ser acessado
@app.route('/atualizar_clientes/<int:id_cliente>', methods=["PUT"])
def atualizar_clientes(id_cliente):
    db_session = local_session()
    try:
        dados = request.get_json()
        print(dados)
        cliente = db_session.execute(select(Cliente).where(Cliente.id_cliente == id_cliente)).scalar()
        print(Cliente)
        print("xxxxx")
        if not dados['nome'] or not dados['cpf'] or not dados['telefone'] or not dados['endereco']:
            return jsonify({'error': 'Preencha todos os campos'}),400
        else:
            cliente.nome = dados["nome"]
            cliente.cpf = dados["cpf"]
            cliente.telefone = dados["telefone"]
            cliente.endereco = dados["endereco"]


            return jsonify({
                "mensagem": 'Cliente atualizado com sucesso!',
            }),200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        db_session.close()

# não pode ser acessado
@app.route('/cadastro_veiculo', methods=['POST'])
def cadastro_veiculo():
    db_session = local_session()
    try:

        dados = request.get_json()
        if not dados['marca'] or not dados['modelo'] or not dados['placa'] or not dados['ano_de_fabricacao'] or not \
        dados['id_cliente']:
            return jsonify({'error': 'Preencha todos os campos'})
        else:
            print(dados)
            sql = select(Veiculos).where(Veiculos.id_cliente == dados['id_cliente'])
            id_cliente_existe= db_session.execute(sql).scalar()
            print(id_cliente_existe)

            sql = select(Veiculos).where(Veiculos.placa == dados['placa'])
            placa_existe = db_session.execute(sql).scalar()
            print(placa_existe)

            if id_cliente_existe:
                return jsonify({
                    "erro":"esse cliente ja contem um veiculo!"
                }),400

            if placa_existe:

                return jsonify({
                    "erro":"esse placa ja contem um veiculo!"
                }),400

            form_novo_veiculo = Veiculos(
                marca=dados['marca'],
                modelo=dados['modelo'],
                placa=dados['placa'],
                ano_de_fabricacao=dados['ano_de_fabricacao'],
            )
            form_novo_veiculo.save(db_session)

            return jsonify({
                'id_cliente': dados['id_cliente'],
                'marca': dados['marca'],
                'modelo': dados['modelo'],
                'placa': dados['placa'],
                'ano_de_fabricacao': dados['ano_de_fabricacao'],
            }),201
    except ValueError:
        return jsonify({'Error': 'Não foi possível cadastrar'})
    finally:
        db_session.close()




@app.route('/lista_veiculos', methods=["GET"])
def lista_veiculos():
    db_session = local_session()
    sql_lista_veiculo = select(Veiculos)
    lista_veiculos_resultado = db_session.execute(sql_lista_veiculo).scalars().all()
    resultado_lista_veiculo = []
    for n in lista_veiculos_resultado:
        resultado_lista_veiculo.append(n.serialize_user())
    return jsonify({'lista': resultado_lista_veiculo})


# não pode ser acessado
@app.route('/atualizar_veiculos/<id>', methods=["PUT"])
def atualizar_veiculos(id):
    db_session = local_session()
    try:
        dados = request.get_json()
        veiculo = db_session.execute(select(Veiculos).where(Veiculos.id == id)).scalar()
        print(veiculo)
        print(dados)
        if not dados["marca"] or not dados["modelo"] or not dados["placa"] or not dados["ano_de_fabricacao"]:
            return jsonify({'error':"preencha todos os campos"}),400
        else:
            veiculo.marca = dados["marca"]
            veiculo.modelo = dados["modelo"]
            veiculo.placa = dados["placa"]
            veiculo.ano_de_fabriacao = dados["ano_de_fabricacao"]

            return jsonify({
                'marca': dados["marca"],
                'modelo': dados["modelo"],
                'placa': dados["placa"],
                'ano_de_fabriacao': dados["ano_de_fabricacao"],
            }),200
    except Exception as e:
        return jsonify({'error': str(e)}),400
    finally:
        db_session.close()




# não pode ser acessado
@app.route('/ordens_de_servicos', methods=['POST'])
def ordens_servicos():
    db_session = local_session()
    try:
        dados = request.get_json()
        if (not dados['veiculos_associados'] or not dados['descricao_de_servico'] or not dados['data_de_abertura']
                or not dados['status'] or not dados['valor_total']):
            return jsonify({"error": 'Preencher todos os campos'})
        else:
            print(dados)
            # sql=select(Ordens_de_servicos).where(Ordens_de_servicos.id_servicos == dados["id_servicos"])
            # id_servicos_existe= db_session.execute(sql).scalar()
            # print(id_servicos_existe)

            sql = select(Ordens_de_servicos).where(Ordens_de_servicos.veiculos_associados == dados['veiculos_associados'])
            veiculos_associados_existe = db_session.execute(sql).scalar()
            print(veiculos_associados_existe)

            # if id_servicos_existe:
            #     return jsonify({
            #
            #         "erro":'esse id servicos ja contem um veiculo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           '
            #     }),400

            if veiculos_associados_existe:
                return jsonify({
                    "erro":"esse veiculo ja contem um veiculo"
                }),400

            form_nova_ordem = Ordens_de_servicos(

                veiculos_associados=dados['veiculos_associados'],
                descricao_de_servico=dados['descricao_de_servico'],
                data_de_abertura=dados['data_de_abertura'],
                status=dados['status'],
                valor_total=dados['valor_total'],
                id_servicos=dados['id_servicos'],


            )
            form_nova_ordem.save(db_session)

            return jsonify({

                'veiculos_associados': dados['veiculos_associados'],
                'descricao': dados['descricao_de_servico'],
                'data_de_abertura': dados['data_de_abertura'],
                'status': dados['status'],
                'valor_total': dados['valor_total'],


            }),201
    except ValueError:
        return jsonify({'error':'não foi possivel acessar as Ordens de Servicos'})
    finally:
        db_session.close()



# não pode ser acessado
@app.route('/lista_servicos', methods=["GET"])
def lista_servicos():
    sql_lista_servicos = select(Ordens_de_servicos)
    lista_servicos_resultado = local_session.execute(sql_lista_servicos).scalars().all()
    resultado_lista_servicos = []
    for n in lista_servicos_resultado:
        resultado_lista_servicos.append(n.serialize_user())
    return jsonify({'lista': resultado_lista_servicos})

@app.route('/atualizar_Ordens/<id_servicos>', methods=["PUT"])
def atualizar_ordens(id_servicos):
    db_session = local_session()
    try:
        dados = request.get_json()
        Ordens_associados = db_session.execute(select(Ordens_de_servicos).where(Ordens_de_servicos.id_servicos == id_servicos)).scalar()
        print(Ordens_associados)
        print(dados)
        if not dados['veiculos_associados']or not dados['descricao_de_servico'] or not dados['data_de_abertura']or not dados['status'] or not dados['valor_total']:
            return jsonify({'error':"preencha todos os campos"}),401


        else:
            Ordens_associados.veiculos_associados = dados['veiculos_associados']
            Ordens_associados.descricao = dados['descricao_de_servico']
            Ordens_associados.data = dados['data_de_abertura']
            Ordens_associados.status = dados['status']
            Ordens_associados.valor_total = dados['valor_total']


            return jsonify({
               'veiculos_associados': dados['veiculos_associados'],
                'descricao': dados['descricao_de_servico'],
                'data_de_abertura': dados['data_de_abertura'],
                'status': dados['status'],
                'valor_total': dados['valor_total'],
            }),200
    except Exception as e:
        return jsonify({'error': str(e)}),400
    finally:
        db_session.close()






if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
# não pode ser acessado
