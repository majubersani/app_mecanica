import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

def main(page: ft.Page):
    page.title = "Cadastro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 375
    page.window_height = 667

    clientes, veiculos, ordens = [], [], []

    def input_field(label):
        return ft.TextField(
            label=label,
            border_radius=10,
            filled=True,
            fill_color=Colors.RED_100,
            border_color=Colors.RED_300
        )

    input_nome = input_field("Nome:")
    input_cpf = input_field("CPF:")
    input_telefone = input_field("Telefone:")
    input_endereco = input_field("Endereço:")

    input_marca = input_field("Marca:")
    input_modelo = input_field("Modelo:")
    input_placa = input_field("Placa:")
    input_ano_fabricacao = input_field("Ano de fabricação:")

    input_data_abertura = input_field("Data da abertura:")
    input_descricao_servico = input_field("Descrição do serviço:")
    input_status = input_field("Status:")
    input_valor_estimado = input_field("Valor estimado:")

    def cadastrar_cliente(e): page.go("/cliente")
    def cadastrar_veiculo(e): page.go("/veiculo")
    def cadastrar_ordem(e): page.go("/ordem")
    def ver_cadastrados(e): page.go("/cadastrados")
    def voltar(e): page.go("/")

    def salvar_cliente(e):
        if input_nome.value and input_cpf.value and input_telefone.value and input_endereco.value:
            clientes.append({
                "nome": input_nome.value,
                "cpf": input_cpf.value,
                "telefone": input_telefone.value,
                "endereco": input_endereco.value
            })
            input_nome.value = input_cpf.value = input_telefone.value = input_endereco.value = ""
            page.go("/cadastrados")

    def salvar_veiculo(e):
        if input_marca.value and input_modelo.value and input_placa.value and input_ano_fabricacao.value:
            veiculos.append({
                "marca": input_marca.value,
                "modelo": input_modelo.value,
                "placa": input_placa.value,
                "ano_fabricacao": input_ano_fabricacao.value
            })
            input_marca.value = input_modelo.value = input_placa.value = input_ano_fabricacao.value = ""
            page.go("/cadastrados")

    def salvar_ordem(e):
        if input_data_abertura.value and input_descricao_servico.value and input_status.value and input_valor_estimado.value:
            ordens.append({
                "data_abertura": input_data_abertura.value,
                "descricao_servico": input_descricao_servico.value,
                "status": input_status.value,
                "valor_estimado": input_valor_estimado.value
            })
            input_data_abertura.value = input_descricao_servico.value = input_status.value = input_valor_estimado.value = ""
            page.go("/cadastrados")

    def main_view():
        return ft.Column(
            controls=[
                ft.Image(src="Logos_app_py.png", width=350),
                ft.ElevatedButton("Cadastrar Cliente", on_click=cadastrar_cliente, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Cadastrar Veículo", on_click=cadastrar_veiculo, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Cadastrar Ordem de Serviço", on_click=cadastrar_ordem, bgcolor=Colors.RED_700, color=Colors.WHITE),
                ft.ElevatedButton("Ver Cadastrados", on_click=ver_cadastrados, bgcolor=Colors.WHITE, color=Colors.RED_700),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

    def form_view(title, inputs, on_save):
        return ft.View(
            f"/{title.lower()}",
            controls=[
                *[ft.Container(content=i, padding=5) for i in inputs],
                ft.Container(ft.ElevatedButton("Salvar", on_click=on_save, expand=True), padding=5),
                ft.Container(ft.ElevatedButton("Voltar", on_click=voltar, expand=True), padding=5),
            ],
            appbar=AppBar(title=Text(f"Cadastrar {title}"), bgcolor=Colors.RED_800),
            bgcolor=Colors.RED_100
        )

    def cliente_view():
        return form_view("Cliente", [input_nome, input_cpf, input_telefone, input_endereco], salvar_cliente)

    def veiculo_view():
        return form_view("Veículo", [input_marca, input_modelo, input_placa, input_ano_fabricacao], salvar_veiculo)

    def ordem_view():
        return form_view("Ordem de Serviço", [input_data_abertura, input_descricao_servico, input_status, input_valor_estimado], salvar_ordem)

    def cadastrados_view():
        return ft.View(
            "/cadastrados",
            controls=[
                *[ft.Text(f"{c['nome']} | {c['cpf']} | {c['telefone']} | {c['endereco']}") for c in clientes],
                ft.Divider(),
                *[ft.Text(f"{v['marca']} {v['modelo']} | {v['placa']} | {v['ano_fabricacao']}") for v in veiculos],
                ft.Divider(),
                *[ft.Text(f"{o['data_abertura']} | {o['descricao_servico']} | {o['status']} | R$ {o['valor_estimado']}") for o in ordens],
                   ft.ElevatedButton("Voltar", on_click=voltar, color=Colors.RED_800),
            ],
            appbar=AppBar(title=Text("Cadastrados"), bgcolor=Colors.RED_800),
            bgcolor=Colors.RED_100
        )

    def gerencia_rotas(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(View("/", [main_view()], bgcolor=Colors.RED_100))
        elif page.route == "/cliente":
            page.views.append(cliente_view())
        elif page.route == "/veiculo":
            page.views.append(veiculo_view())
        elif page.route == "/ordem":
            page.views.append(ordem_view())
        elif page.route == "/cadastrados":
            page.views.append(cadastrados_view())
        page.update()

    page.on_route_change = gerencia_rotas
    page.go("/")

ft.app(target=main)