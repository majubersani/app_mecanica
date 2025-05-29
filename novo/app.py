import flet as ft
from flet import AppBar, Text, View, IconButton
from flet.core.colors import Colors

def main(page: ft.Page):
    # Configuração da página
    page.title = "Cadastro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 375
    page.window_height = 667
    page.bgcolor = Colors.RED_ACCENT_100

    # Funções de cadastro
    def cadastrar_cliente(e):
        page.go("/cliente")

    def cadastrar_veiculo(e):
        page.go("/veiculo")

    def cadastrar_ordem(e):
        page.go("/ordem")

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
        # Aqui você pode adicionar lógica para salvar os dados do cliente
        print("Cliente salvo:", cliente)

        # Limpa os campos após salvar
        for campo in [input_nome, input_cpf, input_telefone, input_endereco]:
            campo.value = ""

        page.show_snack_bar(mensagem_sucesso)
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
        # Aqui você pode adicionar lógica para salvar os dados do veículo
        print("Veículo salvo:", veiculo)

        # Limpa os campos após salvar
        for campo in [input_marca, input_modelo, input_placa, input_ano_fabricacao]:
            campo.value = ""

        page.show_snack_bar(mensagem_sucesso)
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
        # Aqui você pode adicionar lógica para salvar os dados da ordem de serviço
        print("Ordem de serviço salva:", ordem)

        # Limpa os campos após salvar
        for campo in [input_data_abertura, input_descricao_servico, input_status, input_valor_estimado]:
            campo.value = ""

        page.show_snack_bar(mensagem_sucesso)
        page.update()

    # Função para voltar
    def voltar(e):
        page.go("/")

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
                ft.ElevatedButton("Cadastrar Cliente", on_click=cadastrar_cliente, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Cadastrar Veículo", on_click=cadastrar_veiculo, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Cadastrar Ordem de Serviço", on_click=cadastrar_ordem, bgcolor=Colors.RED_700, color=Colors.WHITE),
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
                ft.TextField(label='Nome:', hint_text='EX: Fernanda', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_nome),
                ft.TextField(label='CPF:', hint_text='EX: 12345678910', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_cpf),
                ft.TextField(label='Telefone:', hint_text='EX: 12345678910', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_telefone),
                ft.TextField(label='Endereço:', hint_text='EX: Rua da alegria, 123', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_endereco),
                ft.ElevatedButton("Salvar", on_click=salvar_cliente, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Voltar", on_click=voltar, bgcolor=Colors.GREY_700, color=Colors.WHITE), # Botão Voltar
            ],
            bgcolor=Colors.RED_100,
        )

    # Layout da tela de cadastro de veículo
    def veiculo_view():
        return ft.View(
            appbar=AppBar(title=Text("Cadastrar Veículo", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[
                ft.TextField(label='Marca:', hint_text='EX: Ford', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_marca),
                ft.TextField(label='Modelo:', hint_text='EX: Fusca', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_modelo),
                ft.TextField(label='Placa:', hint_text='EX: A1B23C', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_placa),
                ft.TextField(label='Ano de fabricação:', hint_text='EX: 2007', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_ano_fabricacao),
                ft.ElevatedButton("Salvar", on_click=salvar_veiculo, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Voltar", on_click=voltar, bgcolor=Colors.GREY_700, color=Colors.WHITE), # Botão Voltar
            ],
            bgcolor=Colors.RED_100,
        )

    # Layout da tela de cadastro de ordem de serviço
    def ordem_view():
        return ft.View(
            appbar=AppBar(title=Text("Cadastrar Ordem de Serviço", color=Colors.WHITE), bgcolor=Colors.RED_800),
            controls=[
                ft.TextField(label='Data da abertura:', hint_text='EX: 04-10-2024', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_data_abertura),
                ft.TextField(label='Descrição do serviço:', hint_text='EX: Troca de óleo', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_descricao_servico),
                ft.TextField(label='Status:', hint_text='EX: Completo', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_status),
                ft.TextField(label='Valor estimado:', hint_text='EX: 1400', border_color=Colors.RED_700, focused_border_color=Colors.RED_900, ref=input_valor_estimado),
                ft.ElevatedButton("Salvar", on_click=salvar_ordem, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Voltar", on_click=voltar, bgcolor=Colors.GREY_700, color=Colors.WHITE), # Botão Voltar
            ],
            bgcolor=Colors.RED_100,
        )

    # Roteamento
    def gerencia_rotas(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(View(appbar=AppBar(title=Text("Cadastro", color=Colors.WHITE), bgcolor=Colors.RED_800), controls=[main_view()], bgcolor=Colors.RED_100))
        elif page.route == "/cliente":
            page.views.append(cliente_view())
        elif page.route == "/veiculo":
            page.views.append(veiculo_view())
        elif page.route == "/ordem":
            page.views.append(ordem_view())
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
