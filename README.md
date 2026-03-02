# Framework de Automação de Testes Web Para o Projeto de Finalização da Pós Graduação em Testes Ágeis da C.E.S.A.R School

Este projeto é um framework de testes automatizados End-to-End (E2E) para aplicações Web, desenvolvido em **Python** utilizando **Playwright** e o executor de testes **Pytest**. 

O projeto foi estruturado seguindo o padrão **Page Object Model (POM)** para garantir uma separação clara entre a lógica de interação com as páginas e a lógica dos testes, facilitando a manutenção e a escalabilidade. O site utilizado como alvo dos testes é o [Sauce Demo](https://www.saucedemo.com/).

## 🛠️ Tecnologias Utilizadas

* **Python** (Linguagem de programação principal)
* **Playwright** (Motor de automação web)
* **Pytest** (Framework de testes)
* **pytest-playwright** (Plugin de integração)

## 📂 Estrutura do Projeto

A arquitetura do projeto está dividida da seguinte forma:

- `pages/`: Classes do Page Object Model.
  - `base_page.py`: Inicialização padrão das páginas.
  - `login_page.py`: Elementos e ações da tela de login.
  - `inventory_page.py`: Elementos e ações da tela de produtos.
- `tests/`: Casos de teste automatizados.
  - `test_saucedemo.py`: Arquivo principal com os 5 cenários.
- `pytest.ini`: Configurações de diretório do Pytest.
- `requirements.txt`: Lista de dependências do Python.

## 🧪 Cenários de Teste Automatizados

Os seguintes fluxos foram automatizados no site Sauce Demo:
1.  **Login com sucesso:** Valida o acesso com credenciais válidas.
2.  **Login com falha:** Valida a mensagem de erro ao tentar acessar com senha incorreta.
3.  **Adicionar ao carrinho:** Valida a inclusão de um produto e a atualização do ícone do carrinho.
4.  **Remover do carrinho:** Valida se o contador do carrinho zera ao remover um produto previamente adicionado.
5.  **Logout:** Valida se o usuário consegue sair da sessão e retornar à tela inicial.

## 🚀 Como Configurar e Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3** instalado na sua máquina.

### Passo 1: Clonar o repositório

### Passo 2: Instalar as dependências
Instale os pacotes necessários listados no arquivo requirements.txt:
```Bash
pip install -r requirements.txt
```

### Passo 3: Instalar os navegadores do Playwright
O Playwright precisa baixar os binários dos navegadores (Chromium, Firefox, WebKit) para rodar os testes:
```Bash
playwright install
```

### Passo 4: Executar os testes
Você pode rodar os testes de diferentes maneiras dependendo da sua necessidade:

Modo Headless (Execução rápida em segundo plano):
```Bash
pytest
```

Modo Headed (Abre o navegador visualmente):
```Bash
pytest --headed
```

Modo Detalhado (Mostra o status de cada teste individualmente):
```Bash
pytest -v
```
