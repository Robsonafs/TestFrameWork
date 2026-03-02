from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def acessar(self):
        self.page.goto(self.URL)

    def realizar_login(self, usuario, senha):
        self.page.fill("[data-test='username']", usuario)
        self.page.fill("[data-test='password']", senha)
        self.page.click("[data-test='login-button']")

    def obter_mensagem_erro(self):
        return self.page.inner_text("[data-test='error']")