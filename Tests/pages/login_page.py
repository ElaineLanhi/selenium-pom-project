from Tests.pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class LoginPage(BasePage): #a class no python é usada para criar objetos que possuem atributos e métodos. No caso, estou criando uma classe chamada LoginPage que representa a página de login do site. Dentro da classe, estou definindo os elementos da página e os métodos para interagir com eles.

    def __init__(self): #o def __init__ é um método especial em Python que é chamado quando uma nova instância da classe é criada. Ele é usado para inicializar os atributos da classe e configurar o estado inicial do objeto. No caso, estou usando o __init__ para inicializar o driver do Selenium e os localizadores dos elementos da página de login.
        self.driver = conftest.driver #o self é usado para referenciar a instância atual da classe, permitindo acessar os atributos e métodos da classe. Aqui, estou atribuindo o driver do conftest à variável self.driver, para que possamos usá-lo em outros métodos da classe.
        self.username_field = (By.ID, "user-name") #aqui estou criando uma tupla com o localizador do campo de usuário
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//*[@data-test='error']") 

    def fazer_login(self, usuario, senha): #o def fazer_login é um método da classe LoginPage que recebe dois parâmetros: usuario e senha. Ele é responsável por preencher os campos de usuário e senha e clicar no botão de login.
        self.escrever(self.username_field, usuario) #aqui estou chamando o método escrever da classe BasePage para preencher o campo de usuário com o valor do parâmetro usuario
        self.escrever(self.password_field, senha) 
        self.clicar(self.login_button)

    def verificar_mensagem_erro_login_existe(self): #o def verificar_mensagem_erro é um método da classe LoginPage que verifica se a mensagem de erro de login inválido está visível na página. Ele retorna True se a mensagem estiver visível e False caso contrário.
        self.verificar_elemento_visivel(self.error_message_login)

    def verificar_texto_mensagem_erro_login(self, texto_esperado): 
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'."