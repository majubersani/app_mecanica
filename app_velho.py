import flet as ft
from flet import AppBar, Text, View, Column
from flet.core.colors import Colors


def main(page: ft.Page):
    # Configuração da página
    page.title = "Cadastro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 375
    page.window_height = 667
    page.bgcolor = Colors.RED_ACCENT_100

    # Listas para armazenar os dados
    clientes = []
    veiculos = []
    ordens = []

    # Funções de navegação
    def cadastrar_cliente(e):
        page.go("/cliente")

    def cadastrar_veiculo(e):
        page.go("/veiculo")

    def cadastrar_ordem(e):
        page.go("/ordem")

    def ver_clientes(e):
        page.go("/cadastrados/clientes")

    def ver_veiculos(e):
        page.go("/cadastrados/veiculos")

    def ver_ordens(e):
        page.go("/cadastrados/ordens")

    # Função para salvar cliente
    def salvar_cliente(e):
        if not input_nome.value or not input_cpf.value or not input_telefone.value or not input_endereco.value:
            page.show_snack_bar(mensagem_erro)
            return

        cliente = {
            "nome": input_nome.value,
            "cpf": input_cpf.value,
            "telefone": input_telefone.value,
            "endereco": input_endereco.value
        }
        clientes.append(cliente)  # Adiciona cliente à lista
        limpar_campos_cliente()
        page.show_snack_bar(mensagem_sucesso)
        ver_clientes(e)  # Redireciona para a tela de ver clientes
        page.update()

    # Função para salvar veículo
    def salvar_veiculo(e):
        if not input_marca.value or not input_modelo.value or not input_placa.value or not input_ano_fabricacao.value:
            page.show_snack_bar(mensagem_erro)
            return

        veiculo = {
            "marca": input_marca.value,
            "modelo": input_modelo.value,
            "placa": input_placa.value,
            "ano_fabricacao": input_ano_fabricacao.value
        }
        veiculos.append(veiculo)  # Adiciona veículo à lista
        limpar_campos_veiculo()
        page.show_snack_bar(mensagem_sucesso)
        ver_veiculos(e)  # Redireciona para a tela de ver veículos
        page.update()

    # Função para salvar ordem de serviço
    def salvar_ordem(e):
        if not input_data_abertura.value or not input_descricao_servico.value or not input_status.value or not input_valor_estimado.value:
            page.show_snack_bar(mensagem_erro)
            return

        ordem = {
            "data_abertura": input_data_abertura.value,
            "descricao_servico": input_descricao_servico.value,
            "status": input_status.value,
            "valor_estimado": input_valor_estimado.value
        }
        ordens.append(ordem)  # Adiciona ordem à lista
        limpar_campos_ordem()
        page.show_snack_bar(mensagem_sucesso)
        ver_ordens(e)  # Redireciona para a tela de ver ordens
        page.update()

    # Funções para limpar campos
    def limpar_campos_cliente():
        for campo in [input_nome, input_cpf, input_telefone, input_endereco]:
            campo.value = ""

    def limpar_campos_veiculo():
        for campo in [input_marca, input_modelo, input_placa, input_ano_fabricacao]:
            campo.value = ""

    def limpar_campos_ordem():
        for campo in [input_data_abertura, input_descricao_servico, input_status, input_valor_estimado]:
            campo.value = ""

    # Mensagens de sucesso e erro
    mensagem_sucesso = ft.SnackBar(
        ft.Text("Salvo com sucesso", color=Colors.WHITE),
        open=False,
        bgcolor=Colors.GREEN_ACCENT_700,
    )

    mensagem_erro = ft.SnackBar(
        ft.Text("Preencha todos os campos obrigatórios", color=Colors.WHITE),
        open=False,
        bgcolor=Colors.RED_ACCENT_700,
    )

    # Layout da tela inicial
    def main_view():
        return ft.Column(
            controls=[
                ft.ElevatedButton("Cadastrar Cliente", on_click=cadastrar_cliente, bgcolor=Colors.RED_700,
                                  color=Colors.WHITE),
                ft.ElevatedButton("Cadastrar Veículo", on_click=cadastrar_veiculo, bgcolor=Colors.RED_700,
                                  color=Colors.WHITE),
                ft.ElevatedButton("Cadastrar Ordem de Serviço", on_click=cadastrar_ordem, bgcolor=Colors.RED_700,
                                  color=Colors.WHITE),
                ft.ElevatedButton("Ver Clientes Cadastrados", on_click=ver_clientes, bgcolor=Colors.BLUE_700,
                                  color=Colors.WHITE),
                ft.ElevatedButton("Ver Veículos Cadastrados", on_click=ver_veiculos, bgcolor=Colors.BLUE_700,
                                  color=Colors.WHITE),
                ft.ElevatedButton("Ver Ordens de Serviço Cadastradas", on_click=ver_ordens, bgcolor=Colors.BLUE_700,
                                  color=Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

    # Layout da tela de cadastro de cliente
    def cliente_view():
        return ft.View(
            appbar=AppBar(title=Text("Cadastrar Cliente", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[
                ft.TextField(label='Nome:', hint_text='EX: Fernanda', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_nome),
                ft.TextField(label='CPF:', hint_text='EX: 12345678910', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_cpf),
                ft.TextField(label='Telefone:', hint_text='EX: 12345678910', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_telefone),
                ft.TextField(label='Endereço:', hint_text='EX: Rua da alegria, 123', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_endereco),
                ft.ElevatedButton("Salvar", on_click=salvar_cliente, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Voltar", on_click=voltar, bgcolor=Colors.GREY_700, color=Colors.WHITE),
            ],
            bgcolor=Colors.RED_100,
        )

    # Layout da tela de cadastro de veículo
    def veiculo_view():
        return ft.View(
            appbar=AppBar(title=Text("Cadastrar Veículo", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[
                ft.TextField(label='Marca:', hint_text='EX: Ford', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_marca),
                ft.TextField(label='Modelo:', hint_text='EX: Fusca', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_modelo),
                ft.TextField(label='Placa:', hint_text='EX: A1B23C', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_placa),
                ft.TextField(label='Ano de fabricação:', hint_text='EX: 2007', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_ano_fabricacao),
                ft.ElevatedButton("Salvar", on_click=salvar_veiculo, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Voltar", on_click=voltar, bgcolor=Colors.GREY_700, color=Colors.WHITE),
            ],
            bgcolor=Colors.RED_100,
        )

    # Layout da tela de cadastro de ordem de serviço
    def ordem_view():
        return ft.View(
            appbar=AppBar(title=Text("Cadastrar Ordem de Serviço", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[
                ft.TextField(label='Data da abertura:', hint_text='EX: 04-10-2024', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_data_abertura),
                ft.TextField(label='Descrição do serviço:', hint_text='EX: Troca de óleo', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_descricao_servico),
                ft.TextField(label='Status:', hint_text='EX: Completo', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_status),
                ft.TextField(label='Valor estimado:', hint_text='EX: 1400', border_color=Colors.RED_700,
                             focused_border_color=Colors.RED_900, ref=input_valor_estimado),
                ft.ElevatedButton("Salvar", on_click=salvar_ordem, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Voltar", on_click=voltar, bgcolor=Colors.GREY_700, color=Colors.WHITE),
            ],
            bgcolor=Colors.RED_100,
        )

    # Função para construir a lista de cadastrados
    def construir_lista_cadastrados(tipo):
        lista_cadastrados = []

        if tipo == "clientes":
            lista_cadastrados.append(ft.Text("Clientes Cadastrados:", weight="bold"))
            for c in clientes:
                lista_cadastrados.append(ft.Text(
                    f"Nome: {c['nome']}, CPF: {c['cpf']}, Telefone: {c['telefone']}, Endereço: {c['endereco']}"))

        elif tipo == "veiculos":
            lista_cadastrados.append(ft.Text("Veículos Cadastrados:", weight="bold"))
            for v in veiculos:
                lista_cadastrados.append(ft.Text(
                    f"Marca: {v['marca']}, Modelo: {v['modelo']}, Placa: {v['placa']}, Ano: {v['ano_fabricacao']}"))

        elif tipo == "ordens":
            lista_cadastrados.append(ft.Text("Ordens de Serviço Cadastradas:", weight="bold"))
            for o in ordens:
                lista_cadastrados.append(ft.Text(
                    f"Data: {o['data_abertura']}, Descrição: {o['descricao_servico']}, Status: {o['status']}, Valor: {o['valor_estimado']}"))

        if not lista_cadastrados or len(lista_cadastrados) == 1:  # Se não houver registros, mostrar mensagem
            lista_cadastrados.append(ft.Text("Nenhum registro cadastrado."))

        return lista_cadastrados

    # Layout da tela de cadastrados
    def cadastrados_view(tipo):
        lista_cadastrados = construir_lista_cadastrados(tipo)

        return ft.View(
            appbar=AppBar(title=Text("Cadastrados", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[
                ft.Column(
                    controls=lista_cadastrados,
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
                ft.ElevatedButton("Voltar", on_click=voltar, bgcolor=Colors.GREY_700, color=Colors.WHITE),
            ],
            bgcolor=Colors.RED_100,
        )

    # Função para voltar
    def voltar(e):
        page.go("/")

    # Roteamento
    def gerencia_rotas(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(View(appbar=AppBar(title=Text("Cadastro", color=Colors.WHITE), bgcolor=Colors.RED_800),
                                   controls=[main_view()], bgcolor=Colors.RED_100))
        elif page.route == "/cliente":
            page.views.append(cliente_view())
        elif page.route == "/veiculo":
            page.views.append(veiculo_view())
        elif page.route == "/ordem":
            page.views.append(ordem_view())
        elif page.route == "/cadastrados/clientes":
            page.views.append(cadastrados_view("clientes"))
        elif page.route == "/cadastrados/veiculos":
            page.views.append(cadastrados_view("veiculos"))
        elif page.route == "/cadastrados/ordens":
            page.views.append(cadastrados_view("ordens"))
        page.update()

    # Inicialização dos campos
    input_nome = ft.TextField()
    input_cpf = ft.TextField()
    input_telefone = ft.TextField()
    input_endereco = ft.TextField()
    input_marca = ft.TextField()
    input_modelo = ft.TextField()
    input_placa = ft.TextField()
    input_ano_fabricacao = ft.TextField()
    input_data_abertura = ft.TextField()
    input_descricao_servico = ft.TextField()
    input_status = ft.TextField()
    input_valor_estimado = ft.TextField()

    page.on_route_change = gerencia_rotas
    page.go("/")


ft.app(target=main)

