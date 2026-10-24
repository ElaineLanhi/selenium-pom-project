import pytest
from selenium.webdriver.support import expected_conditions as EC
from Tests.pages.carrinho_page import CarrinhoPage
from Tests.pages.login_page import LoginPage
from Tests.pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho #vai rodar somente os testes que tiverem a marcação "carrinho", quando passar o comando = pytest -m carrinho
class TestAdicionarProdutosCarrinho:
    def test_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()  

        #declarando variaveis para armazenar os nomes dos produtos que serão adicionados ao carrinho
        produto1 = "Sauce Labs Backpack"
        produto2 = "Sauce Labs Bolt T-Shirt"

        #faz o login com usuário e senha válidos
        login_page.fazer_login("standard_user", "secret_sauce")

        #ADICIONADO MOCHILHA NO CARRINHO
        home_page.adicionar_produto_carrinho(produto1)

        #VERIFICANDO QUE A MOCHILA FOI ADICIONADA NO CARRINHO
        home_page.clicar_icone_carrinho()
        #breakpoint() #colocar um ponto de parada para inspecionar o estado da aplicação, é uma forma de debugar
        carrinho_page.verificar_produto_carrinho_existe(produto1)

        #CLICANDO PARA VOLTAR PARA A PÁGINA DE PRODUTOS
        carrinho_page.clicar_botao_continuar_comprando()

        # #ADICIONANDO O PRODUTO "SAUCE LABS BIKE LIGHT" NO CARRINHO
        home_page.adicionar_produto_carrinho(produto2)

        # #VERIFICANDO QUE OS DOIS PRODUTOS FORAM ADICIONADOS NO CARRINHO
        home_page.clicar_icone_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        carrinho_page.verificar_produto_carrinho_existe(produto2)
