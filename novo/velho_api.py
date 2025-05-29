import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors


def main(page: ft.Page):

    # Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667


    # Definição de funções
    lista = []

    def salvar_cliente(e):
        if input_nome.value == "":
            page.overlay.append(msg_error)
            msg_error = True
            page.update()
        else:
            lista.append(input_nome.value)
            input_nome.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()



    # Criação de componentes
    input_nome = ft.TextField(label='Nome:', hint_text='EX: Fernanda')

    input_cpf = ft.TextField(label='CPF:', hint_text='EX: 12345678910')

    input_telefone = ft.TextField(label='Telefone:', hint_text='EX: 12345678910')

    input_endereco = ft.TextField(label='Endereço:', hint_text='EX: Rua da alegria, 123')

    input_marca = ft.TextField(label='Marca:', hint_text='EX: Ford')

    input_modelo = ft.TextField(label='Modelo:', hint_text='EX: Fusca')

    input_placa = ft.TextField(label='Placa:', hint_text='EX: A1B23C')

    input_ano_fabricacao = ft.TextField(label='Ano de fabricação:', hint_text='EX: 2007')

    input_data_abertura = ft.TextField(label='Data da abertura:', hint_text='EX: 04-10-2024')

    input_descricao_servico = ft.TextField(label='Descrição do serviço:', hint_text='EX: Troca de óleo')

    input_status = ft.TextField(label='Status:', hint_text='EX: Completo')

    input_valor_estimado = ft.TextField(label='Valor estimado:', hint_text='EX: 1400')

    msg_sucesso = ft.SnackBar(
        content=ft.Text("Salvo com sucesso"),
        bgcolor=Colors.GREEN
    )

    msg_erro = ft.SnackBar(
        content=ft.Text("Preencha todos os campos"),
        bgcolor=Colors.RED
    )

    lv_nome = ft.ListView(
        height=500
    )


    # Construir o layout
    page.add(
        input_nome
    )


    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)