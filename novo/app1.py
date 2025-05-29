import flet as ft
from flet import AppBar, Text, View, IconButton
from flet.core.colors import Colors

def main(page: ft.Page):
    # Configuração da página
    page.title = "Cadastro de Cliente"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 375
    page.window_height = 667
    page.bgcolor = Colors.RED_ACCENT_100

    # Dados e funções
    clientes = []
    campos_cliente = {}

    # Funções de cadastro (ainda incompletas)
    def cadastrar_cliente(e):
        # Lógica para cadastrar cliente (você pode manter o código existente aqui)
        print("Cadastrar Cliente")
        # Exibir a tela de cadastro de cliente (main_view)
        page.go("/") # Redireciona para a tela principal de cadastro de cliente

    def cadastrar_veiculo(e):
        print("Cadastrar Veículo")
        # Implementar a lógica para cadastrar veículo
        # Criar os campos de texto para veiculo e adicionar a tela
        # Exibir a tela de cadastro de veículo
        page.go("/veiculo")

    def cadastrar_ordem(e):
        print("Cadastrar Ordem de Serviço")
        # Implementar a lógica para cadastrar ordem de serviço
        # Criar os campos de texto para ordem de serviço e adicionar a tela
        # Exibir a tela de cadastro de ordem de serviço
        page.go("/ordem")

    def salvar_cliente(e):
        if not input_nome.value:
            page.show_snack_bar(mensagem_erro)
            return

        cliente = {
            "nome": input_nome.value,
            "cpf": input_cpf.value,
            "telefone": input_telefone.value,
            "endereco": input_endereco.value,
            "marca": input_marca.value,
            "modelo": input_modelo.value,
            "placa": input_placa.value,
            "ano_fabricacao": input_ano_fabricacao.value,
            "data_abertura": input_data_abertura.value,
            "descricao_servico": input_descricao_servico.value,
            "status": input_status.value,
            "valor_estimado": input_valor_estimado.value
        }
        clientes.append(cliente)  # Adiciona o cliente à lista

        # Limpa os campos após salvar
        for campo in campos_cliente.values():
            campo.value = ""

        page.show_snack_bar(mensagem_sucesso)
        page.update()

    def voltar(e):
        page.go("/")

    # Criação de componentes
    input_nome = ft.TextField(label='Nome:', hint_text='EX: Fernanda', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_cpf = ft.TextField(label='CPF:', hint_text='EX: 12345678910', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_telefone = ft.TextField(label='Telefone:', hint_text='EX: 12345678910', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_endereco = ft.TextField(label='Endereço:', hint_text='EX: Rua da alegria, 123', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_marca = ft.TextField(label='Marca:', hint_text='EX: Ford', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_modelo = ft.TextField(label='Modelo:', hint_text='EX: Fusca', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_placa = ft.TextField(label='Placa:', hint_text='EX: A1B23C', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_ano_fabricacao = ft.TextField(label='Ano de fabricação:', hint_text='EX: 2007', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_data_abertura = ft.TextField(label='Data da abertura:', hint_text='EX: 04-10-2024', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_descricao_servico = ft.TextField(label='Descrição do serviço:', hint_text='EX: Troca de óleo', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_status = ft.TextField(label='Status:', hint_text='EX: Completo', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)
    input_valor_estimado = ft.TextField(label='Valor estimado:', hint_text='EX: 1400', border_color=Colors.RED_700, focused_border_color=Colors.RED_900)

    # Adiciona os campos ao dicionário
    campos_cliente = {
        "nome": input_nome,
        "cpf": input_cpf,
        "telefone": input_telefone,
        "endereco": input_endereco,
        "marca": input_marca,
        "modelo": input_modelo,
        "placa": input_placa,
        "ano_fabricacao": input_ano_fabricacao,
        "data_abertura": input_data_abertura,
        "descricao_servico": input_descricao_servico,
        "status": input_status,
        "valor_estimado": input_valor_estimado
    }

    mensagem_sucesso = ft.SnackBar(
        ft.Text("Salvo com sucesso", color=Colors.WHITE),
        open=False,
        bgcolor=Colors.GREEN_ACCENT_700,
    )

    mensagem_erro = ft.SnackBar(
        ft.Text("Preencha o campo nome", color=Colors.WHITE),
        open=False,
        bgcolor=Colors.RED_ACCENT_700,
    )

    # Layout da página principal (com os botões)
    def main_view():
        return ft.Column(
            controls=[
                ft.ElevatedButton("Cadastrar Cliente", on_click=cadastrar_cliente, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Cadastrar Veículo", on_click=cadastrar_veiculo, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Cadastrar Ordem de Serviço", on_click=cadastrar_ordem, bgcolor=Colors.RED_700, color=Colors.WHITE),
                # Adicione os campos de cliente aqui (ou em outra função/view)
                input_nome,
                input_cpf,
                input_telefone,
                input_endereco,
                input_marca,
                input_modelo,
                input_placa,
                input_ano_fabricacao,
                input_data_abertura,
                input_descricao_servico,
                input_status,
                input_valor_estimado,
                ft.ElevatedButton("Salvar", on_click=salvar_cliente, bgcolor=Colors.RED_700, color=Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

    # Views para cada rota
    def cliente_view():
        return ft.View(
            appbar=AppBar(title=Text("Cadastro de Cliente", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[main_view()], # Usando a main_view para o cadastro de cliente
            bgcolor=Colors.RED_100,
        )

    def veiculo_view():
        return ft.View(
            appbar=AppBar(title=Text("Cadastro de Veículo", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[Text("Tela de Cadastro de Veículo")], # Substitua com os campos de veículo
            bgcolor=Colors.RED_100,
        )

    def ordem_view():
        return ft.View(
            appbar=AppBar(title=Text("Cadastro de Ordem de Serviço", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[Text("Tela de Cadastro de Ordem de Serviço")], # Substitua com os campos de ordem de serviço
            bgcolor=Colors.RED_100,
        )

    # Roteamento
    def gerencia_rotas(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(cliente_view()) # Mostra a tela principal (cadastro de cliente)
        elif page.route == "/veiculo":
            page.views.append(veiculo_view()) # Mostra a tela de cadastro de veículo
        elif page.route == "/ordem":
            page.views.append(ordem_view()) # Mostra a tela de cadastro de ordem de serviço
        page.update()

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(target=main)
