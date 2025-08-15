import flet as ft
from flet import colors
import funcoes_api as api_funcoes


def main(page: ft.Page):
    page.title = "Sistema de Oficina"
    page.scroll = "auto"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Componentes globais para evitar NoneType
    msg_bar = ft.SnackBar(open=False)
    dd_cliente_veiculo = ft.Dropdown()

    page.overlay.append(msg_bar)

    # Função para exibir mensagens
    def mostrar_mensagem(mensagem, cor=colors.GREEN):
    msg_bar.content = ft.Text(mensagem, color=cor)
    msg_bar.open = True
    page.update()

    # Rota inicial
    def route_change(route):
    page.views.clear()

    if page.route == "/":
        page.views.append(
            ft.View(
            "/",
            [
                        ft.AppBar(title=ft.Text("Menu Principal"), bgcolor=colors.PURPLE_900),
                        ft.Column(
                            [
                                ft.ElevatedButton("Clientes", on_click=lambda _: page.go("/clientes")),
                                ft.ElevatedButton("Veículos", on_click=lambda _: page.go("/veiculos")),
                                ft.ElevatedButton("Ordens de Serviço", on_click=lambda _: page.go("/ordens_servico")),
                            ]
                        ),
                    ],
                )
            )

        elif page.route == "/clientes":
            clientes_resp = api_funcoes.get_clientes()
            if clientes_resp["success"]:
                lista = clientes_resp["data"]
                items = [
                    ft.ListTile(
                        title=ft.Text(c["nome"]),
                        subtitle=ft.Text(f"CPF: {c['cpf']}"),
                        trailing=ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(
                                    text="Ver detalhes",
                                    on_click=lambda e, cliente=c: mostrar_mensagem(f"Cliente: {cliente['nome']}")
                                )
                            ]
                        )
                    ) for c in lista
                ]
            else:
                items = [ft.Text("Erro ao carregar clientes")]

            page.views.append(
                ft.View(
            "/clientes",
            [
                        ft.AppBar(title=ft.Text("Clientes"), bgcolor=colors.PURPLE_900),
                        ft.Column(items)
                    ]
                )
)

elif page.route == "/veiculos":
veiculos_resp = api_funcoes.get_veiculos()
if veiculos_resp["success"]:
lista = veiculos_resp["data"]
items = [
ft.ListTile(
title=ft.Text(f"{v['marca']} {v['modelo']}"),
subtitle=ft.Text(f"Placa: {v['placa']}"),
) for v in lista
]
else:
items = [ft.Text("Erro ao carregar veículos")]

page.views.append(
ft.View(
"/veiculos",
[
ft.AppBar(title=ft.Text("Veículos"), bgcolor=colors.PURPLE_900),
ft.Column(items)
]
)
)

elif page.route == "/ordens_servico":
ordens_resp = api_funcoes.get_ordens_servico()
if ordens_resp["success"]:
lista = ordens_resp["data"]
items = [
ft.ListTile(
title=ft.Text(f"Serviço: {o['descricao_de_servico']}"),
subtitle=ft.Text(f"Status: {o['status']} - Valor: R$ {o['valor_total']}")
) for o in lista
]
else:
items = [ft.Text("Erro ao carregar ordens de serviço")]

page.views.append(
ft.View(
"/ordens_servico",
[
ft.AppBar(title=ft.Text("Ordens de Serviço"), bgcolor=colors.PURPLE_900),
ft.Column(items)
]
)
)

# Voltar de rotas
def view_pop(view):
page.views.pop()
page.go(page.views[-1].route)

page.on_route_change = route_change
page.on_view_pop = view_pop

page.go(page.route)


ft.app(target=main)