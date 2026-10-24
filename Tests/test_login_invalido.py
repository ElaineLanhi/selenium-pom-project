import pytest
from selenium.webdriver.common.by import By
from Tests.pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login #vai rodar somente os testes que tiverem a marcação "login", quando passar o comando = pytest -m login
class TestLoginInvalido:
    def test_login_invalido(self):

        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

        #chama os objetos a serem usados no teste
        login_page = LoginPage()
            
        
        #faz o login com usuário e senha válidos
        login_page.fazer_login("standard_user", "senha_errada")
        
        #Verifica se o login foi válido, e se a mensagem de erro apareceu
        login_page.verificar_mensagem_erro_login_existe()

        #Verifica o texto da mensagem de erro
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)


