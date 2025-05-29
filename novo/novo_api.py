import requests

def consultar_cliente():
    url = "http://127.0.0.1:5000/clientes"
    response_get_clientes = requests.get(url)
    if response_get_clientes.status_code == 200:
        dados_clientes = response_get_clientes.json()
        for cliente in dados_clientes:  # Supondo que a resposta seja uma lista de clientes
            print(f"\nID: {cliente['id']}")
            print(f"Nome: {cliente['nome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Endereço: {cliente['endereco']}")
    else:
        print(f"Erro ao consultar clientes: {response_get_clientes.status_code}")

def inserir_cliente(nome, cpf, telefone, endereco):
    url = "http://127.0.0.1:5000/criar_cliente"
    novo_cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco,
    }
    response = requests.post(url, json=novo_cliente)
    if response.status_code == 201:
        cliente_criado = response.json()
        print(f"\nCliente criado com sucesso:")
        print(f"Nome: {cliente_criado['nome']}")
        print(f"CPF: {cliente_criado['cpf']}")
    else:
        print(f"Erro ao inserir cliente: {response.status_code}")

def atualizar_cliente(id, nome, cpf, telefone, endereco):
    url = f"http://127.0.0.1:5000/clientes/{id}"
    novo_cliente = {
        "id": id,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco,
    }
    response_antes = requests.get(url)
    response = requests.put(url, json=novo_cliente)
    if response.status_code == 200:
        if response_antes.status_code == 200:
            dados_antes = response_antes.json()
            print(f"\nDados antigos:")
            print(f"Nome: {dados_antes['nome']}")
            print(f"CPF: {dados_antes['cpf']}")
            print(f"Telefone: {dados_antes['telefone']}")
            print(f"Endereço: {dados_antes['endereco']}")
        dados_cliente = response.json()
        print(f"\nDados atualizados:")
        print(f"Nome: {dados_cliente['nome']}")
        print(f"CPF: {dados_cliente['cpf']}")
        print(f"Telefone: {dados_cliente['telefone']}")
        print(f"Endereço: {dados_cliente['endereco']}")
    else:
        print(f"Erro ao atualizar cliente: {response.status_code}")

def consultar_veiculo():
    url = "http://127.0.0.1:5000/veiculos"
    response_get_veiculos = requests.get(url)
    if response_get_veiculos.status_code == 200:
        dados_veiculos = response_get_veiculos.json()
        for veiculo in dados_veiculos:  # Supondo que a resposta seja uma lista de veículos
            print(f"\nID: {veiculo['id']}")
            print(f"Marca: {veiculo['marca']}")
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Placa: {veiculo['placa']}")
            print(f"Ano de Fabricação: {veiculo['ano_fabricacao']}")
    else:
        print(f"Erro ao consultar veículos: {response_get_veiculos.status_code}")

def inserir_veiculo(marca, modelo, placa, ano_fabricacao):
    url = "http://127.0.0.1:5000/veiculos"
    novo_veiculo = {
        "marca": marca,
        "modelo": modelo,
        "placa": placa,
        "ano_fabricacao": ano_fabricacao,
    }
    response = requests.post(url, json=novo_veiculo)
    if response.status_code == 201:
        veiculo_criado = response.json()
        print(f"\nVeículo criado com sucesso:")
        print(f"Marca: {veiculo_criado['marca']}")
        print(f"Modelo: {veiculo_criado['modelo']}")
        print(f"Placa: {veiculo_criado['placa']}")
        print(f"Ano de Fabricação: {veiculo_criado['ano_fabricacao']}")
    else:
        print(f"Erro ao inserir veículo: {response.status_code}")

