import flet as ft
from flet import (
    AppBar, Text, View, ElevatedButton, TextField, ListView,
    ListTile, Icon, PopupMenuButton, PopupMenuItem, Image, Dropdown, SnackBar
)
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.types import CrossAxisAlignment
import flet as api_funcoes  # Importa suas funções da API


def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Sistema de Mecânica Automotiva"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Variáveis para controle de edição
    editar_cliente_id = None
    editar_veiculo_id = None
    editar_ordem_servico_id = None

    # --- Funções de Carregamento para Dropdowns ---
    def carregar_clientes_dropdown(dd_cliente_veiculo=None):
        """Carrega a lista de clientes para o Dropdown de associação de veículos."""
        clientes_response = api_funcoes.get_clientes()
        if clientes_response["success"]:
            clientes_data = clientes_response["data"]
            options = []
            for cliente in clientes_data:
                options.append(Option(
                    key=str(cliente['id']),
                    text=f"{cliente['nome']} (CPF: {cliente['cpf']})"
                ))
            dd_cliente_veiculo.options = options
            page.update()
        else:
            mostrar_mensagem(clientes_response["message"], success=False)

    def carregar_veiculos_dropdown(dd_veiculo_ordem=None):
        """Carrega a lista de veículos para o Dropdown de associação de ordens de serviço."""
        veiculos_response = api_funcoes.get_veiculos()
        if veiculos_response["success"]:
            veiculos_data = veiculos_response["data"]
            options = []
            for veiculo in veiculos_data:
                options.append(Option(
                    key=veiculo['placa'],  # Usando a placa como chave para ordens de serviço
                    text=f"{veiculo['modelo']} ({veiculo['placa']})"
                ))
            dd_veiculo_ordem.options = options
            page.update()
        else:
            mostrar_mensagem(veiculos_response["message"], success=False)

    # --- Funções de Salvar (Cadastro) ---
    def salvar_cliente(e, nome_cliente=None, cpf_cliente=None, telefone_cliente=None, endereco_cliente=None):
        """Salva um novo cliente."""
        if nome_cliente.value.strip() and cpf_cliente.value.strip() and telefone_cliente.value.strip() and endereco_cliente.value.strip():
            response = api_funcoes.post_cliente(
                nome_cliente.value.strip(),
                cpf_cliente.value.strip(),
                telefone_cliente.value.strip(),
                endereco_cliente.value.strip()
            )
            if response["success"]:
                nome_cliente.value = cpf_cliente.value = telefone_cliente.value = endereco_cliente.value = ""
                mostrar_mensagem("Cliente cadastrado com sucesso!", success=True)
                page.go("/lista_clientes")
            else:
                mostrar_mensagem(response["message"], success=False)
        else:
            mostrar_mensagem("Preencha todos os campos!", success=False)
        page.update()

    def salvar_veiculo(e, dd_cliente_veiculo=None, modelo_veiculo=None, ano_veiculo=None, placa_veiculo=None,
                       marca_veiculo=None):
        """Salva um novo veículo."""
        selected_cliente_id = dd_cliente_veiculo.value
        if (marca_veiculo.value.strip() and modelo_veiculo.value.strip() and
                placa_veiculo.value.strip() and ano_veiculo.value.strip() and
                selected_cliente_id):

            try:
                ano = int(ano_veiculo.value.strip())
                cliente_id = int(selected_cliente_id)
            except ValueError:
                mostrar_mensagem("Ano e ID do Cliente devem ser números válidos!", success=False)
                return

            response = api_funcoes.post_veiculo(
                marca_veiculo.value.strip(),
                modelo_veiculo.value.strip(),
                placa_veiculo.value.strip(),
                ano,
                cliente_id
            )
            if response["success"]:
                marca_veiculo.value = modelo_veiculo.value = placa_veiculo.value = ano_veiculo.value = ""
                dd_cliente_veiculo.value = None
                mostrar_mensagem("Veículo cadastrado com sucesso!", success=True)
                page.go("/lista_veiculos")
            else:
                mostrar_mensagem(response["message"], success=False)
        else:
            mostrar_mensagem("Preencha todos os campos e selecione um cliente!", success=False)
        page.update()

    def salvar_ordem_servico(e, dd_veiculo_ordem=None, valor_total_os=None, data_abertura_os=None, status_os=None,
                             descricao_os=None):
        """Salva uma nova ordem de serviço."""
        selected_veiculo_placa = dd_veiculo_ordem.value
        if (descricao_os.value.strip() and data_abertura_os.value.strip() and
                status_os.value.strip() and valor_total_os.value.strip() and
                selected_veiculo_placa):

            try:
                valor_total = float(valor_total_os.value.strip())
            except ValueError:
                mostrar_mensagem("Valor Total deve ser um número válido!", success=False)
                return

            response = api_funcoes.post_ordem_servico(
                selected_veiculo_placa,
                descricao_os.value.strip(),
                data_abertura_os.value.strip(),
                status_os.value.strip(),
                valor_total
            )
            if response["success"]:
                descricao_os.value = data_abertura_os.value = status_os.value = valor_total_os.value = ""
                dd_veiculo_ordem.value = None
                mostrar_mensagem("Ordem de Serviço cadastrada com sucesso!", success=True)
                page.go("/lista_ordens_servico")
            else:
                mostrar_mensagem(response["message"], success=False)
        else:
            mostrar_mensagem("Preencha todos os campos e selecione um veículo!", success=False)
        page.update()

    # --- Funções de Salvar (Edição) ---
    def salvar_editar_cliente(e, edit_endereco_cliente=None, edit_telefone_cliente=None, edit_cpf_cliente=None,
                              edit_nome_cliente=None):
        """Salva as alterações de um cliente."""
        nonlocal editar_cliente_id
        if editar_cliente_id is None:
            mostrar_mensagem("Nenhum cliente selecionado para editar.", success=False)
            return

        if (edit_nome_cliente.value.strip() and edit_cpf_cliente.value.strip() and
                edit_telefone_cliente.value.strip() and edit_endereco_cliente.value.strip()):

            response = api_funcoes.atualizar_cliente(
                editar_cliente_id,
                edit_nome_cliente.value.strip(),
                edit_cpf_cliente.value.strip(),
                edit_telefone_cliente.value.strip(),
                edit_endereco_cliente.value.strip()
            )
            if response["success"]:
                mostrar_mensagem("Cliente atualizado com sucesso!", success=True)
                editar_cliente_id = None
                page.go("/lista_clientes")
            else:
                mostrar_mensagem(response["message"], success=False)
        else:
            mostrar_mensagem("Preencha todos os campos!", success=False)
        page.update()

    def salvar_editar_veiculo(e, edit_marca_veiculo=None, edit_modelo_veiculo=None, edit_ano_veiculo=None,
                              edit_placa_veiculo=None):
        """Salva as alterações de um veículo."""
        nonlocal editar_veiculo_id
        if editar_veiculo_id is None:
            mostrar_mensagem("Nenhum veículo selecionado para editar.", success=False)
            return

        if (edit_marca_veiculo.value.strip() and edit_modelo_veiculo.value.strip() and
                edit_placa_veiculo.value.strip() and edit_ano_veiculo.value.strip()):

            try:
                ano = int(edit_ano_veiculo.value.strip())
            except ValueError:
                mostrar_mensagem("Ano deve ser um número válido!", success=False)
                return

            response = api_funcoes.atualizar_veiculo(
                editar_veiculo_id,
                edit_marca_veiculo.value.strip(),
                edit_modelo_veiculo.value.strip(),
                edit_placa_veiculo.value.strip(),
                ano
            )
            if response["success"]:
                mostrar_mensagem("Veículo atualizado com sucesso!", success=True)
                editar_veiculo_id = None
                page.go("/lista_veiculos")
            else:
                mostrar_mensagem(response["message"], success=False)
        else:
            mostrar_mensagem("Preencha todos os campos!", success=False)
        page.update()

    def salvar_editar_ordem_servico(e, edit_status_os=None, edit_descricao_os=None, edit_data_abertura_os=None,
                                    edit_veiculos_associados_os=None, edit_valor_total_os=None):
        """Salva as alterações de uma ordem de serviço."""
        nonlocal editar_ordem_servico_id
        if editar_ordem_servico_id is None:
            mostrar_mensagem("Nenhuma Ordem de Serviço selecionada para editar.", success=False)
            return

        if (edit_veiculos_associados_os.value.strip() and edit_descricao_os.value.strip() and
                edit_data_abertura_os.value.strip() and edit_status_os.value.strip() and
                edit_valor_total_os.value.strip()):

            try:
                valor_total = float(edit_valor_total_os.value.strip())
            except ValueError:
                mostrar_mensagem("Valor Total deve ser um número válido!", success=False)
                return

            response = api_funcoes.atualizar_ordem_servico(
                editar_ordem_servico_id,
                edit_veiculos_associados_os.value.strip(),
                edit_descricao_os.value.strip(),
                edit_data_abertura_os.value.strip(),
                edit_status_os.value.strip(),
                valor_total
            )
            if response["success"]:
                mostrar_mensagem("Ordem de Serviço atualizada com sucesso!", success=True)
                editar_ordem_servico_id = None
                page.go("/lista_ordens_servico")
            else:
                mostrar_mensagem(response["message"], success=False)
        else:
            mostrar_mensagem("Preencha todos os campos!", success=False)
        page.update()

    # --- Funções de Exibição de Listas ---
    def exibir_lista_clientes(e, lv_clientes=None):
        """Exibe a lista de clientes."""
        lv_clientes.controls.clear()
        response = api_funcoes.get_clientes()
        if response["success"]:
            clientes = response["data"]
            if not clientes:
                lv_clientes.controls.append(Text("Nenhum cliente encontrado."))
            else:
                for c in clientes:
                    lv_clientes.controls.append(
                        ListTile(
                            leading=Icon(ft.Icons.PERSON),
                            title=Text(c["nome"]),
                            subtitle=Text(f"CPF: {c.get('cpf', '')} | Tel: {c.get('telefone', '')}"),
                            trailing=PopupMenuButton(
                                items=[
                                    PopupMenuItem(text="Detalhes",
                                                  on_click=lambda _, cliente=c: ver_detalhes_cliente(cliente)),
                                    PopupMenuItem(text="Editar",
                                                  on_click=lambda _, cliente=c: iniciar_edicao_cliente(cliente)),
                                ]
                            )
                        )
                    )
        else:
            lv_clientes.controls.append(Text(f"Erro ao carregar clientes: {response['message']}"))
        page.update()

    def exibir_lista_veiculos(e, lv_veiculos=None):
        """Exibe a lista de veículos."""
        lv_veiculos.controls.clear()
        response = api_funcoes.get_veiculos()
        if response["success"]:
            veiculos = response["data"]
            if not veiculos:
                lv_veiculos.controls.append(Text("Nenhum veículo encontrado."))
            else:
                for v in veiculos:
                    lv_veiculos.controls.append(
                        ListTile(
                            leading=Icon(ft.Icons.DIRECTIONS_CAR),
                            title=Text(f"{v['marca']} {v['modelo']}"),
                            subtitle=Text(
                                f"Placa: {v['placa']} | Ano: {v['ano_de_fabricacao']} | Cliente ID: {v['id_cliente']}"),
                            trailing=PopupMenuButton(
                                items=[
                                    PopupMenuItem(text="Detalhes",
                                                  on_click=lambda _, veiculo=v: ver_detalhes_veiculo(veiculo)),
                                    PopupMenuItem(text="Editar",
                                                  on_click=lambda _, veiculo=v: iniciar_edicao_veiculo(veiculo)),
                                ]
                            )
                        )
                    )
        else:
            lv_veiculos.controls.append(Text(f"Erro ao carregar veículos: {response['message']}"))
        page.update()

    def exibir_lista_ordens_servico(e, lv_ordens_servico=None):
        """Exibe a lista de ordens de serviço."""
        lv_ordens_servico.controls.clear()
        response = api_funcoes.get_ordens_servico()
        if response["success"]:
            ordens = response["data"]
            if not ordens:
                lv_ordens_servico.controls.append(Text("Nenhuma Ordem de Serviço encontrada."))
            else:
                for os in ordens:
                    lv_ordens_servico.controls.append(
                        ListTile(
                            leading=Icon(ft.Icons.RECEIPT_LONG),
                            title=Text(f"OS ID: {os.get('id_servicos', '')}"),
                            subtitle=Text(
                                f"Veículo: {os.get('veiculos_associados', '')} | Descrição: {os.get('descricao_de_servico', '')}\n"
                                f"Data: {os.get('data_de_abertura', '')} | Status: {os.get('status', '')} | Valor: R$ {os.get('valor_total', ''):.2f}"
                            ),
                            trailing=PopupMenuButton(
                                items=[
                                    PopupMenuItem(text="Detalhes",
                                                  on_click=lambda _, ordem=os: ver_detalhes_ordem_servico(ordem)),
                                    PopupMenuItem(text="Editar",
                                                  on_click=lambda _, ordem=os: iniciar_edicao_ordem_servico(ordem)),
                                ]
                            )
                        )
                    )
        else:
            lv_ordens_servico.controls.append(Text(f"Erro ao carregar Ordens de Serviço: {response['message']}"))
        page.update()

    # --- Funções de Iniciar Edição ---
    def iniciar_edicao_cliente(cliente, edit_endereco_cliente=None, edit_telefone_cliente=None, edit_cpf_cliente=None,
                               edit_nome_cliente=None):
        """Preenche os campos de edição com os dados do cliente selecionado."""
        nonlocal editar_cliente_id
        editar_cliente_id = cliente.get("id")
        edit_nome_cliente.value = cliente["nome"]
        edit_cpf_cliente.value = cliente.get("cpf", "")
        edit_telefone_cliente.value = cliente.get("telefone", "")
        edit_endereco_cliente.value = cliente["endereco"]
        page.go("/editar_cliente")
        page.update()

    def iniciar_edicao_veiculo(veiculo, edit_ano_veiculo=None, edit_placa_veiculo=None, edit_marca_veiculo=None,
                               edit_modelo_veiculo=None):
        """Preenche os campos de edição com os dados do veículo selecionado."""
        nonlocal editar_veiculo_id
        editar_veiculo_id = veiculo.get("id")
        edit_marca_veiculo.value = veiculo["marca"]
        edit_modelo_veiculo.value = veiculo["modelo"]
        edit_placa_veiculo.value = veiculo["placa"]
        edit_ano_veiculo.value = str(veiculo.get("ano_de_fabricacao", ""))
        page.go("/editar_veiculo")
        page.update()

    def iniciar_edicao_ordem_servico(ordem, edit_veiculos_associados_os=None, edit_descricao_os=None,
                                     edit_data_abertura_os=None, edit_status_os=None, edit_valor_total_os=None):
        """Preenche os campos de edição com os dados da ordem de serviço selecionada."""
        nonlocal editar_ordem_servico_id
        editar_ordem_servico_id = ordem.get("id_servicos")
        edit_veiculos_associados_os.value = ordem.get("veiculos_associados", "")
        edit_descricao_os.value = ordem["descricao_de_servico"]
        edit_data_abertura_os.value = ordem["data_de_abertura"]
        edit_status_os.value = ordem["status"]
        edit_valor_total_os.value = str(ordem.get("valor_total", ""))
        page.go("/editar_ordem_servico")
        page.update()

    # --- Funções de Ver Detalhes ---
    def ver_detalhes_cliente(cliente, txt_detalhes=None):
        """Exibe os detalhes de um cliente."""
        txt_detalhes.value = (
            f"ID: {cliente.get('id', '')}\n"
            f"Nome: {cliente.get('nome', '')}\n"
            f"CPF: {cliente.get('cpf', '')}\n"
            f"Telefone: {cliente.get('telefone', '')}\n"
            f"Endereço: {cliente.get('endereco', '')}"
        )
        page.go("/detalhes_cliente")
        page.update()

    def ver_detalhes_veiculo(veiculo, txt_detalhes=None):
        """Exibe os detalhes de um veículo."""
        txt_detalhes.value = (
            f"ID: {veiculo.get('id', '')}\n"
            f"Marca: {veiculo.get('marca', '')}\n"
            f"Modelo: {veiculo.get('modelo', '')}\n"
            f"Placa: {veiculo.get('placa', '')}\n"
            f"Ano de Fabricação: {veiculo.get('ano_de_fabricacao', '')}\n"
            f"ID do Cliente: {veiculo.get('id_cliente', '')}"
        )
        page.go("/detalhes_veiculo")
        page.update()

    def ver_detalhes_ordem_servico(ordem, txt_detalhes=None):
        """Exibe os detalhes de uma ordem de serviço."""
        txt_detalhes.value = (
            f"ID do Serviço: {ordem.get('id_servicos', '')}\n"
            f"Veículo Associado (Placa): {ordem.get('veiculos_associados', '')}\n"
            f"Descrição do Serviço: {ordem.get('descricao_de_servico', '')}\n"
            f"Data de Abertura: {ordem.get('data_de_abertura', '')}\n"
            f"Status: {ordem.get('status', '')}\n"
            f"Valor Total: R$ {ordem.get('valor_total', 0.0):.2f}"
        )
        page.go("/detalhes_ordem_servico")
        page.update()

    # Função para mostrar mensagens (sucesso/erro)
    def mostrar_mensagem(message, success=True, msg_bar=None):
        """Exibe um SnackBar com a mensagem fornecida."""
        msg_bar.content = Text(message)
        msg_bar.bgcolor = Colors.GREEN_700 if success else Colors.RED_700
        msg_bar.open = True
        page.update()

    # --- Gerenciamento de Rotas ---
    def gerencia_rota(e, txt_detalhes=None, cpf_cliente=None, telefone_cliente=None, endereco_cliente=None,
                      nome_cliente=None, edit_endereco_cliente=None, lv_clientes=None, edit_cpf_cliente=None,
                      edit_telefone_cliente=None, edit_nome_cliente=None, marca_veiculo=None, modelo_veiculo=None,
                      placa_veiculo=None, ano_veiculo=None, dd_cliente_veiculo=None, lv_veiculos=None,
                      edit_marca_veiculo=None, edit_modelo_veiculo=None, edit_ano_veiculo=None, edit_placa_veiculo=None):
        """Gerencia as visualizações da aplicação com base na rota."""
        page.views.clear()

        # Visão Principal (Menu Inicial)
        page.views.append(
            View(
                "/",
                [
                    Image(src="https://placehold.co/150x150/000000/FFFFFF?text=Mecânica"),
                    ElevatedButton("Clientes", on_click=lambda _: page.go("/clientes"), width=200,
                                   color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ElevatedButton("Veículos", on_click=lambda _: page.go("/veiculos"), width=200,
                                   color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ElevatedButton("Ordens de Serviço", on_click=lambda _: page.go("/ordens_servico"), width=200,
                                   color=ft.CupertinoColors.SYSTEM_PURPLE),
                ],
                bgcolor=Colors.PURPLE_900,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                padding=ft.padding.all(20)
            )
        )

        # Rotas de Clientes
        if page.route == "/clientes":
            page.views.append(
                View(
                    "/clientes",
                    [
                        Image(src="https://placehold.co/100x100/000000/FFFFFF?text=Clientes"),
                        AppBar(title=Text("Clientes"), bgcolor=Colors.YELLOW_700),
                        ElevatedButton("Cadastrar Cliente", on_click=lambda _: page.go("/cadastro_cliente"),
                                       width=250, color=ft.CupertinoColors.SYSTEM_PURPLE),
                        ElevatedButton("Visualizar Clientes", on_click=lambda _: page.go("/lista_clientes"),
                                       width=250, color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20)
                )
            )
        elif page.route == "/cadastro_cliente":
            page.views.append(
                View(
                    "/cadastro_cliente",
                    [
                        AppBar(title=Text("Cadastro de Cliente"), bgcolor=Colors.YELLOW_700),
                        nome_cliente,
                        cpf_cliente,
                        telefone_cliente,
                        endereco_cliente,
                        ElevatedButton("Salvar Cliente", on_click=salvar_cliente, width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                        ElevatedButton("Voltar ao Menu Clientes", on_click=lambda _: page.go("/clientes"), width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20),
                    scroll="auto"
                )
            )
        elif page.route == "/lista_clientes":
            page.views.append(
                View(
                    "/lista_clientes",
                    [
                        AppBar(title=Text("Lista de Clientes"), bgcolor=Colors.YELLOW_700),
                        lv_clientes,
                        ElevatedButton("Voltar ao Menu Clientes", on_click=lambda _: page.go("/clientes"), width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20)
                )
            )
            exibir_lista_clientes(None)  # Carrega a lista ao entrar na rota
        elif page.route == "/editar_cliente":
            page.views.append(
                View(
                    "/editar_cliente",
                    [
                        AppBar(title=Text("Editar Cliente"), bgcolor=Colors.YELLOW_700),
                        edit_nome_cliente,
                        edit_cpf_cliente,
                        edit_telefone_cliente,
                        edit_endereco_cliente,
                        ElevatedButton("Salvar Alterações", on_click=salvar_editar_cliente, width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                        ElevatedButton("Voltar à Lista", on_click=lambda _: page.go("/lista_clientes"), width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20),
                    scroll="auto"
                )
            )
        elif page.route == "/detalhes_cliente":
            page.views.append(
                View(
                    "/detalhes_cliente",
                    [
                        AppBar(title=Text("Detalhes do Cliente"), bgcolor=Colors.YELLOW_700),
                        txt_detalhes,
                        ElevatedButton("Voltar à Lista", on_click=lambda _: page.go("/lista_clientes"), width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20)
                )
            )

        # Rotas de Veículos
        elif page.route == "/veiculos":
            page.views.append(
                View(
                    "/veiculos",
                    [
                        Image(src="https://placehold.co/100x100/000000/FFFFFF?text=Veículos"),
                        AppBar(title=Text("Veículos"), bgcolor=Colors.YELLOW_700),
                        ElevatedButton("Cadastrar Veículo", on_click=lambda _: page.go("/cadastro_veiculo"),
                                       width=250, color=ft.CupertinoColors.SYSTEM_PURPLE),
                        ElevatedButton("Visualizar Veículos", on_click=lambda _: page.go("/lista_veiculos"),
                                       width=250, color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20)
                )
            )
        elif page.route == "/cadastro_veiculo":
            carregar_clientes_dropdown()  # Carrega clientes para o dropdown
            page.views.append(
                View(
                    "/cadastro_veiculo",
                    [
                        AppBar(title=Text("Cadastro de Veículo"), bgcolor=Colors.YELLOW_700),
                        marca_veiculo,
                        modelo_veiculo,
                        placa_veiculo,
                        ano_veiculo,
                        dd_cliente_veiculo,  # Dropdown para seleção de cliente
                        ElevatedButton("Salvar Veículo", on_click=salvar_veiculo, width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                        ElevatedButton("Voltar ao Menu Veículos", on_click=lambda _: page.go("/veiculos"), width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20),
                    scroll="auto"
                )
            )
        elif page.route == "/lista_veiculos":
            page.views.append(
                View(
                    "/lista_veiculos",
                    [
                        AppBar(title=Text("Lista de Veículos"), bgcolor=Colors.YELLOW_700),
                        lv_veiculos,
                        ElevatedButton("Voltar ao Menu Veículos", on_click=lambda _: page.go("/veiculos"), width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20)
                )
            )
            exibir_lista_veiculos(None)  # Carrega a lista ao entrar na rota
        elif page.route == "/editar_veiculo":
            page.views.append(
                View(
                    "/editar_veiculo",
                    {
                        AppBar(title=Text("Editar Veículo"), bgcolor=Colors.YELLOW_700),
                        edit_marca_veiculo,
                        edit_modelo_veiculo,
                        edit_placa_veiculo,
                        edit_ano_veiculo,
                        ElevatedButton("Salvar Alterações", on_click=salvar_editar_veiculo, width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                        ElevatedButton("Voltar à Lista", on_click=lambda _: page.go("/lista_veiculos"), width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                    },
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20),
                    scroll="auto"
                )
            )
        elif page.route == "/detalhes_veiculo":
            page.views.append(
                View(
                    "/detalhes_veiculo",
                    [
                        AppBar(title=Text("Detalhes do Veículo"), bgcolor=Colors.YELLOW_700),
                        txt_detalhes,
                        ElevatedButton("Voltar à Lista", on_click=lambda _: page.go("/lista_veiculos"), width=350,
                                       color=ft.CupertinoColors.SYSTEM_PURPLE),
                    ],
                    bgcolor=Colors.PURPLE_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    padding=ft.padding.all(20)
                )
            )

        # Rotas de Ordens de Serviço
        elif page.route == "/ordens_servico":
            page.views.append(
                View(
                    "/ordens_servico",
                    [
                        Image(src="https://placehold.co/100x100/000000/FFFFFF?text=OS"),
                        AppBar(title=Text("Ordens de Serviço"), bgcolor=Colors.YELLOW_700),
                        ElevatedButton("Cadastrar Ordem de Serviço",
                                       on_click=lambda _: page.go("/cadastro_ordem_servico"),
                                       width=250, color=ft.CupertinoColors.SYSTEM_PURPLE),
                        ElevatedButton("Visualizar Ordens de Serviço",
                                       on_click=lambda _: page.go("/lista_ordens_servico"),)]

if __name__ == "__main__":
    ft.app(target=main)