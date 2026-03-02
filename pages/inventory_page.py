from pages.base_page import BasePage

class InventoryPage(BasePage):
    def validar_carregamento(self):
        return self.page.locator(".title").is_visible()

    def adicionar_produto_ao_carrinho(self, nome_produto_id):
        # Exemplo de ID: "sauce-labs-backpack"
        self.page.click(f"[data-test='add-to-cart-{nome_produto_id}']")

    def remover_produto_do_carrinho(self, nome_produto_id):
        self.page.click(f"[data-test='remove-{nome_produto_id}']")

    def obter_quantidade_carrinho(self):
        badge = self.page.locator(".shopping_cart_badge")
        if badge.is_visible():
            return badge.inner_text()
        return "0"

    def realizar_logout(self):
        self.page.click("#react-burger-menu-btn")
        self.page.click("#logout_sidebar_link")