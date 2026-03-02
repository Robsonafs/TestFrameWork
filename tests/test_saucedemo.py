import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


# Utilizamos uma fixture do pytest para evitar repetição de código (setup de login)
@pytest.fixture
def login_padrao(page):
    login_page = LoginPage(page)
    login_page.acessar()
    login_page.realizar_login("standard_user", "secret_sauce")
    return page


def test_login_com_sucesso(page):
    """Teste 1: Valida se o usuário consegue logar com credenciais válidas"""
    login_page = LoginPage(page)
    login_page.acessar()
    login_page.realizar_login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    assert inventory_page.validar_carregamento() is True


def test_login_com_falha(page):
    """Teste 2: Valida mensagem de erro ao usar senha incorreta"""
    login_page = LoginPage(page)
    login_page.acessar()
    login_page.realizar_login("standard_user", "senha_errada")

    erro = login_page.obter_mensagem_erro()
    assert "Username and password do not match" in erro


def test_adicionar_item_ao_carrinho(login_padrao):
    """Teste 3: Valida a adição de um produto e a atualização do ícone do carrinho"""
    inventory_page = InventoryPage(login_padrao)

    inventory_page.adicionar_produto_ao_carrinho("sauce-labs-backpack")
    quantidade = inventory_page.obter_quantidade_carrinho()

    assert quantidade == "1"


def test_remover_item_do_carrinho(login_padrao):
    """Teste 4: Valida se o contador do carrinho zera ao remover o produto"""
    inventory_page = InventoryPage(login_padrao)

    # Adiciona e depois remove
    inventory_page.adicionar_produto_ao_carrinho("sauce-labs-bike-light")
    inventory_page.remover_produto_do_carrinho("sauce-labs-bike-light")
    quantidade = inventory_page.obter_quantidade_carrinho()

    assert quantidade == "0"


def test_realizar_logout(login_padrao):
    """Teste 5: Valida se o usuário consegue sair da conta e voltar para a tela de login"""
    inventory_page = InventoryPage(login_padrao)
    inventory_page.realizar_logout()

    # Valida se o botão de login voltou a aparecer (indicando que deslogou)
    botao_login_visivel = login_padrao.locator("[data-test='login-button']").is_visible()
    assert botao_login_visivel is True