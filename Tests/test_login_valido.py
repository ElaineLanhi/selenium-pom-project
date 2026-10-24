import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login #vai rodar somente os testes que tiverem a marcação "login", quando passar o comando = pytest -m login
class TestLoginValido:
    def test_login_valido(self):
        #chama os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()

        #faz o login com usuário e senha válidos
        login_page.fazer_login("standard_user", "secret_sauce")

        #verifica se o login foi bem-sucedido, verificando se o título da página inicial está visível
        home_page.verificar_login_sucesso() #chamando o método verificar_login_sucesso da classe HomePage para verificar se o login foi bem-sucedido, verificando se o título da página inicial está visível.


