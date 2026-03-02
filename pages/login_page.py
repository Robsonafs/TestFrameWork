from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # --- Localizadores ---
    INPUT_USUARIO = "[data-test='username']"
    INPUT_SENHA = "[data-test='password']"
    BOTAO_LOGIN = "[data-test='login-button']"
    MENSAGEM_ERRO = "[data-test='error']"

    def acessar(self):
        self.page.goto(self.URL)

    def realizar_login(self, usuario, senha):
        self.page.fill(self.INPUT_USUARIO, usuario)
        self.page.fill(self.INPUT_SENHA, senha)
        self.page.click(self.BOTAO_LOGIN)

    def obter_mensagem_erro(self):
        return self.page.inner_text(self.MENSAGEM_ERRO)