def atualizar_veiculo(id, marca, modelo, placa, ano_fabricacao):
    url = f"http://127.0.0.1:5000/veiculos/{id}"
    novo_veiculo = {
        "id": id,
        "marca": marca,
        "modelo": modelo,
        "placa": placa,
        "ano_fabricacao": ano_fabricacao,
    }
    response_antes = requests.get(url)
    response = requests.put(url, json=novo_veiculo)
    if response.status_code == 200:
        if response_antes.status_code == 200:
            dados_antes = response_antes.json()
            print(f"\nDados antigos:")
            print(f"Marca: {dados_antes['marca']}")
            print(f"Modelo: {dados_antes['modelo']}")
            print(f"Placa: {dados_antes['placa']}")
            print(f"Ano de Fabricação: {dados_antes['ano_fabricacao']}")
        dados_cliente = response.json()
        print(f"\nDados atualizados:")
        print(f"Marca: {dados_cliente['marca']}")
        print(f"Modelo: {dados_cliente['modelo']}")
        print(f"Placa: {dados_cliente['placa']}")
        print(f"Ano de Fabricação: {dados_cliente['ano_fabricacao']}")
    else:
        print(f"Erro ao atualizar veículo: {response.status_code}")

def consultar_ordem():
    url = "http://127.0.0.1:5000/ordens"
    response_get_ordens = requests.get(url)
    if response_get_ordens.status_code == 200:
        dados_ordens = response_get_ordens.json()
        for ordem in dados_ordens:  # Supondo que a resposta seja uma lista de ordens
            print(f"\nID: {ordem['id']}")
            print(f"Veículo ID: {ordem['veiculo_id']}")
            print(f"Data de Abertura: {ordem['data_abertura']}")
            print(f"Descrição do Serviço: {ordem['descricao_servico']}")
            print(f"Status: {ordem['status']}")
            print(f"Valor Estimado: {ordem['valor_estimado']}")
    else:
        print(f"Erro ao consultar ordens: {response_get_ordens.status_code}")

def inserir_ordem(veiculo_id, data_abertura, descricao_servico, status, valor_estimado):
    url = "http://127.0.0.1:5000/ordens"
    nova_ordem = {
        "veiculo_id": veiculo_id,
        "data_abertura": data_abertura,
        "descricao_servico": descricao_servico,
        "status": status,
        "valor_estimado": valor_estimado,
    }
    response = requests.post(url, json=nova_ordem)
    if response.status_code == 201:
        ordem_criada = response.json()
        print(f"\nOrdem criada com sucesso:")
        print(f"Veículo ID: {ordem_criada['veiculo_id']}")
        print(f"Data de Abertura: {ordem_criada['data_abertura']}")
        print(f"Descrição do Serviço: {ordem_criada['descricao_servico']}")
        print(f"Status: {ordem_criada['status']}")
        print(f"Valor Estimado: {ordem_criada['valor_estimado']}")
    else:
        print(f"Erro ao inserir ordem: {response.status_code}")

def atualizar_ordem(id, veiculo_id, data_abertura, descricao_servico, status, valor_estimado):
    url = f"http://127.0.0.1:5000/ordens/{id}"
    nova_ordem = {
        "id": id,
        "veiculo_id": veiculo_id,
        "data_abertura": data_abertura,
        "descricao_servico": descricao_servico,
        "status": status,
        "valor_estimado": valor_estimado,
    }
    response_antes = requests.get(url)
    response = requests.put(url, json=nova_ordem)
    if response.status_code == 200:
        if response_antes.status_code == 200:
            dados_antes = response_antes.json()
            print(f"\nDados antigos:")
            print(f"Veículo ID: {dados_antes['veiculo_id']}")
            print(f"Data de Abertura: {dados_antes['data_abertura']}")
            print(f"Descrição do Serviço: {dados_antes['descricao_servico']}")
            print(f"Status: {dados_antes['status']}")
            print(f"Valor Estimado: {dados_antes['valor_estimado']}")
        dados_ordem = response.json()
        print(f"\nDados atualizados:")
        print(f"Veículo ID: {dados_ordem['veiculo_id']}")
        print(f"Data de Abertura: {dados_ordem['data_abertura']}")
        print(f"Descrição do Serviço: {dados_ordem['descricao_servico']}")
        print(f"Status: {dados_ordem['status']}")
        print(f"Valor Estimado: {dados_ordem['valor_estimado']}")
    else:
        print(f"Erro ao atualizar ordem: {response.status_code}")

# Exemplo de uso
# Você pode chamar as funções aqui, passando os parâmetros necessários para testar.
