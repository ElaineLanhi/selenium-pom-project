# Automação de Testes Web com Selenium, Pytest e Page Object Model

Projeto de automação de testes end-to-end (E2E) para o site de demonstração [Sauce Demo](https://www.saucedemo.com/), desenvolvido em Python com **Selenium WebDriver** e **Pytest**, seguindo o padrão **Page Object Model (POM)**.

## O que é testado

Os testes cobrem o fluxo principal de compra do site:

1. **Login com credenciais válidas**: acesso à página de produtos após autenticação.
2. **Login com credenciais inválidas**: validação da mensagem de erro exibida.
3. **Adição de produtos ao carrinho**:
   - adiciona o primeiro item ao carrinho;
   - retorna à página inicial de produtos;
   - adiciona um segundo item;
   - acessa o carrinho e confere se os dois itens estão presentes.

## Tecnologias

- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

## Estrutura do projeto

```
.
├── conftest.py                  # Fixture que abre e fecha o navegador
├── requirements.txt             # Dependências do projeto
└── Tests/
    ├── pages/                   # Page Objects
    │   ├── base_page.py         # Métodos comuns reutilizados pelas páginas
    │   ├── login_page.py
    │   ├── home_page.py
    │   └── carrinho_page.py
    ├── test_login_valido.py
    ├── test_login_invalido.py
    └── test_adicionar_produtos_carrinho.py
```

## Como funciona

- O arquivo `conftest.py` define uma **fixture do Pytest** que abre o navegador Chrome, maximiza a janela e acessa o Sauce Demo antes de cada teste, e encerra o navegador ao final.
- Cada página do site possui uma classe própria em `Tests/pages/`, que concentra os seletores e as ações daquela tela. Isso evita repetição de código e facilita a manutenção caso o site mude.
- A `BasePage` reúne os métodos genéricos (como localizar elementos e clicar), que são reaproveitados por todas as outras páginas.
- Os testes ficam enxutos e legíveis, pois só descrevem o fluxo, sem se preocupar com os detalhes de como cada elemento é encontrado.

## Como executar

### Pré-requisitos

- Python 3 instalado
- Google Chrome instalado

### Passo a passo

1. Clone o repositório:

   ```bash
   git clone https://github.com/ElaineLanhi/selenium-pom-project.git
   cd selenium-pom-project
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Linux/Mac
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute os testes:

   ```bash
   pytest
   ```

   Para ver mais detalhes da execução:

   ```bash
   pytest -v
   ```

## Autora

**Elaine Lanhi**

Profissional de QA e documentação técnica, em transição para automação de testes.

[GitHub](https://github.com/ElaineLanhi)
