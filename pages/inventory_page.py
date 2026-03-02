from pages.base_page import BasePage


class InventoryPage(BasePage):
    # --- Localizadores Estáticos ---
    TITULO_PAGINA = ".title"
    BADGE_CARRINHO = ".shopping_cart_badge"
    BOTAO_MENU = "#react-burger-menu-btn"
    LINK_LOGOUT = "#logout_sidebar_link"

    # --- Localizadores Dinâmicos (Templates) ---
    BOTAO_ADICIONAR_TEMPLATE = "[data-test='add-to-cart-{}']"
    BOTAO_REMOVER_TEMPLATE = "[data-test='remove-{}']"

    def validar_carregamento(self):
        return self.page.locator(self.TITULO_PAGINA).is_visible()

    def adicionar_produto_ao_carrinho(self, nome_produto_id):
        # Substitui as chaves {} pelo nome do produto passado no teste
        localizador = self.BOTAO_ADICIONAR_TEMPLATE.format(nome_produto_id)
        self.page.click(localizador)

    def remover_produto_do_carrinho(self, nome_produto_id):
        localizador = self.BOTAO_REMOVER_TEMPLATE.format(nome_produto_id)
        self.page.click(localizador)

    def obter_quantidade_carrinho(self):
        badge = self.page.locator(self.BADGE_CARRINHO)
        if badge.is_visible():
            return badge.inner_text()
        return "0"

    def realizar_logout(self):
        self.page.click(self.BOTAO_MENU)
        self.page.click(self.LINK_LOGOUT)