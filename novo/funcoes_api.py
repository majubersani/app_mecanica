import requests
import json

URL_BASE = "http://127.0.0.1:5000"

def cadastro_usuario_app(nome, cpf, senha, telefone, endereco, papel='usuario'):
    """
    Cadastra um novo usuário para acesso ao sistema (pode ser 'admin' ou 'usuario').
    Este endpoint é para criar usuários que utilizarão o app.
    """
    dados = {
        "nome": nome,
        "cpf": cpf,
        "senha": senha,
        "telefone": telefone,
        "endereco": endereco,
        "papel": papel
    }
    try:
        resposta = requests.post(f"{URL_BASE}/cadastro", json=dados)
        if resposta.status_code == 201:
            return {"success": True, "message": resposta.json().get("msg", "Usuário cadastrado com sucesso!")}
        else:
            error_msg = resposta.json().get("msg", "Erro desconhecido ao cadastrar usuário.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao cadastrar usuário: {e}"}


def post_cliente(nome, cpf, telefone, endereco):
    """
    Cadastra um novo cliente no sistema.
    """
    dados = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco
    }
    try:
        resposta = requests.post(f"{URL_BASE}/cadastro_clientes", json=dados)
        if resposta.status_code == 201:
            return {"success": True, "data": resposta.json()}
        else:
            error_msg = resposta.json().get("erro", "Erro ao cadastrar cliente.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao cadastrar cliente: {e}"}

def get_clientes():
    """
    Obtém a lista de todos os clientes cadastrados.
    """
    try:
        resposta = requests.get(f"{URL_BASE}/lista_clientes")
        if resposta.status_code == 200:
            return {"success": True, "data": resposta.json().get("lista", [])}
        else:
            error_msg = resposta.json().get("error", "Erro ao obter clientes.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao obter clientes: {e}"}

def atualizar_cliente(id_cliente, nome, cpf, telefone, endereco):
    """
    Atualiza os dados de um cliente existente.
    """
    dados = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco
    }
    try:
        resposta = requests.put(f"{URL_BASE}/atualizar_clientes/{id_cliente}", json=dados)
        if resposta.status_code == 200:
            return {"success": True, "message": resposta.json().get("mensagem", "Cliente atualizado com sucesso!")}
        else:
            error_msg = resposta.json().get("error", "Erro ao atualizar cliente.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao atualizar cliente: {e}"}

# --- Funções de Veículos ---
def post_veiculo(marca, modelo, placa, ano_de_fabricacao, id_cliente):
    """
    Cadastra um novo veículo, associando-o a um cliente existente.
    """
    dados = {
        "marca": marca,
        "modelo": modelo,
        "placa": placa,
        "ano_de_fabricacao": ano_de_fabricacao,
        "id_cliente": id_cliente
    }
    try:
        resposta = requests.post(f"{URL_BASE}/cadastro_veiculo", json=dados)
        if resposta.status_code == 201:
            return {"success": True, "data": resposta.json()}
        else:
            error_msg = resposta.json().get("erro", "Erro ao cadastrar veículo.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao cadastrar veículo: {e}"}

def get_veiculos():
    """
    Obtém a lista de todos os veículos cadastrados.
    """
    try:
        resposta = requests.get(f"{URL_BASE}/lista_veiculos")
        if resposta.status_code == 200:
            return {"success": True, "data": resposta.json().get("lista", [])}
        else:
            error_msg = resposta.json().get("error", "Erro ao obter veículos.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao obter veículos: {e}"}

def atualizar_veiculo(id_veiculo, marca, modelo, placa, ano_de_fabricacao):
    """
    Atualiza os dados de um veículo existente.
    """
    dados = {
        "marca": marca,
        "modelo": modelo,
        "placa": placa,
        "ano_de_fabricacao": ano_de_fabricacao
    }
    try:
        resposta = requests.put(f"{URL_BASE}/atualizar_veiculos/{id_veiculo}", json=dados)
        if resposta.status_code == 200:
            return {"success": True, "message": "Veículo atualizado com sucesso!", "data": resposta.json()}
        else:
            error_msg = resposta.json().get("error", "Erro ao atualizar veículo.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao atualizar veículo: {e}"}

# --- Funções de Ordens de Serviço ---
def post_ordem_servico(veiculos_associados, descricao_de_servico, data_de_abertura, status, valor_total):
    """
    Cadastra uma nova ordem de serviço.
    'veiculos_associados' deve ser a placa do veículo, conforme o modelo da API.
    A API parece esperar 'id_servicos' no payload para POST, o que é incomum para um ID auto-gerado.
    Considerando que `id_servicos` é uma PK, não deveria ser enviado no POST.
    Caso a API exija, adicione um 'id_servicos' gerado ou recebido como parâmetro.
    Por enquanto, omiti no payload de criação.
    """
    dados = {
        "veiculos_associados": veiculos_associados,
        "descricao_de_servico": descricao_de_servico,
        "data_de_abertura": data_de_abertura,
        "status": status,
        "valor_total": valor_total,
        # 'id_servicos' não incluído, pois é geralmente auto-gerado pelo banco de dados.
        # Se a API exige, descomente e forneça um valor.
        # "id_servicos": id_servicos,
    }
    try:
        resposta = requests.post(f"{URL_BASE}/ordens_de_servicos", json=dados)
        if resposta.status_code == 201:
            return {"success": True, "data": resposta.json()}
        else:
            error_msg = resposta.json().get("erro", "Erro ao cadastrar ordem de serviço.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao cadastrar ordem de serviço: {e}"}

def get_ordens_servico():
    """
    Obtém a lista de todas as ordens de serviço.
    """
    try:
        resposta = requests.get(f"{URL_BASE}/lista_servicos")
        if resposta.status_code == 200:
            return {"success": True, "data": resposta.json().get("lista", [])}
        else:
            error_msg = resposta.json().get("error", "Erro ao obter ordens de serviço.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao obter ordens de serviço: {e}"}

def atualizar_ordem_servico(id_servicos, veiculos_associados, descricao_de_servico, data_de_abertura, status, valor_total):
    """
    Atualiza os dados de uma ordem de serviço existente.
    """
    dados = {
        "veiculos_associados": veiculos_associados,
        "descricao_de_servico": descricao_de_servico,
        "data_de_abertura": data_de_abertura,
        "status": status,
        "valor_total": valor_total
    }
    try:
        resposta = requests.put(f"{URL_BASE}/atualizar_Ordens/{id_servicos}", json=dados)
        if resposta.status_code == 200:
            return {"success": True, "message": "Ordem de serviço atualizada com sucesso!", "data": resposta.json()}
        else:
            error_msg = resposta.json().get("error", "Erro ao atualizar ordem de serviço.")
            return {"success": False, "message": error_msg}
    except requests.exceptions.ConnectionError:
        return {"success": False, "message": "Erro de conexão com a API. Verifique se a API está rodando."}
    except json.JSONDecodeError:
        return {"success": False, "message": "Resposta inválida da API (não é JSON)."}
    except Exception as e:
        return {"success": False, "message": f"Erro inesperado ao atualizar ordem de serviço: {e}"}
