import requests
from models import *
def consultar_cliente():
    url = "http://127.0.0.1:5000/clientes"
    response_get_clientes = requests.get(url)
    if response_get_clientes.status_code == 200:
        dados_clientes = response_get_clientes.json()
        print(f"\n id: "
              f"{dados_clientes['id']}")
        print(f"\n nome: {dados_clientes['nome']}")
        print(f"\n cpf: {dados_clientes['cpf']}")
        print(f"\n telefone: {dados_clientes['telefone']}")
        print(f"\n endereco: {dados_clientes['endereco']}")
    else:
        print(f"Erro: {response_get_clientes.status_code}")
def inserir_cliente():
    url = "http://127.0.0.1:5000/criar_cliente"
    novo_cliente = {
        "nome": "",
        "cpf": "",
        "telefone": "",
        "endereco": "", }
    response = requests.post(url, json=novo_cliente)
    if response.status_code == 201:
        novo_cliente = response.json()
        print(f"\n nome: {novo_cliente['nome']}")
        print(f"\n cpf: {novo_cliente['cpf']}")
    else:
        print(f"Erro: {response.status_code}")
def atualizar_cliente(id):
    url = f"http://127.0.0.1:5000/clientes/{id}"
    novo_cliente = {
        "id": id,
        "nome": "",
        "cpf": "",
        "telefone": "",
        "endereco": "",}
    response_antes = requests.get(url)
    response = requests.put(url, json=novo_cliente)
    if response.status_code == 200:
        if response_antes.status_code == 200:
            dados_antes = response_antes.json()
            print(f"\n nome antigo: {dados_antes['nome']}")
            print(f"\n cpf antigo: {dados_antes['cpf']}")
            print(f"\n telefone antigo: {dados_antes['telefone']}")
            print(f"\n endereco antigo: {dados_antes['endereco']}")
        dados_cliente = response.json()
        print(f"\n nome: {dados_cliente['nome']}\n cpf: {dados_cliente['cpf']}"
              f"\n telefone: {dados_cliente['telefone']} \n endereco: {dados_cliente['endereco']}")
    else:
        print(f"Erro: {response.status_code}")
def consultar_veiculo():
    url = "http://127.0.0.1:5000/veiculos"
    response_get_veiculos = requests.get(url)
    if response_get_veiculos.status_code == 200:
        dados_veiculos = response_get_veiculos.json()
        print(f"\n id: {dados_veiculos['id']}")
        print(f"\n marca: {dados_veiculos['marca']}")
        print(f"\n modelo: {dados_veiculos['modelo']}")
        print(f"\n placa: {dados_veiculos['placa']}")
        print(f"\n ano_fabricacao: {dados_veiculos['ano_fabricacao']}")
    else:
        print(f"Erro: {response_get_veiculos.status_code}")
def inserir_veiculo():
    url = "http://127.0.0.1:5000/veiculos"
    novo_veiculo = {
        "marca": "",
        "modelo": "",
        "placa": "",
        "ano_fabricacao": "", }
    response = requests.post(url, json=novo_veiculo)
    if response.status_code == 201:
        novo_veiculo = response.json()
        print(f"\n marca: {novo_veiculo['marca']}")
        print(f"\n modelo: {novo_veiculo['modelo']}")
        print(f"\n placa: {novo_veiculo['placa']}")
        print(f"\n ano_fabricacao: {novo_veiculo['ano_fabricacao']}")
    else:
        print(f"Erro: {response.status_code}")
def atualizar_veiculo(id):
    url = f"http://127.0.0.1:5000/veiculos/{id}"
    novo_veiculo = {
        "id": id,
        "marca": "",
        "modelo": "",
        "placa": "",
        "ano_fabricacao": "",
    }
    response_antes = requests.get(url)
    response = requests.put(url, json=novo_veiculo)

    if response.status_code == 200:
        if response_antes.status_code == 200:
            dados_antes = response_antes.json()
            print(f"\n marca antigo: {dados_antes['marca']}")
            print(f"\n modelo antigo: {dados_antes['modelo']}")
            print(f"\n placa antigo: {dados_antes['placa']}")
            print(f"\n ano de fabricacao antigo: {dados_antes['ano_fabricacao']}")
        dados_cliente = response.json()
        print(f"\n marca: {dados_cliente['marca']}\n modelo: {dados_cliente['modelo']}"
              f"\n placa: {dados_cliente['placa']} \n ano de fabricacao: {dados_cliente['ano_fabricacao']}")
    else:
        print(f"Erro: {response.status_code}")


def consultar_ordem():
    url = "http://127.0.0.1:5000/ordens"
    response_get_ordens = requests.get(url)
    if response_get_ordens.status_code == 200:
        dados_ordens = response_get_ordens.json()
        print(f"\n id: {dados_ordens['id']}")
        print(f"\n marca: {dados_ordens['marca']}")
        print(f"\n modelo: {dados_ordens['modelo']}")
        print(f"\n placa: {dados_ordens['placa']}")
        print(f"\n ano_fabricacao: {dados_ordens['ano_fabricacao']}")
    else:
        print(f"Erro: {response_get_ordens.status_code}")


def inserir_ordem():
    url = "http://127.0.0.1:5000/ordens"

    nova_ordem = {
        "veiculo_id": "",
        "data_abertura": "",
        "descricao_servico": "",
        "status": "",
        "valor_estimado": ""
    }

    response = requests.post(url, json=nova_ordem)

    if response.status_code == 201:
        nova_ordem = response.json()
        print(f"\n veiculo_id: {nova_ordem['veiculo_id']}")
        print(f"\n data_abertura: {nova_ordem['data_abertura']}")
        print(f"\n descricao_servico: {nova_ordem['descricao_servico']}")
        print(f"\n status: {nova_ordem['status']}")
        print(f"\n valor_estimado: {nova_ordem['valor_estimado']}")
    else:
        print(f"Erro: {response.status_code}")

    # exemplo_post()


def atualizar_ordem(id):
    url = f"http://127.0.0.1:5000/ordens/{id}"

    nova_ordem = {
        "id": id,
        "veiculo_id": "",
        "data_abertura": "",
        "descricao_servico": "",
        "status": "",
        "valor_estimado": ""
    }
    response_antes = requests.get(url)
    response = requests.put(url, json=nova_ordem)

    if response.status_code == 200:
        if response_antes.status_code == 200:
            dados_antes = response_antes.json()
            print(f"\n id do veiculo antigo: {dados_antes['veiculo_id']}")
            print(f"\n data da abertura antiga: {dados_antes['data_abertura']}")
            print(f"\n descricao de servico antigo: {dados_antes['descricao_servico']}")
            print(f"\n status: {dados_antes['status']}")
            print(f"\n valor estimado antigo: {dados_antes['valor_estimado']}")
        dados_cliente = response.json()
        print(f"\n id do veiculo: {dados_cliente['veiculo_id']}\n data da abertura: {dados_cliente['data_abertura']}"
              f"\n descricao de servico: {dados_cliente['descricao_servico']} \n status: {dados_cliente['status']} \n "
              f"valor estimado: {dados_cliente['valor_estimado']}")
    else:
        print(f"Erro: {response.status_code}")

