import requests

def consultar_cliente():
    url = f"http://127.0.0.1:5000/{id}"
    response_get = requests.get(url)
    if response_get.status_code == 200:
        dados_get_postagem = response_get.json()
        print(f"\n titulo: {dados_get_postagem['title']}")
        print(f"\n conteudo: {dados_get_postagem['body']}")
    else:
        print(f"Erro: {response_get.status_code}")

def inserir_cliente():
    url = "https://jsonplaceholder.typicode.com/posts"
    novo_cliente = {
        "title": "Novo titulo",
        "body": "Nova postagem",
        "userId": 2
    }

    response = requests.post(url, json=nova_postagem)

    if response.status_code == 201:
        dados_post = response.json()
        print(f"\n titulo: {dados_post['title']}")
        print(f"\n conteudo: {dados_post['body']}")
    else:
        print(f"Erro: {response.status_code}")

def exemplo_put(id):
    url =  f"https://jsonplaceholder.typicode.com/posts/{id}"
    nova_postagem = {
        "id": id,
        "title": "Novo titulo",
        "body": "Nova postagem",
        "userId": 1
    }
    response_antes = requests.get(url)
    response = requests.put(url, json=nova_postagem)

    if response.status_code == 200:
        if response_antes.status_code == 200:
            dados_antes = response_antes.json()
            print(f"\n titulo antigo: {dados_antes['title']}")
        dados_post = response.json()
        print(f"\n titulo: {dados_post['title']}")
        print(f"\n conteudo: {dados_post['body']}")
    else:
        print(f"Erro: {response.status_code}")